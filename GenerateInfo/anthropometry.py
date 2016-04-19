#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-08-22 02:46:49
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-13 00:55:35

from math import *
import numpy as np

##################################################################################
# Recebe como entrada os dados brutos do kinect que foram formatados e calcula a
# distancia euclidiana entre todos os membros vizinho do corpo de uma pessoa, le-
# vando em conta os três eixos e todos os frames de uma caminhada.
# Retorna um novo dicionario com a distancia euclidiana entre as juntas e algumas
# informações adicionais utilizadas para calcular essa distancia euclidiana (base,
# altura, profundidade e a distancia euclidiana).
##################################################################################
def generateAnthropometryData(data, v):

	# Create dictionary for v1 Kinect
	if v == 'v1':
		#print ('Creating dictionary v1 Kinect! anth')
		def dictdata():

			# Lista utilizada como referencia para acessar as informações do dicionario.
			anthropometryAttributes = [
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

			return anthropometryAttributes

	# Create dictionary for v2 Kinect
	if v == 'v2':
		#print ('Creating dictionary v2 Kinect! anth')
		def dictdata():

			# Lista utilizada como referencia para acessar as informações do dicionario.
			anthropometryAttributes = [
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

			return anthropometryAttributes

	anthropometryAttributes = dictdata()

	# Creates the dict to store all joints data
	anthropometry = {i: [[], [], [], []] for i in anthropometryAttributes}

	for i in anthropometryAttributes[1:]:
		# Altura
		anthropometry[i][0] = data[i.split('_')[-1]][1] - data[i.split('_')[0]][1]
		# Base
		anthropometry[i][1] = data[i.split('_')[-1]][0] - data[i.split('_')[0]][0]
		# Profundidade
		anthropometry[i][2] = data[i.split('_')[-1]][2] - data[i.split('_')[0]][2]
		# Hipotenusa(Distancia euclidiana entre as juntas)
		anthropometry[i][3] = np.sqrt(anthropometry[i][0]**2 + anthropometry[i][1]**2 + anthropometry[i][2]**2)

	
	# Height
	# Altura de um indíviduo, soma dos membros partindo da cabeça até os pés.
	# A parte inferior do corpo é claculada fazendo a média entre as juntas
	# do lado esquerdo e direito do corpo.
	if v == 'v1':
		anthropometry['Height'][3] = anthropometry['Head_ShoulderCenter'][3] + anthropometry['ShoulderCenter_Spine'][3] + anthropometry['Spine_HipCenter'][3] + ((anthropometry['HipLeft_KneeLeft'][3] + anthropometry['KneeLeft_AnkleLeft'][3] + anthropometry['AnkleLeft_FootLeft'][0]) + (anthropometry['HipRight_KneeRight'][3] + anthropometry['KneeRight_AnkleRight'][3] + anthropometry['AnkleRight_FootRight'][0]))/2
	if v == 'v2':
		anthropometry['Height'][3] = anthropometry['Head_Neck'][3] + anthropometry['Neck_SpineShoulder'][3] + anthropometry['SpineShoulder_SpineMid'][3] + anthropometry['SpineMid_SpineBase'][3] + ((anthropometry['HipLeft_KneeLeft'][3] + anthropometry['KneeLeft_AnkleLeft'][3] + anthropometry['AnkleLeft_FootLeft'][0]) + (anthropometry['HipRight_KneeRight'][3] + anthropometry['KneeRight_AnkleRight'][3] + anthropometry['AnkleRight_FootRight'][0]))/2

	anthropometry['Height'][0] = [0]*(len(anthropometry['Height'][3]))
	anthropometry['Height'][1] = [0]*(len(anthropometry['Height'][3]))
	anthropometry['Height'][2] = [0]*(len(anthropometry['Height'][3]))


	return anthropometry, anthropometryAttributes