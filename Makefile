############################################## ghislain.bernard@gmail.com ##############################################

all: clean

SHELL = /usr/bin/env bash

########################################################################################################################

clean:
	@echo ''
	@echo -e '/!\ cleaning...'

	$(RM) -rv project/__pycache__ portal/__pycache__ portal/migrations/__pycache__
	$(RM) -r dist
	$(RM) -v django.sqlite3 django.sqlite3-journal portal/migrations/[0-9][0-9][0-9][0-9]_*.py

	@echo ...done

############################################## ghislain.bernard@gmail.com ##############################################
