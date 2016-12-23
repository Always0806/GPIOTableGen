# encoding: utf-8
import sys
import os
import signal
import shutil
from Util import ExcelToStruct,StructToExcel,CheckEmptyNetName
from CSAParsing import CSAParsing
from MapGen import GenMapHeaderFile

def ShowArgument():
	print("GPIO table generate from CSA file write by Always")
	return 
	
ShowArgument()

#template='AST2500.xlsx'
#CSAfolder='CSA'
if sys.version_info < (3,):
	template = raw_input("Enter chipset template : ");
else:
	template = input("Enter chipset template : ");
	
if sys.version_info < (3,):
	CSAfolder = raw_input("Enter CSA file folder : ");
else:
	CSAfolder = input("Enter CSA file folder : ");
	
ExcelToStruct(template)
CSAParsing(CSAfolder)
CheckEmptyNetName()
StructToExcel(template)
GenMapHeaderFile()