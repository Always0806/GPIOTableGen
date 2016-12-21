# encoding: utf-8
import sys
import os
import signal
import shutil
import Util
from Util import FindBallNameAppend,FindPositionAppend,PrintItemList

def CSAParsing(foldername):
	for root, dir, files in os.walk(foldername):#search all file in folder
		for file in files:
			file = foldername+'/'+file 
			#print(file)
			
			pre_line = ''
			fo = open(file, "r")
			
			for line in open(file): 
				#####find the ball name
				line = fo.readline()
				index = line.find("$PN")
				if index != -1:# fine $PN
					BallName = line[index+4:].strip()# Get Ball Name
					start_tag = line.find("(")
					end_tag = line.find(")")
					if start_tag != -1 and end_tag!= -1:# fine ()
						position = line[start_tag:end_tag+1].strip()
						FindBallNameAppend(BallName,position)
						#print (BallName + "  " + position)
			fo.close()
			
			for line in open(file): 
				#####find the SIG_NAME
				index = line.find("SIG_NAME")
				if index != -1:# fine SIG_NAME
					SIG_NAME = line[index+9:].strip()
					end_tag = pre_line.find(")")
					if end_tag!= -1:# fine )
						start_tag = pre_line.find("(",end_tag+1)
						end_tag = pre_line.find(")",end_tag+1)
						position = pre_line[start_tag:end_tag+1].strip()
						FindPositionAppend(position,SIG_NAME)
						#print (SIG_NAME + "  " + position)
				
				pre_line = line
			fo.close()
