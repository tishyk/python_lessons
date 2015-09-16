# -*- coding: utf-8 -*-
#c:\pyuic4 Mainwindow.ui>>main_window.py
from PyQt4 import QtGui,QtCore
from main_window import Ui_MainWindow
from get_device_id import *
from apk_instalation import *
from team_city_install import *
from Run_test import *
import urllib, random
from threading import Thread

thread.start_new_thread(os.popen,('adb devices',))
build_info = {}
# Set empty variables
current_date = time.strftime('%Y-%m-%d_%H-%M', time.localtime())
run_test_list,run_test =[],[]
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self,None)#, QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def set_device_info(self):
            for e,d in enumerate(device_info['model']):
                device_line = device_info['model'][e]+' ('+device_info['android_ver'][e]+'/'
                device_line = device_line+device_info['build_type'][e]+'/'+device_info['id'][e]+')'
                self.ui.cb_device.insertItem(e,device_line)
            self.ui.cb_device.insertItem(e+1,"All attached devices")
            #print device_info

        def set_build_type(self):
            try:
                for e,line in enumerate(open('config.ini','r').readlines()):
                    self.ui.cb_buildtype.insertItem(e,line.rstrip())
            except:
                self.ui.cb_buildtype.insertItem(0,"No config.ini file")

        set_build_type(self)
        set_device_info(self)
        try:
            self.tc_connection()
        except urllib2.URLError:
             self.ui.statusbar.showMessage('No Connection to TeamCity server!', 7000)
             local_dirs = glob.glob('.'+os.sep+'BuildsFromTC'+os.sep+'*')
             build_number_list =[line.split('_')[-1] for line in local_dirs]
             [self.ui.cb_number.insertItem(e,line) for e,line in enumerate(build_number_list)]

        QtCore.QObject.connect(self.ui.cb_buildtype, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.tc_connection)
        QtCore.QObject.connect(self.ui.btn_start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.install_main)
        QtCore.QObject.connect(self.ui.btn_clear_device, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_application)
        QtCore.QObject.connect(self.ui.btn_start_test, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_test)
        QtCore.QObject.connect(self.ui.btn_run_all, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_all_test)

    def device_id(self):
        for device_id in device_info['id']:
            if device_id in self.ui.cb_device.currentText():
                device_id = [device_id]
                break
            if 'All' in self.ui.cb_device.currentText():
                device_id = device_info['id']
            else:
                device_id = False
                continue
        return device_id

    def device_name(self):
        for device_id in device_info['id']:
            if device_id in self.ui.cb_device.currentText():
                device_id = [device_id]
                break
            if 'All' in self.ui.cb_device.currentText():
                device_id = device_info['id']
            else:
                device_id = False
                continue
        return device_id

    def tc_connection(self):
        global build_info
        self.ui.cb_number.clear()
        build_info = {'build_id':[],'buildNumber':[],'status':[],'branchId':[], 'href':[],'webUrl':[]}
        page = 'HTTPS://' + SERVER + '/teamCity/httpAuth/app/rest/builds/?locator=buildType:'
        page = page + str(self.ui.cb_buildtype.currentText()).rstrip()+'&count=200&start=0'
        page_xml = get_page_xml(page)
        page_parse(page_xml,build_info)
        [self.ui.cb_number.insertItem(e,line) for e,line in enumerate(build_info['buildNumber']) ]

    def check_new_tcbuild(self, old_build_number):
        new_build_number = get_artifacts(build_info)[1]
        if old_build_number != new_build_number:
            return str(new_build_number)
        else:
            return None

    def install_main(self, build_number = None):
        global dir_name
        thread_list=[]
        zip_name= 'temp.zip'
        device_id = self.device_id()
        if os.path.exists(os.path.abspath('.')+'\\BuildsFromTC'):
            os.popen('rmdir '+os.sep+'BuildsFromTC')

        if build_number == None:
            build_number = str(self.ui.cb_number.currentText())
        artifacts_info = get_artifacts(build_info,build_number) # TC link for downloading and build number
        
        if 'Release' in str(self.ui.cb_buildtype.currentText()):
            dir_name = './BuildsFromTC'+os.sep+'Release'+os.sep+str(self.ui.cb_number.currentText())
        else:
            dir_name = './BuildsFromTC'+os.sep+'Develop'+os.sep+str(self.ui.cb_number.currentText())
        urllib.urlretrieve(artifacts_info[0], zip_name)
        artifact_release(zip_name,dir_name)

        for device in device_id:
            device_name = device_info['model'][device_info['id'].index(device)]
            run_test = [device, dir_name[2:], build_number, device_name]
            if run_test not in run_test_list :
                run_test_list.append([device, dir_name[2:], build_number, device_name])

            thread_list.append(Thread(target=adb_install, args=(dir_name,device)))
        [tr.start() for tr in thread_list]
        [tr.join() for tr in thread_list]
        self.ui.statusbar.showMessage('Packages are installed!',45000)

    def clear_application(self):
        device_id = self.device_id()
        thread_list=[]
        for device in device_id:
            filter = 'com.samsung.'
            thread_list.append(Thread(target=delete_3d_party_apk, args=(device,filter)))
        [tread.start() for tread in thread_list]
        [tread.join() for tread in thread_list]
        self.ui.statusbar.showMessage('Start package un-installation! Filter '+filter, 45000)
        print 'Clear all data with '+filter

    def start_test(self):
        global run_test_list
        ch_state = self.ui.chbox_new_auto.checkState()
        try:
            testcount = int(self.ui.cb_random.currentText())
            print 'Test count for test is',testcount
        except ValueError:
            print 'Random Test count!'
            testcount = None
        i=0
        count = int(self.ui.cb_count.currentText())
        while i<count:
            print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
            print "    Run cycle {0} from {1} cycles. ".format(i,count)
            print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
            thread_list=[]
            if testcount is None:
                testcount = random.randint(200,300)
            seed = random.randint(1, 10000)
            for test in run_test_list:
                thread_list.append(Thread(target=start_run_test,
                                          args=(test[0],test[1],test[2],test[3],testcount,seed,ch_state)))
            [tr.start() for tr in thread_list]
            [tr.join() for tr in thread_list]
            i+=1

            if i<int(self.ui.cb_count.currentText()) and self.ui.chb_latest.checkState()==2:
                if self.check_new_tcbuild(test[2]) != None:
                    build_number = self.check_new_tcbuild(test[2])
                    run_test_list=[]
                    print "\n New build number was found and applied!"
                    self.install_main(build_number)

    def run_all_test(self):
        window.setHidden(True)
        self.install_main()
        self.start_test()
        window.setHidden(False)
        print("All test were finished!")
        self.ui.statusbar.showMessage('All test were finished!')


if __name__=='__main__':
    #thread.start_new(get_device_id, ())
    get_device_id()
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("main.png"))
    myClipBoard = QtGui.QApplication.clipboard()
    window = Main()
    window.show()
    sys.exit(app.exec_())
