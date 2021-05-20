# Google API Book Review Miniapp

## Running Locally

This application uses a default sqlite database, and has only been tested on linux

Requirements:
- Python3 (tested with python 3.6.8)
- VirtualEnv (python3-virtualenv)

Clone from github:
```$ git clone https://github.com/brainwater/samplebooks```
```$ cd samplebooks```

Install python3 and python3-virtualenv:
```$ sudo apt install python3 python3-virtualenv```

Set up the virtualenv:
```$ virtualenv -p python3 env```

Activate the virtualenv:
```$ . env/bin/activate```

Install the pip dependencies:
```$ pip install -r requirements.txt```

Set the environment variable with the Google API Key:
```$ export GOOGLEAPI_KEY='AIz...7b8'```

Migrate the database:
```$ python manage.py migrate```

Run the server:
```$ python manage.py runserver```

Open ```localhost:8000``` in your browser

## Notes

Type in your Author's name in the text box on the home page and hit 'Submit'.
You will see a list of books, click on one of the book titles.
The title, author, publication date, image, description, review submission form, and existing reviews will be shown.
Type your review into the 'Review Content' text box and submit your review.
You will now see your review in the list of reviews at the bottom of the page.


Return to the index page at ```localhost:8000``` in your browser. You will now see a list of reviews and the book title, and you can click on the book title to go to that book's page and see the reviews just for that book.

## Further work

- Error handling
 - If the google api requests fail, there isn't a graceful fallback or helpful error message for the user
 - When the title, author, or other information is missing, the application doesn't have an informative error message for the user nor a fallback strategy
- The image shown is sometimes a 'default' image provided by google
- No header is yet included for site navigation back to the home page
- There is no way to delete existing reviews
- There is no user authentication nor management yet
- UI attractiveness and organization is essentially nonexistant
- Django secret key isn't kept within the environment variables (this matters for things like CSRF prevention)
- Pagination to show more than one query of book results
- Pagination of user reviews to prevent arbitrary size list




