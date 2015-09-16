# -*- coding: utf-8 -*-

#c:\pyuic4 Label_main_window.ui>>label_window.py
import os, re, time, sys, subprocess
from PyQt4 import QtGui,QtCore
from label_window import Ui_LabelWindow

from base64 import b16encode as e1, b32encode as e3, b64encode as e6
from magic import _

try:
    f=open('temp.data','r').readlines()
    data = [_(line[:-1]) for line in f]
    #print data
except:
    pass

try:
    config_ini=open('config.ini','a+').read()
    print 'read config.ini...'
    release_user=re.findall('release_user.*',config_ini)[0].split(':')[1]
    print release_user
except:
    pass


class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self,None, QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_LabelWindow()
        self.ui.setupUi(self)
        self.set_items()
        
        QtCore.QObject.connect(self.ui.btn_label, QtCore.SIGNAL("clicked()"), self.call_labeling )
        QtCore.QObject.connect(self.ui.line_label, QtCore.SIGNAL("textChanged()"), self.box_name)
        
    def box_name(self):
        self.ui.groupBox_label.setTitle(self.ui.line_label.toPlainText())
     
    def set_items(self):
        if len(data)>3:
            try:
                self.ui.line_user.setText(release_user)
            except:
                pass
            
            self.ui.line_model.setText(data[0])
            self.ui.line_code.setText(data[1])
            self.ui.line_csc.setText(data[2])
            self.ui.line_modem.setText(data[3])
            self.ui.line_template.setText(data[4])
            self.ui.line_cl_full.setText(data[5])
            self.ui.line_cl_partials.setPlainText(data[6])
            self.ui.line_pl.setText(data[7])
            self.ui.line_port.setText(data[8])
            self.ui.line_label.setPlainText(data[9].split('OFFICIAL')[0]+'OFFICIAL')
            self.ui.groupBox_label.setTitle(self.ui.line_label.toPlainText())
            
            if '_CODE' in data[9] or '_AP' in data[9]:
                self.ui.line_version.setText(data[1])
            if '_CSC' in data[9]:
                self.ui.line_version.setText(data[2])
            if '_MODEM' in data[9] or '_CP' in data[9]:
                self.ui.line_version.setText(data[3])
                
    
           
    def call_labeling(self):
        print "Start Labeling!"
        open('temp.data','w').write('')
        f=open('temp.data','a')
        try:
            if not os.path.exists('Log'): os.makedirs('Log')
        except:
            print "Can't create Folder Log!"
            pass

        save_to_file= (
               self.ui.line_user.text(),
               self.ui.line_password.text(),
               self.ui.line_port.text(),
               self.ui.line_template.text(),
               self.ui.line_label.toPlainText(),
               
               self.ui.line_model.text(),
               self.ui.line_pl.text(),
               self.ui.line_devgroup.text(),
               self.ui.line_step.text(),
               self.ui.line_version.text(),
               self.ui.line_cl_full.text(),
               self.ui.line_cl_partials.toPlainText(),
               
               self.ui.line_code.text(),
               self.ui.line_csc.text(),
               self.ui.line_modem.text(),
               self.ui.line_comment.toPlainText() )
        
        [f.write(e1(e3(e6(str(line))))[::-1]+'\n') for line in save_to_file]
        f.close()
        
        try:
            child=subprocess.Popen('labeling', shell=None, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        except:
            child=subprocess.Popen('python labeling.py', shell=None,stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            
        window.hide()
        text=child.stdout.read()
        text_err=child.stderr.read()
        print text_err
        
        log_name=str(self.ui.line_label.toPlainText())+'_labeling_log.txt'
        f=open('Log\\'+log_name,'w')
        f.write(text+text_err)
        f.close()
        child.kill()
        
        child=subprocess.Popen('notepad '+'Log\\'+log_name, shell=None)
        print "Main Done!"
        window.close()


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myClipBoard = QtGui.QApplication.clipboard()
    window = Main()
    window.show()
    sys.exit(app.exec_())

