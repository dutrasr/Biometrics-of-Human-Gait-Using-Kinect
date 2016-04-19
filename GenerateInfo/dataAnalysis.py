#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-09-20 20:28:28
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-16 15:01:06

import numpy as np
from scipy.signal import argrelextrema

def peaksValleys(data, attrib):

	for i in range(0,len(attrib)-2):

		k = [[], []] # k[0] picos e k[1] vales

		[k[0].append(data[j]) for j in argrelextrema(data, np.greater)[0]]
		[k[1].append(data[j]) for j in argrelextrema(data, np.less)[0]]

		#print (k[0])
		#print (k[1])

		aux = max(k[0])
		aux2 = min(k[1])
		for i in range(len(k[0])):
			try:
				if aux/k[0][i] < 0.7:
					k[0].pop(i)
			except:
				break


		for i in range(len(k[1])):
			try:
				if aux2/k[1][i] < 0.1:
					k[1].pop(i)
			except:
				break
		#print (k[0])
		#print (k[1])

	return k[0], k[1]


########################################################################################
# Calcula a média e o desvio padrão de quase todos os dados utilizados na analise do
# caminhar humano. gaitAttributes e Anthropometry data.
########################################################################################
def generateDataAnalysis(data, attrib, t):

	# Calcula média das informações de antropometria de uma pessoa.
	if t == 'anth':
		meanStd = {i: [] for i in attrib}

		for i in attrib:

			meanStd[i].append(np.mean(data[i][3]))
			meanStd[i].append(np.std(data[i][3]))

		return meanStd, attrib


	# Calcula os picos e vales do referente de alguns atributos do caminhar. Além disso,
	# calcula também o tempo de cada ciclo do caminhar e a velocidade. 
	elif t == 'gaitAttrib':
		attribGaitAttributes = [
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


		meanStd = {i: [] for i in attribGaitAttributes}
		#print (meanStd)

		for i in range(0, len(attribGaitAttributes)-4, 2):
			#print (data[attrib[i]])
			peaks, valleys = peaksValleys(data[attribGaitAttributes[i].split('-')[-1]], attrib)
			
			meanStd[attribGaitAttributes[i]].append(np.mean(peaks))
			meanStd[attribGaitAttributes[i]].append(np.std(peaks))
			meanStd[attribGaitAttributes[i+1]].append(np.mean(valleys))
			meanStd[attribGaitAttributes[i+1]].append(np.std(valleys))

		# Averange Stride Lenght
		# Calcula o a distância média do comprimento de uma passada.
		avgStrideLenght = 0
		countStrideLenght = 0
		strideLenghtPeaks = argrelextrema(data['StrideLength'], np.greater)
		strideLengthValleys = argrelextrema(data['StrideLength'], np.less)

		if len(strideLenghtPeaks[0]) > len(strideLengthValleys[0]):
			for i in range(0, len(strideLengthValleys[0])):
				avgStrideLenght += abs(data['StrideLength'][strideLenghtPeaks[0][i]] - data['StrideLength'][strideLengthValleys[0][i]])
				avgStrideLenght += abs(data['StrideLength'][strideLenghtPeaks[0][i+1]] - data['StrideLength'][strideLengthValleys[0][i]])
				countStrideLenght += 1
		elif len(strideLenghtPeaks[0]) < len(strideLengthValleys[0]):
			for i in range(0, len(strideLenghtPeaks[0])):
				avgStrideLenght += abs(data['StrideLength'][strideLenghtPeaks[0][i]] - data['StrideLength'][strideLengthValleys[0][i]])
				avgStrideLenght += abs(data['StrideLength'][strideLenghtPeaks[0][i]] - data['StrideLength'][strideLengthValleys[0][i+1]])
				countStrideLenght += 1
		else:
			for i in range(0, len(strideLenghtPeaks[0])):
				avgStrideLenght += abs(data['StrideLength'][strideLenghtPeaks[0][i]] - data['StrideLength'][strideLengthValleys[0][i]])
				try:
					avgStrideLenght += abs(data['StrideLength'][strideLenghtPeaks[0][i]] - data['StrideLength'][strideLengthValleys[0][i+1]])
				except:
					pass
				countStrideLenght += 1
		avgStrideLenght/= countStrideLenght
		#print (avgStrideLenght)
		#print (countStrideLenght)
		meanStd['StrideLength'].append(avgStrideLenght)
		meanStd['StrideLength'].append(0)

		# Stride Width
		meanStd['StrideWidth'].append(np.mean(data['StrideWidth']))
		meanStd['StrideWidth'].append(np.std(data['StrideWidth']))

		# Cycle Time
		cycleTime = 0
		countAvgFrameForStrideLenght = 0
		k = 0
		for i in range(1, len(strideLenghtPeaks[0]), 2):
			cycleTime += abs(k - strideLenghtPeaks[0][i])
			k = strideLenghtPeaks[0][i]
			countAvgFrameForStrideLenght+=1
		cycleTime /= countAvgFrameForStrideLenght

		meanStd['CycleTime'].append(cycleTime/30)
		meanStd['CycleTime'].append(0)

		# Velocity
		meanStd['Velocity'].append(avgStrideLenght/(cycleTime/30))
		return meanStd, attribGaitAttributes



















"""
def mean_stdData(data, attrib, t):


	if 'anth' == t:
		# Armazena as informações de média e desvio padrão de cada conjunto de dados;.
		mean_std = {i: [] for i in attrib}

		for i in attrib:

			mean_std[i].append(np.mean(data[i][3]))
			mean_std[i].append(np.std(data[i][3]))

		return mean_std, attrib

	if 'anthII' == t:
		# Armazena as informações de média e desvio padrão de cada conjunto de dados;.
		mean_std = {i: [] for i in attrib}

		for i in attrib:

			mean_std[i].append(np.mean(data[i]))
			mean_std[i].append(np.std(data[i]))

		return mean_std, attrib

	if 'angles' == t:
		# Armazena as informações de média e desvio padrão de cada conjunto de dados;.
		mean_std = {i: [[], []] for i in attrib}
		for i in attrib:

			mean_std[i][0].append(np.mean(data[i][0]))
			mean_std[i][0].append(np.std(data[i][0]))

			mean_std[i][1].append(np.mean(data[i][1]))
			mean_std[i][1].append(np.std(data[i][1]))


		return mean_std, attrib
"""