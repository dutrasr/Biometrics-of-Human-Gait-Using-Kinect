#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutra
# @Date:   2015-10-14 23:27:55
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-13 00:24:38

from scipy.signal import savgol_filter

def dataFilter(datafd, attribfd):

	datafdFiltered = {i: [[], [], []] for i in attribfd}

	windowSize = 11

	for i in attribfd:
		datafdFiltered[i][0] = savgol_filter(datafd[i][0], windowSize, 3)
		datafdFiltered[i][1] = savgol_filter(datafd[i][1], windowSize, 3)
		datafdFiltered[i][2] = savgol_filter(datafd[i][2], windowSize, 3)

	datafdFiltered['TotalFrames'] = datafd['TotalFrames']

	return datafdFiltered, attribfd






































"""
def buterworthFilter():
	N  = 1    # Filter order
	Wn = 0.001 # Cutoff frequency
	B, A = signal.butter(N, Wn, output='ba')
	return B, A

def signalFilter(data, attrib, v, t):

	def signalFilterAnth():
		nonlocal data, attrib
		nonlocal B, A

		dataAnthFiltered = {i:[[], [], [], []] for i in attrib}

		for j in attrib:
			for k in range(len(data[j])):
				dataAnthFiltered[j][k] = signal.filtfilt(B, A, data[j][k])
		return dataAnthFiltered

	def signalFilterAnthII():
		nonlocal data, attrib
		nonlocal B, A

		dataAnthIIFiltered = {i:[] for i in attrib}

		#dataAnthIIFiltered['Height'] = signal.filtfilt(B , A, data['Height'])
		k = []
		[k.append(data['StrideLength'][i]) for i in signal.argrelextrema(data['StrideLength'], np.greater)[0]]
		dataAnthIIFiltered['StrideLength'] = k
		k = []
		[k.append(data['StrideLength'][i]) for i in signal.argrelextrema(data['StrideWidth'], np.greater)[0]]
		dataAnthIIFiltered['StrideWidth'] = k

		return dataAnthIIFiltered

	def signalFilterAngles():
		nonlocal data, attrib
		nonlocal B, A

		dataAnglesFiltered = {i:[] for i in attrib}
		for i in attrib:
			dataAnglesFiltered[i] = pandas.ewma(data[i], span=4)
		return dataAnglesFiltered

	B, A = buterworthFilter()

	if t == 'anth':
		dataAnthFiltered = signalFilterAnth()
		return dataAnthFiltered

	if t == 'anthII':
		dataAnthIIFiltered = signalFilterAnthII()
		return dataAnthIIFiltered
	if t == 'angles':
		dataAnglesFiltered = signalFilterAngles()
		return dataAnglesFiltered
"""