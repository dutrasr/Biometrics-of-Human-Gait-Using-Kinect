#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-08-27 01:17:31
# @Last Modified by:   dutrasr
# @Last Modified time: 2015-09-20 22:13:08

#import modules
import os

###################################################################################
# Recebe um diretorio com as pastas contendo as coletas e retorna um dicionario com
# a chave representando a pasta e a lista representando os arquivos contidos nela
###################################################################################
def getFiles(CurrentDir):
	try:
		# Get all the folders on the current directory.
		dList = [os.path.join(CurrentDir, folders) for folders in os.listdir(CurrentDir)]
		#return dList
	except:
		print ("Something went wrong!!")
		return

	folderFiles = {}
	#print (folders)
	for i in dList:
		#aux =[]
		#print (i)
		#aux.append(os.listdir(i))
		folderFiles[i] = os.listdir(i)
	#print (folderFiles)
	return folderFiles

###################################################################################
###################################################################################