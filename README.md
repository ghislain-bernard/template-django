## template-django

[![django.webp](django.webp)](https://www.djangoproject.com)

### usage

```bash
$ ./manage.py check
System check identified no issues (0 silenced).

$ ./manage.py makemigrations
Migrations for 'portal':
  portal/migrations/0001_initial.py
    + Create model Element

$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, portal, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying portal.0001_initial... OK
  Applying sessions.0001_initial... OK

$ ./manage.py createsuperuser --username=admin --email=
Password: 
Password (again): 
Superuser created successfully.

$ ./manage.py collectstatic

130 static files copied to '/home/user/git/template-django/dist/static'.

$ ./manage.py shell
7 objects imported automatically (use -v 2 for details).

Python 3.14.0 (main, Oct 22 2025, 19:45:08) [GCC 15.2.1 20250813]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use `ipython --help-all | less` to view all the IPython configuration options.

In [1]: import portal.models

In [2]: portal.models.Element(name='127.0.0.1').save()

In [3]: portal.models.Element(name='::1').save()

In [4]: exit

$ DJANGO_RUNSERVER_HIDE_WARNING=true ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 27, 2025 - 01:43:15
Django version 5.2.7, using settings None
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[27/Oct/2025 02:09:16] "GET / HTTP/1.1" 200 699
[27/Oct/2025 02:09:16] "GET /static/style.css HTTP/1.1" 200 881
[27/Oct/2025 02:09:16] "GET /static/img/django.webp HTTP/1.1" 200 8708
[27/Oct/2025 02:09:16] "GET /static/favicon.ico HTTP/1.1" 200 318
[27/Oct/2025 02:09:36] "GET /admin/ HTTP/1.1" 302 0
[27/Oct/2025 02:09:36] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4178
[27/Oct/2025 02:09:36] "GET /static/admin/css/base.css HTTP/1.1" 200 22120
[27/Oct/2025 02:09:36] "GET /static/admin/css/responsive.css HTTP/1.1" 200 16565
[27/Oct/2025 02:09:36] "GET /static/admin/js/theme.js HTTP/1.1" 200 1653
[27/Oct/2025 02:09:36] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2808
[27/Oct/2025 02:09:36] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2810
[27/Oct/2025 02:09:36] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[27/Oct/2025 02:09:36] "GET /static/admin/css/login.css HTTP/1.1" 200 951
[27/Oct/2025 02:09:36] "GET /favicon.ico HTTP/1.1" 301 0
[27/Oct/2025 02:09:36] "GET /static/favicon.ico HTTP/1.1" 200 318
^C

$ yapf --in-place --verbose manage.py
Reformatting manage.py

$ yapf --in-place --verbose project/{asgi,settings,urls,wsgi}.py
Reformatting project/asgi.py
Reformatting project/settings.py
Reformatting project/urls.py
Reformatting project/wsgi.py

$ yapf --in-place --verbose portal/{apps,views}.py portal/{admin,models}.py
Reformatting portal/apps.py
Reformatting portal/views.py
Reformatting portal/admin.py
Reformatting portal/models.py

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

$ pylint --verbose portal/{apps,views}.py portal/{admin,models}.py
Using config file /home/user/git/template-django/.pylintrc
Get ASTs.
AST for portal/apps.py
AST for portal/views.py
AST for portal/admin.py
AST for portal/models.py
Linting 4 modules.
portal/apps.py (1 of 4)
portal/views.py (2 of 4)
portal/admin.py (3 of 4)
portal/models.py (4 of 4)

$ mypy manage.py
Success: no issues found in 1 source file

$ mypy project/{asgi,settings,urls,wsgi}.py
Success: no issues found in 4 source files

$ mypy portal/{apps,views}.py portal/{admin,models}.py
Success: no issues found in 4 source files

$ make clean

/!\ cleaning...
rm -f -rv project/__pycache__ portal/__pycache__ portal/migrations/__pycache__
removed 'project/__pycache__/__init__.cpython-314.pyc'
removed 'project/__pycache__/settings.cpython-314.pyc'
removed 'project/__pycache__/urls.cpython-314.pyc'
removed directory 'project/__pycache__'
removed 'portal/__pycache__/__init__.cpython-314.pyc'
removed 'portal/__pycache__/apps.cpython-314.pyc'
removed 'portal/__pycache__/models.cpython-314.pyc'
removed 'portal/__pycache__/admin.cpython-314.pyc'
removed 'portal/__pycache__/views.cpython-314.pyc'
removed directory 'portal/__pycache__'
removed 'portal/migrations/__pycache__/__init__.cpython-314.pyc'
removed 'portal/migrations/__pycache__/0001_initial.cpython-314.pyc'
removed directory 'portal/migrations/__pycache__'
rm -f -r dist
rm -f -v django.sqlite3 django.sqlite3-journal portal/migrations/[0-9][0-9][0-9][0-9]_*.py
removed 'django.sqlite3'
removed 'portal/migrations/0001_initial.py'
...done
```

> MIT License  
> ghislain.bernard@gmail.com
