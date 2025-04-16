- python -m django startproject mysite djangotutorial (create django project)
- python manage.py startapp polls (add section in project)
- python manage.py runserver (start server)
- python manage.py migrate (The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .tables (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.
)
- python manage.py makemigrations (By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.)
-  python manage.py check ( this checks for any problems in your project without making migrations or touching the database.)
- python manage.py shell ( the shell command automatically imports the models from your INSTALLED_APPS.)
- python manage.py createsuperuser