# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UiProjectDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProjectDlg(object):
    def setupUi(self, ProjectDlg):
        ProjectDlg.setObjectName("ProjectDlg")
        ProjectDlg.resize(795, 474)
        ProjectDlg.setMinimumSize(QtCore.QSize(795, 474))
        ProjectDlg.setMaximumSize(QtCore.QSize(795, 474))
        self.project = QtWidgets.QGroupBox(ProjectDlg)
        self.project.setGeometry(QtCore.QRect(10, 70, 771, 331))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.project.setFont(font)
        self.project.setTitle("")
        self.project.setObjectName("project")
        self.gridLayoutWidget = QtWidgets.QWidget(self.project)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 751, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.grid_file = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_file.setFrameShape(QtWidgets.QFrame.Box)
        self.grid_file.setText("")
        self.grid_file.setObjectName("grid_file")
        self.gridLayout.addWidget(self.grid_file, 1, 3, 1, 1)
        self.rps_file_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rps_file_btn.setObjectName("rps_file_btn")
        self.gridLayout.addWidget(self.rps_file_btn, 3, 0, 1, 1)
        self.db_url = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.db_url.setObjectName("db_url")
        self.gridLayout.addWidget(self.db_url, 0, 3, 1, 1)
        self.verbose = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.verbose.setText("")
        self.verbose.setObjectName("verbose")
        self.gridLayout.addWidget(self.verbose, 5, 3, 1, 1)
        self.db_verbose = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.db_verbose.setText("")
        self.db_verbose.setObjectName("db_verbose")
        self.gridLayout.addWidget(self.db_verbose, 6, 3, 1, 1)
        self.xps_file_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.xps_file_btn.setObjectName("xps_file_btn")
        self.gridLayout.addWidget(self.xps_file_btn, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.grid_file_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.grid_file_btn.setObjectName("grid_file_btn")
        self.gridLayout.addWidget(self.grid_file_btn, 1, 0, 1, 1)
        self.sps_file_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sps_file_btn.setObjectName("sps_file_btn")
        self.gridLayout.addWidget(self.sps_file_btn, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.sps_file = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sps_file.setFrameShape(QtWidgets.QFrame.Box)
        self.sps_file.setText("")
        self.sps_file.setWordWrap(True)
        self.sps_file.setObjectName("sps_file")
        self.gridLayout.addWidget(self.sps_file, 2, 3, 1, 1)
        self.rps_file = QtWidgets.QLabel(self.gridLayoutWidget)
        self.rps_file.setFrameShape(QtWidgets.QFrame.Box)
        self.rps_file.setText("")
        self.rps_file.setObjectName("rps_file")
        self.gridLayout.addWidget(self.rps_file, 3, 3, 1, 1)
        self.xps_file = QtWidgets.QLabel(self.gridLayoutWidget)
        self.xps_file.setFrameShape(QtWidgets.QFrame.Box)
        self.xps_file.setText("")
        self.xps_file.setObjectName("xps_file")
        self.gridLayout.addWidget(self.xps_file, 4, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(ProjectDlg)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(19, 10, 751, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.new_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sfc-ui/ui/icons/folder--plus-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_btn.setIcon(icon)
        self.new_btn.setIconSize(QtCore.QSize(24, 24))
        self.new_btn.setObjectName("new_btn")
        self.gridLayout_2.addWidget(self.new_btn, 0, 1, 1, 1)
        self.save_as_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sfc-ui/ui/icons/disk-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_as_btn.setIcon(icon1)
        self.save_as_btn.setIconSize(QtCore.QSize(24, 24))
        self.save_as_btn.setObjectName("save_as_btn")
        self.gridLayout_2.addWidget(self.save_as_btn, 0, 7, 1, 1)
        self.open_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sfc-ui/ui/icons/folder-open-document-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon2)
        self.open_btn.setIconSize(QtCore.QSize(24, 24))
        self.open_btn.setObjectName("open_btn")
        self.gridLayout_2.addWidget(self.open_btn, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 6, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QtCore.QSize(24, 24))
        self.save_btn.setObjectName("save_btn")
        self.gridLayout_2.addWidget(self.save_btn, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 4, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ProjectDlg)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 410, 771, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.close_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/sfc-ui/ui/icons/cross-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QtCore.QSize(24, 24))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)

        self.retranslateUi(ProjectDlg)
        self.close_btn.clicked.connect(ProjectDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(ProjectDlg)

    def retranslateUi(self, ProjectDlg):
        _translate = QtCore.QCoreApplication.translate
        ProjectDlg.setWindowTitle(_translate("ProjectDlg", "Dialog"))
        self.label.setText(_translate("ProjectDlg", "DB URL"))
        self.rps_file_btn.setText(_translate("ProjectDlg", "RPS file"))
        self.xps_file_btn.setText(_translate("ProjectDlg", "XPS file"))
        self.label_6.setText(_translate("ProjectDlg", "Verbose"))
        self.grid_file_btn.setText(_translate("ProjectDlg", "Grid file"))
        self.sps_file_btn.setText(_translate("ProjectDlg", "SPS file"))
        self.label_7.setText(_translate("ProjectDlg", "DB verbose"))
        self.new_btn.setText(_translate("ProjectDlg", "New"))
        self.save_as_btn.setText(_translate("ProjectDlg", "Save As"))
        self.open_btn.setText(_translate("ProjectDlg", "Open"))
        self.save_btn.setText(_translate("ProjectDlg", "Save"))
        self.close_btn.setText(_translate("ProjectDlg", "Close"))
import resources_rc
