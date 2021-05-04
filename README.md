# click2buy
An Ecommerce webiste.

## Starting the project
* create a virtual environment: `python -m venv venv`
* start the venv: `venv\scripts\activate` or `source venv/bin/activate`
* install requirements: `pip install -r requirements.txt`
* install frontend dependencies: 
    * cd into the frontend folder: `cd frontend`
    * install dependencies: `npm install`
* start servers:
    * django server: `django manage.py runserver`
    * react server: `npm start`
    
> The project can be viewed on both servers; i.e `localhost:8000` and `localhost:3000`
> but the react server needs the django server up for it to function. Also, any changes
>made in the react app and be effected by running `yarn build` in the frontend directory.
>I have already ran `yarn build`, so no need except any further changes are made.
--------
#### Super user details
username : `admin@cllick2buy.com`

password : `asdf:lkj`

if that doesn't work, create a new superuser using : `python manage.py createsuperuser`