# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Label_main_window.ui'
#
# Created: Wed Oct 08 13:43:36 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LabelWindow(object):
    def setupUi(self, LabelWindow):
        LabelWindow.setObjectName(_fromUtf8("LabelWindow"))
        LabelWindow.resize(446, 479)
        LabelWindow.setToolTip(_fromUtf8(""))
        LabelWindow.setStyleSheet(_fromUtf8("background-color: rgb(229, 229, 229);"))
        LabelWindow.setIconSize(QtCore.QSize(24, 24))
        LabelWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        LabelWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(LabelWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 451))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 638))
        self.centralwidget.setStyleSheet(_fromUtf8("background-color:rgb(227, 227, 227);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 632))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(237, 245, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(2, 5, 2, 2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_description = QtGui.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_description.setFont(font)
        self.groupBox_description.setStyleSheet(_fromUtf8("background-color: rgb(237, 245, 255);"))
        self.groupBox_description.setFlat(False)
        self.groupBox_description.setCheckable(False)
        self.groupBox_description.setObjectName(_fromUtf8("groupBox_description"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_description)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.line_model = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_model.sizePolicy().hasHeightForWidth())
        self.line_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_model.setFont(font)
        self.line_model.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_model.setText(_fromUtf8(""))
        self.line_model.setObjectName(_fromUtf8("line_model"))
        self.gridLayout_3.addWidget(self.line_model, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_6.setFrameShadow(QtGui.QFrame.Raised)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.line_pl = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_pl.sizePolicy().hasHeightForWidth())
        self.line_pl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_pl.setFont(font)
        self.line_pl.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_pl.setText(_fromUtf8(""))
        self.line_pl.setObjectName(_fromUtf8("line_pl"))
        self.gridLayout_3.addWidget(self.line_pl, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(False)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_7.setFrameShadow(QtGui.QFrame.Raised)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.line_devgroup = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_devgroup.sizePolicy().hasHeightForWidth())
        self.line_devgroup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_devgroup.setFont(font)
        self.line_devgroup.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_devgroup.setText(_fromUtf8(""))
        self.line_devgroup.setReadOnly(False)
        self.line_devgroup.setObjectName(_fromUtf8("line_devgroup"))
        self.gridLayout_3.addWidget(self.line_devgroup, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(False)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_8.setFrameShadow(QtGui.QFrame.Raised)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.line_step = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_step.sizePolicy().hasHeightForWidth())
        self.line_step.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_step.setFont(font)
        self.line_step.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_step.setText(_fromUtf8(""))
        self.line_step.setObjectName(_fromUtf8("line_step"))
        self.gridLayout_3.addWidget(self.line_step, 3, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(False)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_10.setFrameShadow(QtGui.QFrame.Raised)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.line_cl_full = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_cl_full.sizePolicy().hasHeightForWidth())
        self.line_cl_full.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_cl_full.setFont(font)
        self.line_cl_full.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_cl_full.setText(_fromUtf8(""))
        self.line_cl_full.setObjectName(_fromUtf8("line_cl_full"))
        self.gridLayout_3.addWidget(self.line_cl_full, 4, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(False)
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_11.setFrameShadow(QtGui.QFrame.Raised)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(False)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_9.setFrameShadow(QtGui.QFrame.Raised)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 6, 0, 1, 1)
        self.line_version = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_version.sizePolicy().hasHeightForWidth())
        self.line_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_version.setFont(font)
        self.line_version.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_version.setText(_fromUtf8(""))
        self.line_version.setObjectName(_fromUtf8("line_version"))
        self.gridLayout_3.addWidget(self.line_version, 6, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setMouseTracking(False)
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_12.setFrameShadow(QtGui.QFrame.Raised)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 7, 0, 1, 1)
        self.line_code = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_code.sizePolicy().hasHeightForWidth())
        self.line_code.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_code.setFont(font)
        self.line_code.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_code.setText(_fromUtf8(""))
        self.line_code.setObjectName(_fromUtf8("line_code"))
        self.gridLayout_3.addWidget(self.line_code, 7, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setMouseTracking(False)
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_13.setFrameShadow(QtGui.QFrame.Raised)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 8, 0, 1, 1)
        self.line_csc = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_csc.sizePolicy().hasHeightForWidth())
        self.line_csc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_csc.setFont(font)
        self.line_csc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_csc.setText(_fromUtf8(""))
        self.line_csc.setObjectName(_fromUtf8("line_csc"))
        self.gridLayout_3.addWidget(self.line_csc, 8, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setMouseTracking(False)
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_14.setFrameShadow(QtGui.QFrame.Raised)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 9, 0, 1, 1)
        self.line_modem = QtGui.QLineEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_modem.sizePolicy().hasHeightForWidth())
        self.line_modem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_modem.setFont(font)
        self.line_modem.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_modem.setText(_fromUtf8(""))
        self.line_modem.setObjectName(_fromUtf8("line_modem"))
        self.gridLayout_3.addWidget(self.line_modem, 9, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setMouseTracking(False)
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_15.setFrameShadow(QtGui.QFrame.Raised)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 10, 0, 1, 1)
        self.line_comment = QtGui.QPlainTextEdit(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_comment.sizePolicy().hasHeightForWidth())
        self.line_comment.setSizePolicy(sizePolicy)
        self.line_comment.setMinimumSize(QtCore.QSize(0, 32))
        self.line_comment.setMaximumSize(QtCore.QSize(16777215, 80))
        self.line_comment.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_comment.setFont(font)
        self.line_comment.setAutoFillBackground(False)
        self.line_comment.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_comment.setFrameShape(QtGui.QFrame.NoFrame)
        self.line_comment.setFrameShadow(QtGui.QFrame.Plain)
        self.line_comment.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.line_comment.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.line_comment.setPlainText(_fromUtf8(""))
        self.line_comment.setObjectName(_fromUtf8("line_comment"))
        self.gridLayout_3.addWidget(self.line_comment, 10, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_description)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_5.setFrameShadow(QtGui.QFrame.Raised)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.line_cl_partials = QtGui.QPlainTextEdit(self.groupBox_description)
        self.line_cl_partials.setMinimumSize(QtCore.QSize(0, 19))
        self.line_cl_partials.setMaximumSize(QtCore.QSize(16777215, 174))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_cl_partials.setFont(font)
        self.line_cl_partials.setAutoFillBackground(False)
        self.line_cl_partials.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_cl_partials.setFrameShape(QtGui.QFrame.NoFrame)
        self.line_cl_partials.setFrameShadow(QtGui.QFrame.Plain)
        self.line_cl_partials.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.line_cl_partials.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.line_cl_partials.setPlainText(_fromUtf8(""))
        self.line_cl_partials.setObjectName(_fromUtf8("line_cl_partials"))
        self.gridLayout_3.addWidget(self.line_cl_partials, 5, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_description, 4, 0, 1, 4)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 4)
        self.btn_label = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_label.sizePolicy().hasHeightForWidth())
        self.btn_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_label.setFont(font)
        self.btn_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 143);"))
        self.btn_label.setObjectName(_fromUtf8("btn_label"))
        self.gridLayout_2.addWidget(self.btn_label, 1, 1, 1, 2)
        self.groupBox_label = QtGui.QGroupBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_label.sizePolicy().hasHeightForWidth())
        self.groupBox_label.setSizePolicy(sizePolicy)
        self.groupBox_label.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_label.setFont(font)
        self.groupBox_label.setStyleSheet(_fromUtf8("background-color: rgb(237, 245, 255);"))
        self.groupBox_label.setObjectName(_fromUtf8("groupBox_label"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_label)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_label)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_2.setFrameShadow(QtGui.QFrame.Raised)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 3, 1, 1)
        self.line_password = QtGui.QLineEdit(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_password.sizePolicy().hasHeightForWidth())
        self.line_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_password.setText(_fromUtf8(""))
        self.line_password.setEchoMode(QtGui.QLineEdit.Password)
        self.line_password.setObjectName(_fromUtf8("line_password"))
        self.gridLayout_4.addWidget(self.line_password, 0, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_label)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_4.setFrameShadow(QtGui.QFrame.Raised)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 5, 1, 1)
        self.line_port = QtGui.QLineEdit(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_port.sizePolicy().hasHeightForWidth())
        self.line_port.setSizePolicy(sizePolicy)
        self.line_port.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_port.setFont(font)
        self.line_port.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_port.setText(_fromUtf8(""))
        self.line_port.setObjectName(_fromUtf8("line_port"))
        self.gridLayout_4.addWidget(self.line_port, 0, 6, 1, 1)
        self.line_2 = QtGui.QFrame(self.groupBox_label)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 7)
        self.label_17 = QtGui.QLabel(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setMouseTracking(False)
        self.label_17.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_17.setFrameShadow(QtGui.QFrame.Raised)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setMouseTracking(False)
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(0, 0, 76);\n"
"background-color: rgb(237, 245, 255);"))
        self.label_16.setFrameShadow(QtGui.QFrame.Raised)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_4.addWidget(self.label_16, 3, 0, 1, 1)
        self.line_label = QtGui.QPlainTextEdit(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_label.sizePolicy().hasHeightForWidth())
        self.line_label.setSizePolicy(sizePolicy)
        self.line_label.setMinimumSize(QtCore.QSize(0, 18))
        self.line_label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_label.setFont(font)
        self.line_label.setAutoFillBackground(False)
        self.line_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.line_label.setFrameShadow(QtGui.QFrame.Plain)
        self.line_label.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.line_label.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.line_label.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.line_label.setPlainText(_fromUtf8(""))
        self.line_label.setObjectName(_fromUtf8("line_label"))
        self.gridLayout_4.addWidget(self.line_label, 3, 1, 1, 6)
        self.line_template = QtGui.QLineEdit(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_template.sizePolicy().hasHeightForWidth())
        self.line_template.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_template.setFont(font)
        self.line_template.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_template.setText(_fromUtf8(""))
        self.line_template.setObjectName(_fromUtf8("line_template"))
        self.gridLayout_4.addWidget(self.line_template, 2, 1, 1, 6)
        self.line_user = QtGui.QLineEdit(self.groupBox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_user.sizePolicy().hasHeightForWidth())
        self.line_user.setSizePolicy(sizePolicy)
        self.line_user.setMaximumSize(QtCore.QSize(160, 16777215))
        self.line_user.setBaseSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_user.setFont(font)
        self.line_user.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 76)"))
        self.line_user.setText(_fromUtf8(""))
        self.line_user.setObjectName(_fromUtf8("line_user"))
        self.gridLayout_4.addWidget(self.line_user, 0, 1, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_label, 0, 0, 1, 4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        LabelWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LabelWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 16))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LabelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LabelWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelWindow)
        LabelWindow.setTabOrder(self.line_user, self.line_password)
        LabelWindow.setTabOrder(self.line_password, self.line_port)
        LabelWindow.setTabOrder(self.line_port, self.line_template)
        LabelWindow.setTabOrder(self.line_template, self.line_label)
        LabelWindow.setTabOrder(self.line_label, self.btn_label)
        LabelWindow.setTabOrder(self.btn_label, self.line_model)
        LabelWindow.setTabOrder(self.line_model, self.line_pl)
        LabelWindow.setTabOrder(self.line_pl, self.line_devgroup)
        LabelWindow.setTabOrder(self.line_devgroup, self.line_step)
        LabelWindow.setTabOrder(self.line_step, self.line_cl_full)
        LabelWindow.setTabOrder(self.line_cl_full, self.line_cl_partials)
        LabelWindow.setTabOrder(self.line_cl_partials, self.line_version)
        LabelWindow.setTabOrder(self.line_version, self.line_code)
        LabelWindow.setTabOrder(self.line_code, self.line_csc)
        LabelWindow.setTabOrder(self.line_csc, self.line_modem)
        LabelWindow.setTabOrder(self.line_modem, self.line_comment)

    def retranslateUi(self, LabelWindow):
        LabelWindow.setWindowTitle(_translate("LabelWindow", "Labeling tool for RT Help Box v1.0", None))
        self.groupBox_description.setTitle(_translate("LabelWindow", "Description", None))
        self.label_6.setText(_translate("LabelWindow", "[SW PL]", None))
        self.label_7.setText(_translate("LabelWindow", "[DEV_GROUP]", None))
        self.label_8.setText(_translate("LabelWindow", "[STEP]", None))
        self.label_10.setText(_translate("LabelWindow", "[BASE CL]", None))
        self.label_11.setText(_translate("LabelWindow", "[ADD CL]", None))
        self.label_9.setText(_translate("LabelWindow", "[VERSION]", None))
        self.label_12.setText(_translate("LabelWindow", "[Code]", None))
        self.label_13.setText(_translate("LabelWindow", "[CSC]", None))
        self.label_14.setText(_translate("LabelWindow", "[Modem]", None))
        self.label_15.setText(_translate("LabelWindow", "[Comment] ", None))
        self.label_5.setText(_translate("LabelWindow", "[Model]", None))
        self.btn_label.setText(_translate("LabelWindow", "Create Label on P4", None))
        self.groupBox_label.setTitle(_translate("LabelWindow", "LABEL NAME", None))
        self.label_2.setText(_translate("LabelWindow", "P4 user", None))
        self.label_3.setText(_translate("LabelWindow", "P4 Password", None))
        self.label_4.setText(_translate("LabelWindow", "P4 port", None))
        self.label_17.setText(_translate("LabelWindow", "Template", None))
        self.label_16.setText(_translate("LabelWindow", "Label", None))

