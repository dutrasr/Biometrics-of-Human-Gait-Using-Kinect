#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-08-20 04:41:29
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-16 15:50:15


import travelToDir as ttd
import formattingData as fd
import signalFilter as sf
import anthropometry as anth
import gaitAttributes as ga
import dataAnalysis as da
import saveData as sd

import numpy as np
import pickle
import sys


def main(arg=None):
	#files = {'testfiles': ['kinect2_5.csv']}
	files = ttd.getFiles('editedCollections/coletas')
	#print (files)
	# Organiza as capturas por ordem cronológica
	for i in files:
		files[i] = sorted(files[i])
	#print (files)

	for i in files.keys():
		print (len(files[i]))
		v = 'v2'
		folderanth = 'data/'+v+'/anthropometry/'
		folderaj = 'data/'+v+'/angles/'
		folderda = 'data/'+v+'/mean_std/'
		for k in range(len(files[i])):
			print (files[i][k])
			if '360' in files[i][k]:
				v = 'v1'
				folderanth = 'data/'+v+'/anthropometry/'
				folderaj = 'data/'+v+'/angles/'
				folderda = 'data/'+v+'/mean_std/'
			print (i+'/'+files[i][k])
			name = i.split('/')[-1]
			#print (name)

			# Format all raw data from kinect for better manipulation.
			# Ok!
			datafd, attribfd = fd.formatData(i+'/'+files[i][k], v)

			# Filters all raw data from kinect.
			# Ok!
			datafdFiltered, attribfdFiltered = sf.dataFilter(datafd, attribfd)

			# Generate the euclidian distance between all neighboors joints.
			# Ok!
			dataAnth, attribAnth = anth.generateAnthropometryData(datafd, v)

			# Generate all anthropometry info filtered.
			# Ok!
			dataAnthFiltered, attribAnthFiltered = anth.generateAnthropometryData(datafdFiltered, v)
			
			# Generate all gait attributes(angles) and spatiotemporal parameters.
			## Need some fix at line 42 Knee Ankle canculation.
			dataGaitAttrib, attribGaitAttrib = ga.generategaitAttributes(dataAnth, datafd)
			
			# Generate all gait attributes(angles) and spatiotemporal parameters filtered.
			## Need some fix at line 42 Knee Ankle canculation.
			dataGaitAttribFiltered, attribGaitAttribFiltered = ga.generategaitAttributes(dataAnthFiltered, datafdFiltered)


			### OOOOOOOOOk!!
			try:
				if 'anth' in arg:
					print ('Saving anthropometry data!!!')

					# Save anthropomtry between neightboors.
					sd.saveDataI(dataAnth, attribAnth, 'txt', name, k, folderanth+'notFiltered/txt/')
					sd.saveDataI(dataAnth, attribAnth, 'np', name, k, folderanth+'notFiltered/np/')

					# Save all anthropometry info between neighboors.
					sd.saveDataI(dataAnthFiltered, attribAnthFiltered, 'txt', name, k, folderanth+'filtered/txt/')
					sd.saveDataI(dataAnthFiltered, attribAnthFiltered, 'np', name, k, folderanth+'filtered/np/')
			except:
				raise
				pass

			### OK!!!!
			try:
				if 'gaitAttrib' in arg:
					print ('Saving gaitAttrib data!!')

					# Save angles info.
					sd.saveDataII(dataGaitAttrib, attribGaitAttrib, 'txt', name, k, folderaj+'notFiltered/txt/')
					sd.saveDataII(dataGaitAttrib, attribGaitAttrib, 'np', name, k, folderaj+'notFiltered/np/')
					
					# Save filtered angles info.
					sd.saveDataII(dataGaitAttribFiltered, attribGaitAttribFiltered, 'txt', name, k, folderaj+'filtered/txt/')
					sd.saveDataII(dataGaitAttribFiltered, attribGaitAttribFiltered, 'np', name, k, folderaj+'filtered/np/')
			except:
				raise
				pass

			### KIND OF OK!!!
			try:
				if 'meanStd' in arg:
					print ('Generating and saving all mean an standart desviation data!!')

					# Generate the mean and standart desviation in all anthropometry data and the filtered data.
					dataMeanStdAnth, attribMeanStdAnth = da.generateDataAnalysis(dataAnth, attribAnth, 'anth')
					dataMeanStdAnthFiltered, attribMeanStdAnthFiltered = da.generateDataAnalysis(dataAnthFiltered, attribAnth, 'anth')

					### Save mean and standart desviation data neighboors filtered and not filtered.
					sd.saveDataII(dataMeanStdAnth, attribMeanStdAnth, 'txt', name, k, folderda+'notFiltered/anthropometry/txt/')
					sd.saveDataII(dataMeanStdAnth, attribMeanStdAnth, 'np', name, k, folderda+'notFiltered/anthropometry/np/')

					sd.saveDataII(dataMeanStdAnthFiltered, attribMeanStdAnthFiltered, 'txt', name, k, folderda+'filtered/anthropometry/txt/')
					sd.saveDataII(dataMeanStdAnthFiltered, attribMeanStdAnthFiltered, 'np', name, k, folderda+'filtered/anthropometry/np/')
					##
					
					# Generate the mean and standart desviation from all Gait Attributes
					dataMeanStdGaitAttrib, attribMeanStdGaitAttrib = da.generateDataAnalysis(dataGaitAttrib, attribGaitAttrib, 'gaitAttrib')
					dataMeanStdGaitAttribFiltered, attribMeanStdGaitAttribFiltered = da.generateDataAnalysis(dataGaitAttribFiltered, attribGaitAttribFiltered, 'gaitAttrib')

					### Save mean and standart desviation info from all peaks and valleys of all angles.
					sd.saveDataII(dataMeanStdGaitAttrib, attribMeanStdGaitAttrib, 'txt', name, k, folderda+'notFiltered/gaitAttributes/txt/')
					sd.saveDataII(dataMeanStdGaitAttrib, attribMeanStdGaitAttrib, 'np', name, k, folderda+'notFiltered/gaitAttributes/np/')

					sd.saveDataII(dataMeanStdGaitAttribFiltered, attribMeanStdGaitAttribFiltered, 'txt', name, k, folderda+'filtered/gaitAttributes/txt/')
					sd.saveDataII(dataMeanStdGaitAttribFiltered, attribMeanStdGaitAttribFiltered, 'np', name, k, folderda+'filtered/gaitAttributes/np/')
					##
					

			except:
				raise
				pass

main(sys.argv)