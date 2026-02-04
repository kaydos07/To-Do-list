# Django To-Do App with PostgreSQL

A To-Do List application built with basic features from beginner code

## Features
* **Add Tasks:** Save new tasks directly to the PostgreSQL database.
* **Toggle Status:** Click tasks to mark them as Complete/Incomplete (Dynamic UI).
* **Delete Tasks:** Remove tasks permanently.
* **Persistent Data:** Data is stored in a local PostgreSQL server.
* **Progressing:** Show progress on finishing task. 

## Tech Stack
* **Backend:** Django (Python)
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS, Django Template Language (DTL)

## How to Run This Project

### 1. Prerequisites
* Python installed.
* PostgreSQL installed and running (PgAdmin 4).

### 2. Installation
Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/django-todo.git](https://github.com/YOUR_USERNAME/django-todo.git)
cd django-todo
pip install -r requirements.txt
```

### 3. Database setup

* create file named ```.env```
* Add your local database credentials:
```
DB_NAME=project1
DB_USER=postgres
DB_PASSWORD=YOUR_ACTUAL_DB_PASSWORD
DB_HOST=localhost
SECRET_KEY=YOUR_GENERATED_SECRET_KEY
```
* create table:
```
python manage.py migrate
```
* start server:
```
python manage.py runserver
```

