#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2015-08-20 02:25:07
# @Last Modified by:   dutra
# @Last Modified time: 2015-11-16 15:28:30

import numpy as np
from math import *

##################################################################################
# Recebe um arquivo de entrada com os dados referentes a uma caminhada do kinect 
# v1 ou v2, cria um  objeto dicionario de acordo com a versão do kinect e retor-
# na esse dicionário com os dados armazenado organizados da seguinte forma:
# dataSkeleton['junta do corpo'] = [[pontos X], [pontos Y], [pontos Z]]
# atributesSkeleton contem as chaves do dicionario dataSkeleton referentes as jun-
# tas do corpo.
# O dicionario que é retornado está no formato array no formato array, facilitando
# assim a manipulação do mesmo.
##################################################################################

###
# A função formatData() deve ser chamada pelo modulo principal para formatar o ar-
# quivo contendo as informações brutas do Kinect v1 e v2.
##
def formatData(arq, v):

	# Create dictionary for v1 Kinect
	if v == 'v1':
		#print ('Creating dictionary v1 Kinect! fd')
		def dictdata():
			# Tendo em vista que um dicionário não possui uma ordem para acessar os seus 
			# elementos, é necessário utilizar uma lista como referência para percorrer as
			# chaves do dicionário na mesma ordem em que elas são armazenadas pelo Kinect.
			attributesSkeleton = [
						'Head',
						'ShoulderCenter',
						'ShoulderLeft',
						'ShoulderRight',
						'Spine',
						'HipCenter',
						'HipLeft',
						'HipRight',
						'ElbowLeft',
						'WristLeft',
						'HandLeft',
						'ElbowRight',
						'WristRight',
						'HandRight',
						'KneeLeft',
						'AnkleLeft',
						'FootLeft',
						'KneeRight',
						'AnkleRight',
						'FootRight'
						]

			# Dicionário que vai armazenar as informações referentes a uma caminhada.
			return attributesSkeleton


	# Create dictionary for v2 Kinect
	if v == 'v2':
		#print ('Creating dictionary v2 Kinect! fd')
		def dictdata():
			# Tendo em vista que um dicionário não possui uma ordem para acessar os seus 
			# elementos, é necessário utilizar uma lista como referência para percorrer as
			# chaves do dicionário na mesma ordem em que elas são armazenadas pelo Kinect.
			attributesSkeleton = [
						'Head',
						'Neck',
						'SpineShoulder',
						'SpineMid',
						'ShoulderRight',
						'ShoulderLeft',
						'SpineBase',
						'HipRight',
						'HipLeft',
						'ElbowRight',
						'WristRight',
						'HandRight',
						'HandTipRight',
						'ThumbRight',
						'ElbowLeft',
						'WristLeft',
						'HandLeft',
						'HandTipLeft',
						'ThumbLeft',
						'KneeRight',
						'AnkleRight',
						'FootRight',
						'KneeLeft',
						'AnkleLeft',
						'FootLeft'
						]

			return attributesSkeleton


	attributesSkeleton = dictdata()

	# Dicionário que vai armazenar as informações referentes a uma caminhada.
	dataSkeleton = {i: [[], [], []] for i in attributesSkeleton}
	dataSkeleton['TotalFrames'] = 0


	f = open(arq, 'r')


	# Ignora a primeira linha do arquivo .txt de leitura, linhas dos atributos.
	line = f.readline()

	###
	# Lê o arquivo de entrada linha por linha, faz o split separando os valores e
	# armazena os dados em um dicionario no formato junta : [[x], [y], [z]].
	linesWithZeros = 0
	for line in f:
		l = line[:-1].split(',')
		if '0.000000' in l:
			linesWithZeros+=1
			continue
			#print (l)
		if len(l) == 75 or len(l) == 60:

			def saveInfoDict(l):
				# As atribuições nonlocal fazem referencia aos objetos criados em
				# um modulo superior.
				nonlocal dataSkeleton
				nonlocal attributesSkeleton

				# Como na linha line lida do arquivo f estão todos os pontos X, Y
				# e Z referentes a um frame, é necessário percorrer todos os atri-
				# butos de três em três posições.
				pos = 0
				for i in attributesSkeleton:
					dataSkeleton[i][0].append(float(l[pos]))
					dataSkeleton[i][1].append(float(l[pos+1]))
					dataSkeleton[i][2].append(float(l[pos+2]))
					pos+=3
			
			saveInfoDict(l)
	f.close()
	
	# Salva o número total de frames da caminhada em questão.
	dataSkeleton['TotalFrames'] = len(dataSkeleton['Head'][0])

	###
	# Transforma as listas do dicionario contendo as informações dos eixos X, Y e
	# Z em arrays.
	for i in attributesSkeleton:
		dataSkeleton[i][0] = np.array(dataSkeleton[i][0])
		dataSkeleton[i][1] = np.array(dataSkeleton[i][1])
		dataSkeleton[i][2] = np.array(dataSkeleton[i][2])
	##

	return dataSkeleton, attributesSkeleton
