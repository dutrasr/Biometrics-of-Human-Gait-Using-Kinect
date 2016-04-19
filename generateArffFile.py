#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutra
# @Date:   2015-10-30 04:53:35
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-18 00:40:35

import os
import pickle
import sys
import random
import arff

####################################################################################
# Gera uma lista com os atributos que vão ser utilizados no KNN:
# allData: Todos os atributos;
# leftSide: Apenas atributos do lado esquerdo;
# rightSide: Apenas atributos do lado direito.
#
# ***Gerar novos conjuntos de atributos mais especificos.***
####################################################################################
def attribAnth(arg_):
	attribAnthv1All = [
			'Height',
			'Head_ShoulderCenter',
			'ShoulderCenter_ShoulderRight',
			'ShoulderRight_ElbowRight',
			'ElbowRight_WristRight',
			'WristRight_HandRight',
			'ShoulderCenter_ShoulderLeft',
			'ShoulderLeft_ElbowLeft',
			'ElbowLeft_WristLeft',
			'WristLeft_HandLeft',
			'ShoulderCenter_Spine',
			'Spine_HipCenter',
			'HipCenter_HipRight',
			'HipRight_KneeRight',
			'KneeRight_AnkleRight',
			'AnkleRight_FootRight',
			'HipCenter_HipLeft',
			'HipLeft_KneeLeft',
			'KneeLeft_AnkleLeft',
			'AnkleLeft_FootLeft'
			]

	attribAnthv2All = [
			'Height',
			'Head_Neck',
			'Neck_SpineShoulder',
			'SpineShoulder_ShoulderRight',
			'ShoulderRight_ElbowRight',
			'ElbowRight_WristRight',
			'WristRight_ThumbRight',
			'WristRight_HandRight',
			'HandRight_HandTipRight',
			'SpineShoulder_ShoulderLeft',
			'ShoulderLeft_ElbowLeft',
			'ElbowLeft_WristLeft',
			'WristLeft_ThumbLeft',
			'WristLeft_HandLeft',
			'HandLeft_HandTipLeft',
			'SpineShoulder_SpineMid',
			'SpineMid_SpineBase',
			'SpineBase_HipRight',
			'HipRight_KneeRight',
			'KneeRight_AnkleRight',
			'AnkleRight_FootRight',
			'SpineBase_HipLeft',
			'HipLeft_KneeLeft',
			'KneeLeft_AnkleLeft',
			'AnkleLeft_FootLeft'
			]

	if arg_ == 'leftSide':
		attribAnthv1Arg = [
				'ShoulderCenter_ShoulderLeft',
				'ShoulderLeft_ElbowLeft',
				'ElbowLeft_WristLeft',
				'WristLeft_HandLeft',
				'HipCenter_HipLeft',
				'HipLeft_KneeLeft',
				'KneeLeft_AnkleLeft',
				'AnkleLeft_FootLeft'
				]

		attribAnthv2Arg = [
				'SpineShoulder_ShoulderLeft',
				'ShoulderLeft_ElbowLeft',
				'ElbowLeft_WristLeft',
				'WristLeft_ThumbLeft',
				'WristLeft_HandLeft',
				'HandLeft_HandTipLeft',
				'SpineBase_HipLeft',
				'HipLeft_KneeLeft',
				'KneeLeft_AnkleLeft',
				'AnkleLeft_FootLeft'
				]
		return attribAnthv1All, attribAnthv2All, attribAnthv1Arg, attribAnthv2Arg

	elif arg_ == 'rightSide':
		attribAnthv1Arg = [
				'ShoulderCenter_ShoulderRight',
				'ShoulderRight_ElbowRight',
				'ElbowRight_WristRight',
				'WristRight_HandRight',
				'HipCenter_HipRight',
				'HipRight_KneeRight',
				'KneeRight_AnkleRight',
				'AnkleRight_FootRight',
				]

		attribAnthv2Arg = [
				'SpineShoulder_ShoulderRight',
				'ShoulderRight_ElbowRight',
				'ElbowRight_WristRight',
				'WristRight_ThumbRight',
				'WristRight_HandRight',
				'HandRight_HandTipRight',
				'SpineBase_HipRight',
				'HipRight_KneeRight',
				'KneeRight_AnkleRight',
				'AnkleRight_FootRight',
				]
		return attribAnthv1All, attribAnthv2All, attribAnthv1Arg, attribAnthv2Arg

	return attribAnthv1All, attribAnthv2All, attribAnthv1All, attribAnthv2All

