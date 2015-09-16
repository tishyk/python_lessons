# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

Mydata_files = [('config.ini','login.data', ["smd_.ico",'config.ini','login.data',])]
#build_exe_options = {"optimize": 1,"icon" : 'smd.ico'}
#base = "Win32GUI"

'''
setup(
        name="TC",
        console=[{"script":"team_city_install_x32_Feed.py",}],
        #data_files = Mydata_files,
        options={"py2exe":{"ascii":0,"bundle_files": 1,"compressed": True, "optimize": 1,"includes":["time",'sip','magic','get_device_id','apk_instalation'],"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],}},
	zipfile=None,
        )

setup(
        name="TC",
        console=[{"script":"team_city_size_x32.py",}],
        #data_files = Mydata_files,
        options={"py2exe":{"ascii":0,"bundle_files": 1,"compressed": True, "optimize": 1,"includes":["time",'sip','magic'],"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],}},
	zipfile=None,
        )


'''

setup(
        name="RT",
        console=[{"script":"main.py", 'icon_resources': [ (1, 'python3x.ico'),]}],
        #data_files = Mydata_files,
        options={"py2exe":{"ascii":0,"bundle_files": 1,"compressed": True, "optimize": 1,"includes":["time",'sip'],"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],}},
	zipfile=None,
        )

'''
setup(
        name="RT_label",
        windows=[{"script":"main_label.py", 'icon_resources': [ (1, 'smd_.ico'),]}],
        #data_files = Mydata_files,
        options={"py2exe":{"ascii":0,"bundle_files": 1,"compressed": True, "optimize": 1,"includes":['sip','magic'],"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],}},
	zipfile=None,)

setup(
        name="RT",
        console=[{"script":"labeling.py",}],
        #data_files = Mydata_files,
        options={"py2exe":{"ascii":0,"bundle_files": 1,"compressed": True, "optimize": 1,"includes":["time",'sip'],"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],}},
	zipfile=None,
        )

Py2exe extends Distutils setup keywords
In addition to the standard distutils setup keywords, the following py2exe keywords specify what and how to build. 

keyword 
 description 
 
console 
 list of scripts to convert into console exes 
 
windows 
 list of scripts to convert into GUI exes 
 
service 
 list of module names containing win32 service classes 
 
com_server 
 list of module names containing com server classes 
 
ctypes_com_server 
 list of module names containing com server classes 
 
zipfile 
 name of shared zipfile to generate; may specify a subdirectory; defaults to 'library.zip'. If zipfile is set to None, the files will be bundled within the executable instead of 'library.zip'. 
 
options 
 dictionary { "py2exe": { "opt1": val1, "opt2": val2, ... } } 
 


The options dictionary of py2exe
The option keyword takes the following set of dictionary key: value pairs. The dictionary "key" names and the "value" types are listed in the table below. 

key 
 value 
 
unbuffered 
 if true, use unbuffered binary stdout and stderr 
 
optimize 
 string or int of optimization level (0, 1, or 2) 0 = don’t optimize (generate .pyc) 1 = normal optimization (like python -O) 2 = extra optimization (like python -OO) See http://docs.python.org/distutils/apiref.html#module-distutils.util for more info. 
 
includes 
 list of module names to include 
 
packages 
 list of packages to include with subpackages 
 
ignores 
 list of modules to ignore if they are not found 
 
excludes 
 list of module names to exclude 
 
dll_excludes 
 list of dlls to exclude 
 
dist_dir 
 directory in which to build the final files 
 
typelibs 
 list of gen_py generated typelibs to include 
 
compressed 
 (boolean) create a compressed zipfile 
 
xref 
 (boolean) create and show a module cross reference 
 
bundle_files 
 bundle dlls in the zipfile or the exe. Valid values for bundle_files are: 3 = don't bundle (default) 2 = bundle everything but the Python interpreter 1 = bundle everything, including the Python interpreter 
 
skip_archive 
 (boolean) do not place Python bytecode files in an archive, put them directly in the file system 
 
ascii 
 (boolean) do not automatically include encodings and codecs 
 
custom-boot-script 
 Python file that will be run when setting up the runtime environment 
 

Example: 


setup(
        windows=['trypyglet.py'],
        options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
                }
        }
)

'''
