# Simple DRF

Simple webapp to explore what DRF can do for specific cases.

Feature: we create cities object (model 'City') while fetching their local weather temperature before persiting them into our DB.

## Install

```shell
git clone git@github.com:simcap/simpledrf.git
cd simplrdrf
python3 manage.py makemigrations
python3 manage.py migrate
```

## Test 

```shell
python3 manage.py test
```

## Run

```shell
python3 manage.py runserver
```

## Usage

Once the service is running, create a new city from the terminal:

```shell
curl --data "name=paris&lon=2.35&lat=48.75" http://127.0.0.1:8000/cities/new
```

List all your current cities via the terminal:

```shell
curl -H"Accept: application/json; indent=2" http://127.0.0.1:8000/cities/ 
```

... or browse to [http://127.0.0.1:8000/cities/](http://127.0.0.1:8000/cities/).