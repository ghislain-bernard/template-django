## template-django

[![django.webp](django.webp)](https://www.djangoproject.com)

### usage

```bash
$ ./manage.py check
System check identified no issues (0 silenced).

$ ./manage.py collectstatic

3 static files copied to '/home/user/git/template-django/dist/static'.

$ DJANGO_RUNSERVER_HIDE_WARNING=true ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 20, 2025 - 22:34:58
Django version 5.2.1, using settings None
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[22/Oct/2025 13:11:09] "GET / HTTP/1.1" 200 699
[22/Oct/2025 13:11:09] "GET /static/style.css HTTP/1.1" 200 881
[22/Oct/2025 13:11:09] "GET /static/img/django.webp HTTP/1.1" 200 8708
[22/Oct/2025 13:11:09] "GET /static/favicon.ico HTTP/1.1" 200 318
^C

$ yapf --in-place --verbose manage.py
Reformatting manage.py

$ yapf --in-place --verbose project/{asgi,settings,urls,wsgi}.py
Reformatting project/asgi.py
Reformatting project/settings.py
Reformatting project/urls.py
Reformatting project/wsgi.py

$ yapf --in-place --verbose portal/{apps,views}.py
Reformatting portal/apps.py
Reformatting portal/views.py

$ pylint --verbose manage.py
Using config file /home/user/git/template-django/.pylintrc
Get ASTs.
AST for manage.py
Linting 1 modules.
manage.py (1 of 1)

$ pylint --verbose project/{asgi,settings,urls,wsgi}.py
Using config file /home/user/git/template-django/.pylintrc
Get ASTs.
AST for project/asgi.py
AST for project/settings.py
AST for project/urls.py
AST for project/wsgi.py
Linting 4 modules.
project/asgi.py (1 of 4)
project/settings.py (2 of 4)
project/urls.py (3 of 4)
project/wsgi.py (4 of 4)

$ pylint --verbose portal/{apps,views}.py
Using config file /home/user/git/template-django/.pylintrc
Get ASTs.
AST for portal/apps.py
AST for portal/views.py
Linting 2 modules.
portal/apps.py (1 of 2)
portal/views.py (2 of 2)

$ mypy manage.py
Success: no issues found in 1 source file

$ mypy project/{asgi,settings,urls,wsgi}.py
Success: no issues found in 4 source files

$ mypy portal/{apps,views}.py
Success: no issues found in 2 source files

$ make clean

/!\ cleaning...
rm -f -rv project/__pycache__ portal/__pycache__ dist
removed 'project/__pycache__/__init__.cpython-314.pyc'
removed 'project/__pycache__/settings.cpython-314.pyc'
removed 'project/__pycache__/urls.cpython-314.pyc'
removed directory 'project/__pycache__'
removed 'portal/__pycache__/__init__.cpython-314.pyc'
removed 'portal/__pycache__/apps.cpython-314.pyc'
removed 'portal/__pycache__/views.cpython-314.pyc'
removed directory 'portal/__pycache__'
removed 'dist/static/favicon.ico'
removed 'dist/static/style.css'
removed 'dist/static/img/django.webp'
removed directory 'dist/static/img'
removed directory 'dist/static'
removed directory 'dist'
...done
```

> MIT License  
> ghislain.bernard@gmail.com