def attribGait(arg_):
	attribGaitAll = [
			'Peaks-HipRight_KneeRight',
			'Valleys-HipRight_KneeRight',
			'Peaks-KneeRight_AnkleRight',
			'Valleys-KneeRight_AnkleRight',
			'Peaks-AnkleRight_FootRight',
			'Valleys-AnkleRight_FootRight',
			'Peaks-HipLeft_KneeLeft',
			'Valleys-HipLeft_KneeLeft',
			'Peaks-KneeLeft_AnkleLeft',
			'Valleys-KneeLeft_AnkleLeft',
			'Peaks-AnkleLeft_FootLeft',
			'Valleys-AnkleLeft_FootLeft',
			'StrideLength',
			'StrideWidth',
			'CycleTime',
			'Velocity'
			]
	# Left Side
	if arg_ == 'leftSide':
		attribGaitArg = [
			'Peaks-HipLeft_KneeLeft',
			'Valleys-HipLeft_KneeLeft',
			'Peaks-KneeLeft_AnkleLeft',
			'Valleys-KneeLeft_AnkleLeft',
			'Peaks-AnkleLeft_FootLeft',
			'Valleys-AnkleLeft_FootLeft',
			'StrideLength',
			'StrideWidth',
			'CycleTime',
			'Velocity'
			]
		return attribGaitAll, attribGaitArg

	# Right Side
	elif arg_ == 'rightSide':
		attribGaitArg = [
			'Peaks-HipRight_KneeRight',
			'Valleys-HipRight_KneeRight',
			'Peaks-KneeRight_AnkleRight',
			'Valleys-KneeRight_AnkleRight',
			'Peaks-AnkleRight_FootRight',
			'Valleys-AnkleRight_FootRight',
			'StrideLength',
			'StrideWidth',
			'CycleTime',
			'Velocity'
			]
		return attribGaitAll, attribGaitArg

	return attribGaitAll, attribGaitAll


