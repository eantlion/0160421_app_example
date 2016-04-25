teacherapp
==========

INSTALLATION
------------

These instructions assume installation under linux system running ubuntu 14.04

Requirements: 

Install pip: https://pip.pypa.io/en/stable/installing/

Install virtualenv: https://virtualenv.pypa.io/en/latest/installation.html


Update Packages

	sudo apt-get update

	sudo apt-get upgrade

git clone the project

While inside the project folder

	sudo virtualenv ./myenv

	source ./myenv/bin/activate

	pip install -r ./requirements.txt

Install postgres: 

	deactivate

	sudo apt-get install libpq-dev python-dev

	sudo apt-get install postgresql postgresql-contrib

Configure PostgreSQL

	source ./myenv/bin/activate

	sudo su - postgres

	createdb teacherdb

	createuser -P --interactive
You will receive 6 prompts: 

username, password, and confirm password are up to you, the last 3 just enter 'n'

	psql

	GRANT ALL PRIVILEGES ON DATABASE teacherdb TO myuser;
Replace 'myuser' with the user name you selected above

	\q

	exit

You must then add the username and password you created to ./teacherapp/settings.py:ln84-85


FIRST RUN
---------

	source ./myenv/bin/activate

	cd teacherapp/

	python manage.py migrate

	python manage.py collectstatic

	python manage.py createsuperuser

This will be the username you use to access admin dashboard at localhost:8000/admin/


Adding Dependencies
-------------------

1. Install the dependency using `pip`
2. Save it by running `pip freeze > requirements.txt`




USAGE
=====

Registering
-----------
Navigate to localhost:8000

To create a teacher account, click the Register button and fill out the form, then submit

To log in, either with the new teacher or with your admin account, fill out Username and Password and click Login

You will be redirected to the dashboard


Creating Students
-----------------
Navigate to Dashboard

Click the 'Create a new student record' 

Fill out form and submit

You will be redirected to student details page for the newly created student

Admin Accounts:

You can also access localhost:8000/admin and navigate to students and add them through there.



Creating Classrooms
-------------------
Navigate to Dashboard

Click the 'Create a new classroom' 

Fill out form and submit

You will be redirected to classroom details page for the newly created classroom



Adding/Removing Students from Classroom
---------------------------------------
Navigate to Dashboard

Click 'View your classrooms'

Click the classroom you want to add/remove students from the list

Click 'You can add/remove students here'

Two lists with checkboxed entries denote students currently enrolled and students not enrolled

Check all you would like to remove from the first list

Check all you would like to add from the second list

Press submit

Changes should happen immediately and be reflected on the page