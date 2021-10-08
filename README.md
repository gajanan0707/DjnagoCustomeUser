# DjnagoCustomeUser
## Setup

Create a virtual environment to install dependencies in and activate it:

```sh
$ sudo pip3 install virtualenv

Now create a virtual environment
$ virtualenv venv 

Active your virtual environment:
$ source venv/bin/activate

To deactivate:
    deactivate

```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
-------------------Steps----------------
1)(venv)$ cd customeuser
2)(venv)$ python manage.py runserver

```
And navigate to `http://127.0.0.1:8000/admin`.