def attribAnthArff(attribAnthv1, attribAnthv2, argattrib):

	if argattrib == 'allData':
		attributesv1 = [
				('Height', 'REAL'),
				('Head_ShoulderCenter', 'REAL'),
				('ShoulderCenter_ShoulderRight', 'REAL'),
				('ShoulderRight_ElbowRight', 'REAL'),
				('ElbowRight_WristRight', 'REAL'),
				('WristRight_HandRight', 'REAL'),
				('ShoulderCenter_ShoulderLeft', 'REAL'),
				('ShoulderLeft_ElbowLeft', 'REAL'),
				('ElbowLeft_WristLeft', 'REAL'),
				('WristLeft_HandLeft', 'REAL'),
				('ShoulderCenter_Spine', 'REAL'),
				('Spine_HipCenter', 'REAL'),
				('HipCenter_HipRight', 'REAL'),
				('HipRight_KneeRight', 'REAL'),
				('KneeRight_AnkleRight', 'REAL'),
				('AnkleRight_FootRight', 'REAL'),
				('HipCenter_HipLeft', 'REAL'),
				('HipLeft_KneeLeft', 'REAL'),
				('KneeLeft_AnkleLeft', 'REAL'),
				('AnkleLeft_FootLeft', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]
		attributesv2 = [
				('Height', 'REAL'),
				('Head_Neck', 'REAL'),
				('Neck_SpineShoulder','REAL'),
				('SpineShoulder_ShoulderRight', 'REAL'),
				('ShoulderRight_ElbowRight', 'REAL'),
				('ElbowRight_WristRight', 'REAL'),
				('WristRight_ThumbRight', 'REAL'),
				('WristRight_HandRight', 'REAL'),
				('HandRight_HandTipRight', 'REAL'),
				('SpineShoulder_ShoulderLeft', 'REAL'),
				('ShoulderLeft_ElbowLeft', 'REAL'),
				('ElbowLeft_WristLeft', 'REAL'),
				('WristLeft_ThumbLeft', 'REAL'),
				('WristLeft_HandLeft', 'REAL'),
				('HandLeft_HandTipLeft', 'REAL'),
				('SpineShoulder_SpineMid', 'REAL'),
				('SpineMid_SpineBase', 'REAL'),
				('SpineBase_HipRight', 'REAL'),
				('HipRight_KneeRight', 'REAL'),
				('KneeRight_AnkleRight', 'REAL'),
				('AnkleRight_FootRight', 'REAL'),
				('SpineBase_HipLeft', 'REAL'),
				('HipLeft_KneeLeft', 'REAL'),
				('KneeLeft_AnkleLeft', 'REAL'),
				('AnkleLeft_FootLeft', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]

	elif argattrib == 'leftSide':
		attributesv1 = [
				('ShoulderCenter_ShoulderLeft', 'REAL'),
				('ShoulderLeft_ElbowLeft', 'REAL'),
				('ElbowLeft_WristLeft', 'REAL'),
				('WristLeft_HandLeft', 'REAL'),
				('HipCenter_HipLeft', 'REAL'),
				('HipLeft_KneeLeft', 'REAL'),
				('KneeLeft_AnkleLeft', 'REAL'),
				('AnkleLeft_FootLeft', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]
		attributesv2 = [
				('SpineShoulder_ShoulderLeft', 'REAL'),
				('ShoulderLeft_ElbowLeft', 'REAL'),
				('ElbowLeft_WristLeft', 'REAL'),
				('WristLeft_ThumbLeft', 'REAL'),
				('WristLeft_HandLeft', 'REAL'),
				('HandLeft_HandTipLeft', 'REAL'),
				('SpineBase_HipLeft', 'REAL'),
				('HipLeft_KneeLeft', 'REAL'),
				('KneeLeft_AnkleLeft', 'REAL'),
				('AnkleLeft_FootLeft', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]

	elif argattrib == 'rightSide':
		attributesv1 = [
				('ShoulderCenter_ShoulderRight', 'REAL'),
				('ShoulderRight_ElbowRight', 'REAL'),
				('ElbowRight_WristRight', 'REAL'),
				('WristRight_HandRight', 'REAL'),
				('HipCenter_HipRight', 'REAL'),
				('HipRight_KneeRight', 'REAL'),
				('KneeRight_AnkleRight', 'REAL'),
				('AnkleRight_FootRight', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]
		attributesv2 = [
				('SpineShoulder_ShoulderRight', 'REAL'),
				('ShoulderRight_ElbowRight', 'REAL'),
				('ElbowRight_WristRight', 'REAL'),
				('WristRight_ThumbRight', 'REAL'),
				('WristRight_HandRight', 'REAL'),
				('HandRight_HandTipRight', 'REAL'),
				('SpineBase_HipRight', 'REAL'),
				('HipRight_KneeRight', 'REAL'),
				('KneeRight_AnkleRight', 'REAL'),
				('AnkleRight_FootRight', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]

	return attributesv1, attributesv2


def attribGaitArff(attribGaitv1, attribGaitv2, argattrib):
	if argattrib == 'allData':
		attributes = [
				('Peaks-HipRight_KneeRight', 'REAL'),
				('Valleys-HipRight_KneeRight', 'REAL'),
				('Peaks-KneeRight_AnkleRight', 'REAL'),
				('Valleys-KneeRight_AnkleRight', 'REAL'),
				('Peaks-AnkleRight_FootRight', 'REAL'),
				('Valleys-AnkleRight_FootRight', 'REAL'),
				('Peaks-HipLeft_KneeLeft', 'REAL'),
				('Valleys-HipLeft_KneeLeft', 'REAL'),
				('Peaks-KneeLeft_AnkleLeft', 'REAL'),
				('Valleys-KneeLeft_AnkleLeft', 'REAL'),
				('Peaks-AnkleLeft_FootLeft', 'REAL'),
				('Valleys-AnkleLeft_FootLeft', 'REAL'),
				('StrideLength', 'REAL'),
				('StrideWidth', 'REAL'),
				('CycleTime', 'REAL'),
				('Velocity', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]
	if argattrib == 'leftSide':
		attributes = [
				('Peaks-HipLeft_KneeLeft', 'REAL'),
				('Valleys-HipLeft_KneeLeft', 'REAL'),
				('Peaks-KneeLeft_AnkleLeft', 'REAL'),
				('Valleys-KneeLeft_AnkleLeft', 'REAL'),
				('Peaks-AnkleLeft_FootLeft', 'REAL'),
				('Valleys-AnkleLeft_FootLeft', 'REAL'),
				('StrideLength', 'REAL'),
				('StrideWidth', 'REAL'),
				('CycleTime', 'REAL'),
				('Velocity', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]
	if argattrib == 'rightSide':
		attributes = [
				('Peaks-HipRight_KneeRight', 'REAL'),
				('Valleys-HipRight_KneeRight', 'REAL'),
				('Peaks-KneeRight_AnkleRight', 'REAL'),
				('Valleys-KneeRight_AnkleRight', 'REAL'),
				('Peaks-AnkleRight_FootRight', 'REAL'),
				('Valleys-AnkleRight_FootRight', 'REAL'),
				('StrideLength', 'REAL'),
				('StrideWidth', 'REAL'),
				('CycleTime', 'REAL'),
				('Velocity', 'REAL'),
				('Name', ['0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
				]
	return attributes


####################################################################################


def saveArffFile(datav1, datav2, attribv1, attribv2, filtering, argattrib, rand_i, aux_i, t):

	k = ''

	if t == 'anth':
		x = 'anthropometry'
	elif t == 'gait':
		x = 'gaitAttributes'


	if argattrib == 'allData':
		k = 'ArffFiles/Data/'+x+'/allData/'+str(aux_i)+'/'
	elif argattrib == 'leftSide':
		k = 'ArffFiles/Data/'+x+'/leftSide/'+str(aux_i)+'/'
	elif argattrib == 'rightSide':
		k = 'ArffFiles/Data/'+x+'/rightSide/'+str(aux_i)+'/'


	testFilev1 = k+'testFilev1'+filtering+'Rand'+str(rand_i)+'Size'+str(aux_i)+'.arff'
	testFilev2 = k+'testFilev2'+filtering+'Rand'+str(rand_i)+'Size'+str(aux_i)+'.arff'

	#print (dataAnthv1)
	#print (attribAnthv1)
	#print (dataAnthv2)
	#print (attribAnthv2)

	##
	# Anthopometry.
	##
	if t == 'anth':
		attributesAnthv1, attributesAnthv2 = attribAnthArff(attribv1, attribv2, argattrib)
		## For Kinect v1	

		objAnthv1 = {
			   'description': 'u',
			   'relation': 'anthropometry',
			   'attributes': attributesAnthv1,
			   'data': datav1
			   }

		## For Kinect v2

		objAnthv2 = {
			   'description': 'u',
			   'relation': 'anthropometry',
			   'attributes': attributesAnthv2,
			   'data': datav2
			   }

		#print (objv1)
		fv1 = open(testFilev1, 'a')
		fv2 = open(testFilev2, 'a')
		arff.dump(objAnthv1, fv1)
		arff.dump(objAnthv2, fv2)
		fv1.close()
		fv2.close()


	##
	# Gait Attributes.
	##
	elif t == 'gait':
		attributesGait = attribGaitArff(attribv1, attribv2, argattrib)
		## For Kinect v1	

		objGaitv1 = {
			   'description': 'u',
			   'relation': 'anthropometry',
			   'attributes': attributesGait,
			   'data': datav1
			   }

		## For Kinect v2

		objGaitv2 = {
			   'description': 'u',
			   'relation': 'anthropometry',
			   'attributes': attributesGait,
			   'data': datav2
			   }

		#print (objv1)
		fv1 = open(testFilev1, 'a')
		fv2 = open(testFilev2, 'a')
		arff.dump(objGaitv1, fv1)
		arff.dump(objGaitv2, fv2)
		fv1.close()
		fv2.close()


####################################################################################
def main(argattrib):
	##
	# aux_x é utilizado para agrupar conjunto de dados para a analise no weka.
	##
	aux_x = [4,8,12,16]
	
	##
	# listRandColectData é utilizado para sortear n coletas para serem agrupadas e,
	# posteriormente, analisadas no weka.
	listRandColectData = [0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

	x = ()
	s = {}

	for aux_i in aux_x:
		print (aux_i)
		##
		# Esse for nos diz o 
		##
		for rand_i in range(10):
			s ={}
			while len(s) < aux_i:
				x += (random.choice(listRandColectData),)
				s = set(x)
			x = ()
			print(s)


			for i in ['notFiltered', 'filtered']:

				##
				# Read and organize all files related to antropometry.
				###
				pathAnthv1 = 'data/v1/mean_std/'+i+'/anthropometry/np/'
				pathAnthv2 = 'data/v2/mean_std/'+i+'/anthropometry/np/'

				filesAnthv1 = sorted(os.listdir(pathAnthv1))
				filesAnthv2 = sorted(os.listdir(pathAnthv2))
				#print (filesAnthv1)
				#print (filesAnthv2)


				##
				# Read and organize all files related to Gait Attributes.
				##
				pathGaitv1 = 'data/v1/mean_std/'+i+'/gaitAttributes/np/'
				pathGaitv2 = 'data/v2/mean_std/'+i+'/gaitAttributes/np/'

				filesGaitv1 = sorted(os.listdir(pathGaitv1))
				filesGaitv2 = sorted(os.listdir(pathGaitv2))
				
				#print (filesGaitv1)
				#print (filesGaitv2)

				#input()

				##
				# Antropometria.
				# attribAnthv(1|2): Todos os atributos.
				# attribAnthv(1|2)_(1|2): Os atributos que vão realmente ser salvos.
				##
				attribAnthv1, attribAnthv2, attribAnthv1_2, attribAnthv2_2 = attribAnth(argattrib)
				#print (attribAnthv1)
				#print (attribAnthv2)

				##
				# Gait Attributes.
				# attribGait: Todos os attributos.
				# attribGait_: Todos os attributos que vão ser salvos.
				##
				attribGaitv12, attribGait_ = attribGait(argattrib)


				##################################################################
				# Anthropometry.
				##
				if len(filesAnthv1) == len(filesAnthv2):
					dataAnthv1 = []
					dataAnthv2 = []
					for i2 in range(len(filesAnthv1)):
						if filesAnthv1[i2] == 'attrib.np' or filesAnthv2[i2] == 'attrib.np':
							continue
						if i2 not in s:
							continue

						dictAnthv1 = {a: [] for a in ['Name'] + attribAnthv1}

						dictAnthv2 = {a: [] for a in ['Name'] + attribAnthv2}
		 
						#dictAnthv1['Name'] = filesAnthv1[i2].split('.np')[0]
						#dictAnthv2['Name'] = filesAnthv2[i2].split('.np')[0]
						dictAnthv1['Name'] = i2
						dictAnthv2['Name'] = i2

						# Files Kinect v1
						#print (filesAnthv1[i2])
						fv1 = open(pathAnthv1+filesAnthv1[i2], 'rb')
						while True:
							try:
								d = pickle.load(fv1)
							except:
								break

							for j in d.keys():
								dictAnthv1[j].append(d[j])
						#print (dictAnthv1)
						#print (attribAnthv1)

						# Files Kinect v2
						#print (filesAnthv2[i2])
						fv2 = open(pathAnthv2+filesAnthv2[i2], 'rb')
						while True:
							try:
								d = pickle.load(fv2)
							except:
								break

							for j in d.keys():
								dictAnthv2[j].append(d[j])
						#print (dictAnthv2)
						#print (attribAnthv2)

						#print ('##################')


						for j in range(len(dictAnthv1[attribAnthv1[0]])):
							auxv1 = []
							for k in attribAnthv1_2:
								auxv1.append(dictAnthv1[k][j][0])
							auxv1.append(dictAnthv1['Name'])
							dataAnthv1.append(auxv1)
						

						for j in range(len(dictAnthv2[attribAnthv2[0]])):
							auxv2 = []
							for k in attribAnthv2_2:
								auxv2.append(dictAnthv2[k][j][0])
							auxv2.append(dictAnthv2['Name'])
							dataAnthv2.append(auxv2)

					
					#print (dataAnthv1)
					#print ('#########################')
					#print (dataAnthv2)

					#input()
					saveArffFile(dataAnthv1, dataAnthv2, attribAnthv1, attribAnthv2, i, argattrib, rand_i, aux_i, 'anth')
					#input()

				##################################################################
				# Gait Attributes
				##
				if len(filesGaitv1) == len(filesGaitv2):
					dataGaitv1 = []
					dataGaitv2 = []
					for i2 in range(len(filesGaitv1)):
						if filesGaitv1[i2] == 'attrib.np' or filesGaitv2[i2] == 'attrib.np':
							continue
						if i2 not in s:
							continue

						dictGaitv1 = {a: [] for a in ['Name'] + attribGaitv12}

						dictGaitv2 = {a: [] for a in ['Name'] + attribGaitv12}

						dictGaitv1['Name'] = i2
						dictGaitv2['Name'] = i2

						# Files Kinect v1
						#print (filesGaitv1[i2])
						fv1 = open(pathGaitv1+filesGaitv1[i2], 'rb')
						while True:
							try:
								d = pickle.load(fv1)
							except:
								break

							for j in d.keys():
								dictGaitv1[j].append(d[j])
						#print (dictGaitv1)
						#print (attribGaitv1)

						# Files Kinect v2
						#print (filesGaitv2[i2])
						fv2 = open(pathGaitv2+filesGaitv2[i2], 'rb')
						while True:
							try:
								d = pickle.load(fv2)
							except:
								break

							for j in d.keys():
								dictGaitv2[j].append(d[j])
						#print (dictAnthv2)
						#print (attribAnthv2)

						for j in range(len(dictGaitv1[attribGaitv12[0]])):
							auxv1 = []
							for k in attribGait_:
								auxv1.append(dictGaitv1[k][j][0])
							auxv1.append(dictGaitv1['Name'])
							dataGaitv1.append(auxv1)
						

						for j in range(len(dictGaitv2[attribGaitv12[0]])):
							auxv2 = []
							for k in attribGait_:
								auxv2.append(dictGaitv2[k][j][0])
							auxv2.append(dictGaitv2['Name'])
							dataGaitv2.append(auxv2)

					saveArffFile(dataGaitv1, dataGaitv2, attribGaitv12, attribGaitv12, i, argattrib, rand_i, aux_i, 'gait')
					##################################################################










main(sys.argv[1])