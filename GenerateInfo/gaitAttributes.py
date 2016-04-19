#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-08-25 14:26:32
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-16 15:49:22

import numpy as np
from scipy.signal import argrelextrema
#######################################################################################
# Generate all gait attributes.
# Kinematic parameters: Angles from hip, knee and ankle.
# Others Parameters: Stride Length(Comprimento da passada), Stride Width(Largura da
# passada), Cycle Time(Time between a complete cycle) and Velocity(velocidade que uma
# pessoa completa um ciclo de caminhar).
#######################################################################################

def generategaitAttributes(dataAnth, datafd):

	# List of keys to the dictionary that is going to store all angles info.
	attribGaitAttributes = [
						'HipRight_KneeRight',
						'KneeRight_AnkleRight',
						'AnkleRight_FootRight',
						'HipLeft_KneeLeft',
						'KneeLeft_AnkleLeft',
						'AnkleLeft_FootLeft',
						'StrideLength',
						'StrideWidth'
						]

	# Create the dictionary to store all data.
	gaitAttributes = {i: [] for i in attribGaitAttributes}

	# Hip angles
	# Use the formula of a inverted pendulum to calculate the angle of the hip.
	ir = 'HipRight_KneeRight'
	il = 'HipLeft_KneeLeft'
	gaitAttributes[ir] = (90 - np.arctan2(datafd[ir.split('_')[0]][1] - datafd[ir.split('_')[-1]][1], datafd[ir.split('_')[0]][0] - datafd[ir.split('_')[-1]][0])*(180/np.pi))*-1 # Right
	gaitAttributes[il] = (90 - np.arctan2(datafd[il.split('_')[0]][1] - datafd[il.split('_')[-1]][1], datafd[il.split('_')[0]][0] - datafd[il.split('_')[-1]][0])*(180/np.pi))*-1 # Left

	# Knee Angles
	jr = 'KneeRight_AnkleRight'
	jl = 'KneeLeft_AnkleLeft'
	gaitAttributes[jr] = 180 - np.arccos(dataAnth[jr][0]/dataAnth[jr][3])*(180/np.pi) # Right
	gaitAttributes[jl] = 180 - np.arccos(dataAnth[jl][0]/dataAnth[jl][3])*(180/np.pi) # Left

	# Foot angles
	# Não me parece muito certo ainda.
	ir = 'AnkleRight_FootRight'
	il = 'AnkleLeft_FootLeft'
	gaitAttributes[ir] = 180 - np.arccos(dataAnth[ir][0]/dataAnth[ir][3])*(180/np.pi) # Right
	gaitAttributes[il] = 180 - np.arccos(dataAnth[il][0]/dataAnth[il][3])*(180/np.pi) # Left

	# Stride Lenght
	gaitAttributes['StrideLength'] = abs(datafd['FootRight'][0] - datafd['FootLeft'][0])
	
	# Stride Width
	gaitAttributes['StrideWidth'] = abs(datafd['FootLeft'][2] - datafd['FootRight'][2])
	"""
	# Averange Stride Lenght
	# Calcula o a distância média do comprimento de uma passada.
	avgStrideLenght = 0
	countStrideLenght = 0
	strideLenghtPeaks = argrelextrema(gaitAttributes['StrideLength'], np.greater)
	strideLengthValleys = argrelextrema(gaitAttributes['StrideLength'], np.less)

	if len(strideLenghtPeaks[0]) > len(strideLengthValleys[0]):
		for i in range(0, len(strideLengthValleys[0])):
			avgStrideLenght += abs(gaitAttributes['StrideLength'][strideLenghtPeaks[0][i]] - gaitAttributes['StrideLength'][strideLengthValleys[0][i]])
			avgStrideLenght += abs(gaitAttributes['StrideLength'][strideLenghtPeaks[0][i]] - gaitAttributes['StrideLength'][strideLengthValleys[0][i+1]])
			countStrideLenght += 1
	elif len(strideLenghtPeaks[0]) < len(strideLengthValleys[0]):
		for i in range(0, len(strideLenghtPeaks[0])):
			avgStrideLenght += abs(gaitAttributes['StrideLength'][strideLenghtPeaks[0][i]] - gaitAttributes['StrideLength'][strideLengthValleys[0][i]])
			avgStrideLenght += abs(gaitAttributes['StrideLength'][strideLenghtPeaks[0][i]] - gaitAttributes['StrideLength'][strideLengthValleys[0][i+1]])
			countStrideLenght += 1
	else:
		for i in range(0, len(strideLenghtPeaks[0])):
			avgStrideLenght += abs(gaitAttributes['StrideLength'][strideLenghtPeaks[0][i]] - gaitAttributes['StrideLength'][strideLengthValleys[0][i]])
			try:
				avgStrideLenght += abs(gaitAttributes['StrideLength'][strideLenghtPeaks[0][i]] - gaitAttributes['StrideLength'][strideLengthValleys[0][i+1]])
			except:
				pass
			countStrideLenght += 1
	#print (avgStrideLenght)
	#print (countStrideLenght)
	avgStrideLenght /= countStrideLenght
	
	# Averange Cycle Time
	cycleTime = 0
	countAvgFrameForStrideLenght = 0
	k = 0
	for i in range(1, len(strideLenghtPeaks[0]), 2):
		cycleTime += abs(k - strideLenghtPeaks[0][i])
		k = strideLenghtPeaks[0][i]
		countAvgFrameForStrideLenght+=1
	cycleTime /= countAvgFrameForStrideLenght

	#print (strideLenghtPeaks)
	#print (strideLengthValleys)
	#print (len(strideLenghtPeaks[0]))
	#print (len(strideLengthValleys[0]))
	#print (countStrideLenght)


	# CycleTime and Velocity
	gaitAttributes['CycleTime'] = cycleTime / 30 # 30 is the frame rate of all captures
	gaitAttributes['Velocity'] = avgStrideLenght / gaitAttributes['CycleTime']

	#print (gaitAttributes['CycleTime'])
	#print (gaitAttributes['Velocity'])
	"""
	return gaitAttributes, attribGaitAttributes
