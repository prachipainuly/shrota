# shrota
A gaming web app for capturing ASL gestures and converting them to text.

Steps to run backend server:

1. Make sure to cd shrota/server
2. Pip install requirements
3. cd backend 
   Since, manage.py is the initial file for our Django backend,
   we will now run commands from root of the project that is backend.
4. Run python manage.py makemigrations
   This creates data models.
5. Run python manage.py migrate
6. You can run python manage.py shell to enter interactive shell and exit() to come out
7. To add data to models:
   from shrota.models import Word 
   Word.objects.create(id=1, name='Banana', category='Fruits')
8. Finally, to run the backend server, use command
   python manage.py runserver
   Make sure you are in the root of project while running this command: server/backend/
9. Go to http://127.0.0.1:8000/ to access end points
