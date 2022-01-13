# Homework 12 
Files with tasks from homework are the following:
* `task1/models.py`
* `task1/migrations/0001_initial.py`
* `task1/migrations/0002_auto_20220104_1507.py`

## Solution Notes 

<mark>
These notes were originally done for myself to track commands which I execute. 
However finally I decided to keep them as README.md
</mark>

### Project Initialization
This project was automatically generated using  command
```
django-admin startproject homework12
```
After that I changed `DATABASES` variable in `settings.py` to satisfy the condition in the task description.

### App Initialization
Then I created Django App `task1` with command 
```
python manage.py startapp task1
```
It generated folder `task1` with following structure.

TODO: folder structure

After that I added `task1` to `INSTALLED_APPS` variable in `setting.py` file.

### Generate Migrations 
I generated initial schema migrations based on implemented models in `task1/models.py` using command:
```
python manage.py makemigrations task1
```

I generated empty migration to implement data migration using command:
```
python manage.py makemigrations --empty task1
```

### Run migrations 
I applied migrations to sqlite3 database `main.db` using command 
```
python manage.py migrate task1
```