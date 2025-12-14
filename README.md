# blog   
## This project is designed for people to use like a forum, where they can share their lives with each other.
### In this project, with the help of others, people can share their experiences and help each other correct mistakes.
####
### Download requirements.txt and how to download it:
```bash
pip install -r requirements.txt
```
### Create a new file named `.env` in the project root folder.  
### Add the newly generated Django `SECRET_KEY` and set `DEBUG=True` in this file
### how create new django secret key:
```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
## Project structure
- ### blog
  - core <- this is app
    - migrations
    - __init__.py
    - admin.py
    - apps.py
    - auth_models.py
    - auth_views.py
    - models.py
    - tests.py
    - urls.py 
    - views.py
  - src <- this is project
    - __init__.py
    - asgi.py
    - settings.py
    - urls.py
    - wsgi.py
  - static <- This is your styles and javascripts
  - template
    - partials
      - login.html <- this is your login
      - register.html<- this is your register
    - add-post.html
    - filter-author.html
    - index.html
