# shrota
A gaming web app for capturing ASL gestures and matching them for correctness.

Steps to run backend server:

1. Make sure to cd shrota/server
2. Pip install -r requirements
3. cd backend 
   Since, manage.py is the initial file for our Django backend,
   we will now run commands from root of the project that is backend.
4. Run python manage.py makemigrations
   This creates data models.
5. Run python manage.py migrate
6. You can run python manage.py shell to enter interactive shell and exit() to come out
7. To add data to models manually:
   from shrota.models import Word 
   Word.objects.create(id=1, name='Banana', category='Fruits')
8. To load alphabets to DB, run the script:
    python manage.py runscript load_database
9. Finally, to run the backend server, use command
   python manage.py runserver
   Make sure you are in the root of project while running this command: server/backend/
10. Go to http://127.0.0.1:8000/ to access end points

Steps to run frontend ui:
1. Make sure to have npm installed in local machine
2. cd frontend
3. npm i
4. npm start
5. Access the UI on localhost:3000/
