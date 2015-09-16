# -*- coding: utf-8 -*-
#c:\pyuic4 Mainwindow.ui>>main_window.py
from PyQt4 import QtGui,QtCore
from main_window import Ui_MainWindow
from head_parcing import *
from functools import wraps
import os,time,sys,subprocess

binary_size={}

linked_item = [['1','line_project'],
                    ['2','line_date'],
                    ['3','line_code'],
                    ['4','line_csc'],
                    ['5','line_modem'],
                    ['7','line_template'],
                    ['8','line_full'],
                    ['9','line_partial'],
                    ['10','line_approver'],
                    ['11','line_p4port'],
                    ['12','label_name'],
                    ['13','line_smd'],
                    ['14','line_smd_home'],
                    ['15','line_user'],
                    ['16','line_manager'] ]

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def left_click(func, parent):
    @wraps(func)
    def wrapper(evt):
        QtGui.QLabel.mousePressEvent(parent, evt)
        if evt.button() == QtCore.Qt.LeftButton:
            parent.emit(QtCore.SIGNAL('leftClicked()'))
        func(evt)
    return wrapper



class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self,None, QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.line_date.setText(str(symbol_date)+"R1")
        self.ui.line_info.installEventFilter(self)
        
        for n in range(1, 17):
            label = self.ui.__getattribute__('label_' + str(n))
            label.mousePressEvent = left_click(label.mousePressEvent, label)
            try:
                QtCore.QObject.connect(label, QtCore.SIGNAL('leftClicked()'), self.__getattribute__('link_activation_'+str(n)))
            except:
                print "Link not found at label position -",str(n)
            
        
        QtCore.QObject.connect(self.ui.line_info, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.info_changed )
        QtCore.QObject.connect(self.ui.btn_clean, QtCore.SIGNAL(_fromUtf8("clicked()")), self.list_clean )
        QtCore.QObject.connect(self.ui.btn_label, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_creation)
        QtCore.QObject.connect(self.ui.line_info, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.list_clean)
        QtCore.QObject.connect(self.ui.list_mail, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.mail_selection)
        QtCore.QObject.connect(self.ui.list_size, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.size_selection)
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.box_selection)
        
        
    activation=lambda self,x,y: self.link_activation(x,y)
    
    # shit code !!! be carefull!
    def link_activation_1(self):
        self.activation(linked_item[0][0],linked_item[0][1],) 
    def link_activation_2(self):
        self.activation(linked_item[1][0],linked_item[1][1],)
    def link_activation_3(self):
        self.activation(linked_item[2][0],linked_item[2][1],)    
    def link_activation_4(self):
        self.activation(linked_item[3][0],linked_item[3][1],)    
    def link_activation_5(self):
        self.activation(linked_item[4][0],linked_item[4][1],)    
    # def for 6 not supported! combo box!  
    def link_activation_7(self):
        self.activation(linked_item[5][0],linked_item[5][1],)    
    def link_activation_8(self):
        self.activation(linked_item[6][0],linked_item[6][1],)    
    def link_activation_9(self):
        self.activation(linked_item[7][0],linked_item[7][1],)    
    def link_activation_10(self):
        self.activation(linked_item[8][0],linked_item[8][1],)    
    def link_activation_11(self):
        self.activation(linked_item[9][0],linked_item[9][1],)    
    def link_activation_12(self):
        self.activation(linked_item[10][0],linked_item[10][1],)    
    def link_activation_13(self):
        self.activation(linked_item[11][0],linked_item[11][1],)
    def link_activation_14(self):
        self.activation(linked_item[12][0],linked_item[12][1],) 
    def link_activation_15(self):
        self.activation(linked_item[13][0],linked_item[13][1],) 
    def link_activation_16(self):
        self.activation(linked_item[14][0],linked_item[14][1],) 

        
    def link_activation(self,label,line):

        label = self.ui.__getattribute__('label_' + str(label))
        obj_text = self.ui.__getattribute__(line)
        
        print label.text(),label.objectName()

        try:
            item_text=str(obj_text.text())
        except:
            item_text=str(obj_text.toPlainText())
                
        myClipBoard.setText(_fromUtf8(item_text),QtGui.QClipboard.Clipboard)
        clipboard_text= myClipBoard.text("plain",QtGui.QClipboard.Selection)
        print 'copy',item_text
        self.ui.statusBar.showMessage('Successfully copied!',1000)


    def eventFilter(self, object, event):
        if (object is self.ui.line_info):
            if (event.type() == QtCore.QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()   # must accept the dragEnterEvent or else the dropEvent can't occur !!!
                    print "accept"
                else:
                    event.ignore()
                    print "ignore"
            if (event.type() == QtCore.QEvent.Drop):
                if event.mimeData().hasUrls():   # if file or link is dropped
                    urlcount = len(event.mimeData().urls())  # count number of drops
                    url_list = event.mimeData().urls()  #[0] get first url
                    for url in url_list:
                        try:
                            path=str(url.toString())[8:].decode(sys.getdefaultencoding())
                        except:
                            pass
                        try:    
                            size='{:,}'.format(os.path.getsize(path))
                            file_name=os.path.basename(path)
                            binary_size[file_name]=size
                            self.ui.list_size.addItem(file_name+" : "+size+" Bytes")
                                                    
                            print file_name+" : "+size+" Bytes"
                        except:
                            print "Drop file failed"

            return False # lets the event continue to the edit
        return False  

    def label_creation(self):
        from base64 import b16encode as e1, b32encode as e3, b64encode as e6
        open('temp.data','w').close()
        f=open('temp.data','a')
        try:
            child.kill(shell=None)
        except:
            print 'Child label not started!'
        
        save_to_file= (
               self.ui.line_project.text(),
               self.ui.line_code.text(),
               self.ui.line_csc.text(),
               self.ui.line_modem.text(),
               self.ui.line_template.text(),
               self.ui.line_full.text(),
               self.ui.line_partial.toPlainText() ,
               self.ui.line_approver.text(),
               self.ui.line_p4port.text(),
               self.ui.label_name.toPlainText(),
               str(self.ui.comboBox.currentText()),
               )
        
        [f.write(e1(e3(e6(str(line))))[::-1]+'\n') for line in save_to_file]
        f.close()
        try:
            child=subprocess.Popen('start main_label', shell=None) #for exe
            #child=subprocess.Popen('python main_label.py', shell=None)
        except:
           child= subprocess.Popen('main_label')
        '''   
        finally:
           child= subprocess.Popen('python main_label.py') '''
            
        print "Saved to file temp.data!"

    def box_selection(self):
        bin_type=str(self.ui.comboBox.currentText())
        try:
            self.ui.line_template.setText(p4[bin_type]["Path/Template"])
            self.ui.line_p4port.setText(p4[bin_type]["Server"])
            self.ui.line_full.setText(p4[bin_type]["Full"])
            self.ui.line_partial.setPlainText(p4[bin_type]["Partials"])
        except:
            print u"\nFail in Bin Type fields insert \n"
        print self.ui.comboBox.currentText()
        
        self.label_insert(project,model,info_text)
        
    def label_insert(self,project,model,info_text):
        
        bin_type=str(self.ui.comboBox.currentText()) #get current box str
        fget_label_new(info_text,model)                   # find labels in text
        for bins in p4["LABEL_MARK"]:
        
            # check label presence
            
            if model[:-2] in p4["LABEL"]:
                self.ui.label_name.setPlainText("\n".join(p4["LABEL"][bin_type]))
                
            if model not in p4["LABEL"][bin_type]:
                for bins in p4["LABEL_MARK"]:
                    if bin_type == bins:
                        for label_version in p4[bin_type]["VERSION"]:
                            lab=project+"_"+label_version+"_"+str(symbol_date)+"R1_"+bin_type+"_OFFICIAL"
                            if lab not in p4["LABEL"][bin_type]:
                                p4["LABEL"][bin_type].append(lab)
        # if
        self.ui.label_name.setPlainText("\n".join(p4["LABEL"][bin_type]))
        self.ui.comboBox.setFocus()
        
    def info_changed(self):
        global project,model,info_text
        p4["LABEL"]={"CODE":[],"CSC":[],"MODEM":[]}
        p4["LABEL_MARK"]=[]
        info_text=''
        for symbol in self.ui.line_info.text():
            try:
                info_text+=str(symbol).decode(sys.getdefaultencoding())
            except:
                pass
            
        fget_p4_path_port(info_text)
        fget_full_partials(info_text)
                
        if "Recipients\t" in info_text or "samsung.com" in info_text: # get id for mail list from parcing 
            for i in mail_list(info_text):   
                self.ui.list_mail.addItem(str(i))
                
        if "Project\t" in info_text or "SM-" in info_text or "GT-" in info_text: # get project name from parcing 
            project=fget_project(info_text)
            model=(project.split("_")[0]).split("-")[-1]
            print model
            self.ui.line_project.setText(project)
            
        if "Approval User\t" in info_text and ")" in info_text:
            info_approver=fget_approver(info_text)
            self.ui.line_user.setText(info_approver[0])
            self.ui.line_approver.setText(info_approver[1])
            
        if "Project Manager\t" in info_text and ")" in info_text:
            self.ui.line_manager.setText(fget_manager(info_text))
        
        if "Code Version" in info_text or "CSC Version" in info_text or "CP Version" in info_text:
            
            fget_versions(info_text)
            fversion_name_correction(model)
            fget_label_new(info_text, model)
            print p4["LABEL"]

            fmake_smd_name()
 
            self.ui.line_code.setText(", ".join(p4["CODE"]["VERSION"]))
            self.ui.line_csc.setText(", ".join(p4["CSC"]["VERSION"]))
            self.ui.line_modem.setText(", ".join(p4["MODEM"]["VERSION"]))
            
            self.ui.line_smd.setPlainText("\n".join(p4["SMD_NAME"]))
            self.ui.line_smd_home.setPlainText("\n".join(p4["SMD_NAME_HOME"]))

            
        self.box_selection()
        
        self.label_insert(project,model,info_text)
        
        #print p4
        self.ui.line_info.clear()
 
    def size_selection(self):
        if self.ui.list_size.currentItem().text()!="Select all":
            item_text=self.ui.list_size.currentItem().text()
            myClipBoard.setText(item_text,QtGui.QClipboard.Clipboard)
            clipboard_text= myClipBoard.text("plain",QtGui.QClipboard.Selection)
            print item_text
        else:        
            size_list=''
            for i in xrange(self.ui.list_size.count()):
                size_list+=self.ui.list_size.item(i).text()+"\n"
            size_list.replace("Select all\n",'')
            print size_list,"-"*60
            
            myClipBoard.setText(size_list,QtGui.QClipboard.Clipboard)
            clipboard_text= myClipBoard.text("plain",QtGui.QClipboard.Selection)
            print clipboard_text  
        
    def mail_selection(self):
        if self.ui.list_mail.currentItem().text()!="Select all":
            item_text=self.ui.list_mail.currentItem().text()
            myClipBoard.setText(item_text,QtGui.QClipboard.Clipboard)
            clipboard_text= myClipBoard.text("plain",QtGui.QClipboard.Selection)
            print item_text
        else:        
            mail_list=''
            for i in xrange(self.ui.list_mail.count()):
                mail_list+=self.ui.list_mail.item(i).text()+";"
            mail_list.replace("Select all;",'')
            print mail_list
            myClipBoard.setText(mail_list,QtGui.QClipboard.Clipboard)
            clipboard_text= myClipBoard.text("plain",QtGui.QClipboard.Selection)
            print clipboard_text        
      
    def list_clean(self):
        self.ui.list_mail.clear()
        self.ui.list_mail.addItem("Select all")
        self.ui.list_size.clear()
        self.ui.list_size.addItem("Select all") 
                     
                     
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("main.png"))
    myClipBoard = QtGui.QApplication.clipboard()
    window = Main()
    window.show()
    sys.exit(app.exec_())
