
<br />
<div align="center">
  <img src="./assets/logo.png" alt="mail package manager logo" height="150" />
  <h1>
    <font color="#9E4D3B">Tutor's Companion</font>
  </h1>
</div>
<p align="center">
  <br />
  <img alt="Python" src="https://img.shields.io/badge/python%403.9.6-lightblue">
  <img alt="Django" src="https://img.shields.io/badge/django%404.2.5-lightgreen">
  <img alt="Static Badge" src="https://img.shields.io/badge/django--rest--framework%403.14.0-red">


  <br />
</p>

## Table of contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment variables](#environment-variables)
- [Running the app](#running-the-app)

## Description

A backend application to manage a small private tutoring business.

## Requirements
 - Python 3.9.6
 - Django 4.2.5
 - Django REST Framework 3.14.0

## Installation
Once you've cloned the repository, your next step is to establish a virtual environment to ensure a pristine Python installation. This can be achieved by executing the following command:

```bash
$ python -m venv env
```

After this, it becomes essential to activate the virtual environment. For additional details on this step, you can find more information [here](https://docs.python.org/3/tutorial/venv.html):

To install all the necessary dependencies, execute the command:

```
$ pip install -r requirements.txt
```

## Environment variables

Create a `.env` file with the following in the root

```bash
# server mode
$ DEBUG=<DEBUG>

# app secret
$ SECRET_KEY=<SECRET_KEY>

# database name
$ DATABASE_NAME=<DATABASE_NAME>

# database host
$ DATABASE_HOST=<DATABASE_HOST>

# database user
$ DATABASE_USER=<DATABASE_USER>

# database user password
$ DATABASE_PASSWORD=<DATABASE_PASSWORD>

# database port
$ DATABASE_PORT=<DATABASE_PORT>
```

## Running the app

To start up the Django's development server, navigate to the root of the project and run the command:
```
$ python manage.py runserver
```
