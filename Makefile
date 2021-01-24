SHELL := /bin/bash


ifeq ($(uname_S), Windows)
    venv\Scripts\activate.bat
endif

ifeq ($(uname_S), Linux)
    . venv/bin/activate
endif

test:
	python -m unittest discover tests
.PHONY: test

lint:
	pylint *.py --ignore-patterns=test_.*?py,__init*
.PHONY: lint

# pip install pyuic5-tool
ui:
	python -m PyQt5.uic.pyuic ui/UIMainWindowForm.ui -o UIMainWindowForm.py
	pyrcc5 resources.qrc -o resources_rc.py
.PHONY: ui