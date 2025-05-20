## template-django

[![django.webp](django.webp)](https://www.djangoproject.com)

### usage

```console
$ ./server.py check
System check identified no issues (0 silenced).

$ DJANGO_RUNSERVER_HIDE_WARNING=true ./server.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 20, 2025 - 22:34:58
Django version 5.2.1, using settings None
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

^C

$ gunicorn server
[2025-05-20 22:36:02 +0200] [2549713] [INFO] Starting gunicorn 23.0.0
[2025-05-20 22:36:02 +0200] [2549713] [INFO] Listening at: http://127.0.0.1:8000 (2549713)
[2025-05-20 22:36:02 +0200] [2549713] [INFO] Using worker: sync
[2025-05-20 22:36:02 +0200] [2549819] [INFO] Booting worker with pid: 2549819
^C
[2025-05-20 22:36:03 +0200] [2549713] [INFO] Handling signal: int
[2025-05-20 22:36:03 +0200] [2549819] [INFO] Worker exiting (pid: 2549819)
[2025-05-20 22:36:04 +0200] [2549713] [INFO] Shutting down: Master

$ yapf --in-place --verbose server.py core/settings.py core/urls.py core/portal/views.py
Reformatting server.py
Reformatting core/settings.py
Reformatting core/urls.py
Reformatting core/portal/views.py

$ pylint --verbose server.py core/settings.py core/urls.py core/portal/views.py
Using config file /home/user/git/template-django/.pylintrc

$ mypy server.py core/settings.py core/urls.py core/portal/views.py
Success: no issues found in 4 source files
```

> MIT License  
> ghislain.bernard@gmail.com
