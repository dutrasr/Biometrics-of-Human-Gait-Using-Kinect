#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-08-26 00:00:06
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-15 18:37:21

import pickle
import os

###################################################################################
# Aramazena as informações dos tamanhos das juntas (distancia euclidiana).
###################################################################################
def saveDataI(data, attrib, dataType, name, lap, folder):
		# Armazena as informações em um arquivo texto.
	if(dataType == 'txt'):
		def saveDataIntoFile():
			nonlocal data
			nonlocal attrib
			f = open(folder+name+'.txt', 'a')
			f.write(str(lap))
			f.write('\n')
			for i in attrib:
				f.write(str(i))
				for k in data[i][3]:
					f.write(',')
					f.write(str(k))
				f.write('\n')
			f.close()
	if(dataType == 'np'):
		def saveDataIntoFile():
			nonlocal data
			nonlocal attrib

			if not 'attrib.np' in os.listdir(folder):
				f = open(folder+'attrib.np', 'ab')
				pickle.dump(attrib, f)
				f.close()
			f = open(folder+name+'.np', 'ab')
			pickle.dump(data, f)
			f.close()

	saveDataIntoFile()

###################################################################################
###################################################################################


###################################################################################
# Armazena as informações dos do caminhar.
###################################################################################
def saveDataII(data, attrib, dataType, name, lap, folder):
	# Armazena as informações em um arquivo texto
	if(dataType == 'txt'):
		def saveDataIntoFile():
			nonlocal data
			nonlocal attrib
			f = open(folder+name+'.txt', 'a')
			f.write(str(lap))
			f.write('\n')
			for i in attrib:
				f.write(str(i))
				for k in data[i]:
					f.write(',')
					f.write(str(k))
				f.write('\n')
			f.close()

	# Armazena as informações na forma em que elas estão, isto é, numpy array-.
	if(dataType == 'np'):
		def saveDataIntoFile():
			nonlocal data
			nonlocal attrib

			if not 'attrib.np' in os.listdir(folder):
				f = open(folder+'attrib.np', 'ab')
				pickle.dump(attrib, f)
				f.close()
			f = open(folder+name+'.np', 'ab')
			pickle.dump(data, f)
			f.close()

	saveDataIntoFile()

###################################################################################
###################################################################################