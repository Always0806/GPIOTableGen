# encoding: utf-8
import sys
import os
import signal
import shutil
import math
import Util
from Util import xstr

MAX_TABS=9
TAB=4
def GetTABS(NetName):
	tab_str=''
	str_tabs = len(xstr(NetName))/TAB
	left_tabs = math.ceil(MAX_TABS-str_tabs)
	#print (xstr(NetName)+"   "+str(str_tabs)+"   "+str(left_tabs))
	for i in range(left_tabs):
		tab_str=tab_str+"\t"
	return tab_str

def GenMapHeaderFile():
	f = open('GPIOMAP.h', 'w')

	f.write("#ifndef I_GPIODEF_H_\n")
	f.write("#define I_GPIODEF_H_\n\n")

	i = 0
	for item in Util.ItemList:
		f.write("#define "+xstr(item.NetName)+GetTABS(item.NetName)+xstr(item.GPIO)+"\n")
		i=i+1
		if i%8==0:
			f.write("\n")
	
	f.write("\n#endif\n")
	f.close()