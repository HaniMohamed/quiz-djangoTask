# quiz-djangoTask
A quiz app using django framework.

## Running Project

- Install [Python3.9.1](https://www.python.org/downloads/)
- Install [docker](https://www.docker.com/products/docker-desktop)
- Install [docker-compose](https://docs.docker.com/compose/)
- clone the project using [git](https://git-scm.com/downloads)
- [`cd`](https://linuxize.com/post/linux-cd-command/) into the project
- run `docker-compose up --build` to run the db and project container (and leave it running)
- Visit the project on this URL: [localhost:8000/api/v1/](http://localhost:8000/api/v1/)

## Seeding database
to generate dummy data using package called "django-seed"
- run `docker-compose exec web python manage.py seed quiz --number=100` or any number 
