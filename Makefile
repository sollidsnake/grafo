uis/uiMainwindow.py : uis/mainwindow.ui
	pyuic4 uis/mainwindow.ui -o uis/uiMainwindow.py

uis/uiResultado.py : uis/resultado.ui
	pyuic4 uis/resultado.ui -o uis/uiResultado.py

uis/uiAbout.py : uis/about.ui
	pyuic4 uis/about.ui -o uis/uiAbout.py
