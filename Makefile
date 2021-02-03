SHELL := /bin/bash

GIT_TAG = $(shell git describe --tags)

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
#--ignore-patterns set in .pylintrc
	pylint *.py

.PHONY: lint

# pip install pyuic5-tool
ui:
	python -m PyQt5.uic.pyuic ui/UIMainWindowForm.ui -o ui/UIMainWindowForm.py
	python -m PyQt5.uic.pyuic ui/UIProjectDlg.ui -o ui/UIProjectDlg.py
	python -m PyQt5.uic.pyuic ui/UISettingsDlg.ui -o ui/UISettingsDlg.py
	pyrcc5 resources.qrc -o resources_rc.py
.PHONY: ui

build:
	rm -rf ./build ./dist
	pyinstaller main.py --hidden-import hook-sqlalchemy.py -n SeismicFoldCalculation --windowed
	cd dist; \
	tar zcvf ../dist-out/SeismicFoldCalculation-"${GIT_TAG}".linux.tgz SeismicFoldCalculation/; \
	cd ..
	@echo "TAG: ${GIT_TAG}"
.PHONY: build