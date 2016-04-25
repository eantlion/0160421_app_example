teacherapp
==========

INSTALLATION
------------

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

	pip install -r /path/to/requirements.txt

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

	GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
Replace 'myuser' with the user name you selected above

You must then add the username and password you created to ./teacherapp/settings.py:ln84-85




Adding Dependencies
-------------------

1. Install the dependency using `pip`
2. Save it by running `pip freeze > requirements.txt`
