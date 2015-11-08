#! usr/bin/env
#! coding: utf-8

import os
import time


# write into report.txt file next headers:
# №~   ITEM     TYPE    CREATION TIME
#write into body info from list:
# 1 s.tischenko         <DIR>   'Tue Oct 27 21:57:22 2015'
# 2 Test_group3.docx    <File>  'Sat Oct 31 14:44:39 2015'

#How?
# get list of items in folder:  os.listdir('..') -> Ex. ['python_test1.png', 's.tischenko',...
# get item creation time: time.ctime(os.path.getctime('../python_test1.png'))
# check for item type -> os.path.isdir('../python_test1.png') -> True if directory (write <DIR>)
# else TYPE -> <File>


#**
# For strig formating use %
# "N%0.2i\t%.%is\t<%s>\t%s" % (lst.index(item)+1,max_name_lenmax_name_len,item,item_type,ctime"
