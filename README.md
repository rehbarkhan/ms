# ms
XYZ College Management System - Django

### Steps to run this project in your computer.
<pre>
1 . clone this project
2 . cd to this project i,e ms
3 . execute - virtualenv .
4 . source bin/activate (MacOS / Linux) & Script/activate ( Windows )
5 . pip install -r requ.txt
6 . python manage.py makemigrations
7 . python manage.py migrate
8 . python manage.py populate_db [ note down the username password which will generate]
6 . python manage.py runserver
After running server you will get the ipaddress to access this project.
</pre>

<pre>
 ### Always use branch and create a pr for merging the changes
</pre>

#### How to generate random secrete key for django app
- python manage.py shell
- from django.core.management.utils import get_random_secret_key
- get_random_secret_key()
