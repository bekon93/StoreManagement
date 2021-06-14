Steps to run the project

1. Open the project with PyCharm
2. Run the sm.py file
3. Access the project with a browser on localhost

This is a simple project that will be able to manage a small local store,
you will be able to Manage employees, items(products) and orders, by doing some basic operations like
adding, editing and deleting stuff.

You can find the templates that are used on the templates folder, also the static folder has the css and js part of the project,
on the db  folder you can check how is the database organized and how are the tables created.

On the controller.py u can find the methods that are created based on the SQLAlchemy that 
manage the databases and requests from the users.

On the requirements.txt u can check the libraries that the project needs to work.


On the testing.py we have added some test using unittest library to check that the code runs as it should.

All the code that connects the database, controller and temlates is written on sm.py, all the routes are defined in this file of the project.

Some of the ddl scripts are written on the controller.py using SQLAlchemy and some of them are written on sm.py using sqlite3, just so the project has both of them included.

