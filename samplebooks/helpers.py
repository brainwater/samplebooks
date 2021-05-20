import requests
from samplebooks_site.settings import GOOGLEAPI_KEY, AUTHOR_MAX_LENGTH, GOOGLEAPI_VOLUME_URL


# TODO: Currently just does a general query with the given text, instead of specifically for the author name
def google_search_author(author_name):
    assert(len(author_name) <= AUTHOR_MAX_LENGTH)
    query_params = {'q': author_name,
                    'key': GOOGLEAPI_KEY}
    # TODO: Throw exception if request fails
    json_response = requests.get(GOOGLEAPI_VOLUME_URL, query_params).json()
    print(json_response)
    # TODO: Throw exception if invalid response format
    # Asserting that the response is sane, books contain titles, ids, and authors
    assert(all(
        all(['id' in book,
             'volumeInfo' in book,
             'title' in book['volumeInfo'],
             len(book['volumeInfo']['authors']) >= 1])
        for book in json_response['items']))
    booklist = json_response['items']
    # TODO: determine best way to implement pagination
    return booklist

def google_book_details(book_id):
    detail_url = GOOGLEAPI_VOLUME_URL + '/' + book_id
    # TODO: throw exception if request fails
    json_response = requests.get(detail_url).json()
    # Asserting that the book contains an author, title, image, published date, and description
    assert('volumeInfo' in json_response)
    volume_info = json_response['volumeInfo']
    assert('title' in volume_info)
    assert('authors' in volume_info)
    assert(len(volume_info['authors']) >= 1)
    assert('imageLinks' in volume_info)
    assert(len(volume_info['imageLinks']) >= 1)
    assert('description' in volume_info)
    assert('publishedDate' in volume_info)
    # TODO: determine if google could ever fail to provide any of the image links
    # Default to the Large image, but provide any image in the image links list.
    imageLink = list(volume_info['imageLinks'].values())[0]
    if 'large' in volume_info['imageLinks']:
        imageLink = volume_info['imageLinks']['large']
    parameters = {
        'imageLink': imageLink,
        'title': volume_info['title'],
        'author': volume_info['authors'][0],
        'description': volume_info['description'],
        'publishedDate': volume_info['publishedDate'],
    }
    return parameters


# TODO: add caching to prevent hammering the google API
def _book_title(book_id):
    detail_url = GOOGLEAPI_VOLUME_URL + '/' + book_id
    # TODO: throw exception if request fails
    json_response = requests.get(detail_url).json()
    assert('volumeInfo' in json_response)
    assert('title' in json_response['volumeInfo'])
    return json_response['volumeInfo']['title']

def review_list(reviews):
    # TODO: handle excpetions for problem books
    return [{'content': review.content,
             'book_title': _book_title(review.book_id),
             'book_id': review.book_id,}
            for review in reviews]
    
    

