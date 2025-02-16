Project:- Segwise
Repo-> https://github.com/sabbir2609/zenith-b
Repo-> https://github.com/alamorre/django-docker
Setup
1. python3 -m venv .venv
2.  source .venv/bin/activate
3. pip install django if required upgrade then:- pip install --upgrade pip
4. pip freeze > requirements.txt
5. Start Project -> django-admin startproject EventTrigger
6. Move directory -> cd EventTrigger
7. Migrate data -> python manage.py makemigrations then -> python manage.py migrate
8. If you want to create superuser then ->  python manage.py createsuperuser then enter username -> email address -> password -> password again -> Bypass password validation and create user anyway? [y/N]: Y 
Then Superuser created successfully.
9. Create app -> python manage.py startapp app_name
Extra point -> pip install gunicorn psycopg2-binary

Docker:- 
1 docker build -t event-trigger:latest .   

DB
1. python manage.py dbshell to check connection 
2. Sql -u postgres


   https://docs.google.com/document/d/1uxCXqQJMZDAPfHhcRP3PNPg6HPPDE3p-sES6XLvO6KA/edit?tab=t.0

https://www.youtube.com/@adam_la_morre

https://github.com/alamorre/django-docker/blob/main/Dockerfile


https://github.com/sabbir2609/zenith-be/blob/main/docker/Dockerfile

https://github.com/gaurav637/IssueTrackerApp/blob/main/docker-compose.yml

https://github.com/andyjud/docker/blob/main/.dockerignore
