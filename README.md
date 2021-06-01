# library

[upwork](https://www.upwork.com/ab/proposals/1395617258159792129)

**Write a small library application in Django.**

Features:
+ [x] User can login to the system
+ [x] User can borrow a book (check out)
+ [x] User can return a book (check in)
+ [x] If a book is no longer available because it has been checked out, please display a validation error.
+ [x] If the book is available for checkout, please display a success message when the book is successfully checked out.
+ [x] Write a fixture for loading up several books.


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/gamifications/library
```

Create Virtual Env and Install the requirements:

```bash
cd library
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Create the database and run the development server:

```bash
python manage.py migrate
python manage.py loaddata datas.json
python manage.py runserver
```

Running tests

```bash
python manage.py test
```