# the-game

This is a work in progress game.

## Dependencies

* python
* pip

## Usage

Create a virtualenv:

```cmd
$ pip3 install virtualenv
$ virtualenv venv
```

Activate the virtualenv by using the provided `activate` script:

```cmd
$ source venv/bin/activate
(venv) $
```

Inside the virtualenv, install the dependencies:

```cmd
(venv) $ pip install flask jinja2
```

Run the app:

```cmd
(venv) $ env FLASK_APP=main.py flask run
```

We may eventually get around to some actual build tooling.
