#!/usr/bin/python

import cv2
from Tkinter import *
from tkFileDialog import *
import sys
from numpy import *
#from EdgeDetection import EdgeDetection as ed
from ShapeDetection import ShapeDetection as sd
import math

def getFromGroup(shapeDetector,bg):
	detect = shapeDetector.applyDFS(shapeDetector.test,shapeDetector.test.border,bg)
	imgC = shapeDetector.test.originalImg

		
	"""	
	for i in shapeDetector.test.border:
        	 imgC[i[0],i[1]]= [0,0,255]
	"""
	cv2.imwrite("lines_fig.png",imgC)

	return detect

def calcDistributionOfSizes():
    return

def discardLittleLines():
    return

histogram = []
c = {}
def getEquation(point,angle=0):
    
    for angle in range(0,180,10):
        p = point[0]*math.cos(angle) + point[1]*math.sin(angle)

        if [p,angle] not in histogram:
            histogram.append([p,angle])
            c[str(round(p))+","+str(angle)] = 0
        else:
            c[str(round(p))+","+str(angle)] += 1


def drawLines():
    return

"""
Get angle
Identify the rho for each pixel through the image 
dataX
dataY.append(dataX)
"""
"""
def makeVotationByRho(test):
	container = list()
	for y in xrange(test.height):
		xData = list()
		for x in xrange(test.width):
			rho = (x-test.width/2)*cos(test.angles[y][x]) + (y/2 - test.height)*sin(test.angles[y][x])
			xData.append( test.histogram[y][x],(int(180 * (test.angles[y][x] / 3.1416)) / 18), rho )
		container.append(xData)
	return container
"""
def makeVotationByRho(points,test):
	container = list()
	index_counter = 0
	print "points:", points
	for y in range(1,test.height-1,1):
		for x in range(1,test.width-1,1):
			#print (y,x)
			if [y,x] in points:
				print "I am in points"
				rho = (x-test.width/2)*cos(test.angles[index_counter]) + (y/2 - test.height)*sin(test.angles[index_counter]) 
				print "rho: ",rho
				
				container.append([test.angles[index_counter],'%.0f' % (int(180 * (test.angles[index_counter] / 3.1416))/18), '%.0f' % rho,[y,x]])
				#shapeDetector.test.originalImg[y,x] = [0,255,0]
				index_counter += 1
			#else:
				#shapeDetector.test.originalImg[y,x] = [0,0,0]
		
	#for element in points:
		#shapeDetector.test.originalImg[element[0],element[1]] = [255,0,0]
		

	return container

def createCombinations(container,test):
	comb = dict()
	for e in container:
		magnitude,angle,rho,point = e
		combination = (angle,rho)
		if combination in comb:
			comb[combination] += 1
		else:
			comb[combination] = 1
	return comb

def countMostFrecuent(comb):
	bigger = ""
	for i in comb:
		if bigger == "":
			bigger = i
		elif comb[i] > comb[bigger]:
			bigger = i
		
	return bigger

#starting
shapeDetector = sd.ShapeDetection()
shapeDetector.test.path = "LineDetection/figures.png"
shapeDetector.test.detectBorders()
background = shapeDetector.getBackground()

#         0  45 90 -45                                                                                                                         
groups = [[],[],[],[]]

def main():
	fig = getFromGroup(shapeDetector,background)
	
	for i in fig:
        	shapeDetector.test.originalImg[i[0],i[1]] = [100,100,100]
		#shapeDetector.test.originalImg[i] = [100,100,100]
		cv2.imwrite("lines_fig.png",shapeDetector.test.originalImg)

	container = makeVotationByRho(fig,shapeDetector.test)
	comb = createCombinations(container,shapeDetector.test)
	biggerComb = countMostFrecuent(comb)
	print ""
	print "comb: ",comb
	print ""
	print "container: ",container
	for i in container:
		#print "entro a container"
		magnitude,angle,rho,point = i
		print "point: ",point
		print "bg: ", biggerComb
		print "angle,rho ",(angle,rho)
		comp = (angle,rho)
		if biggerComb == comp:	
			print "pinto de azul"
			shapeDetector.test.originalImg[point[0],point[1]] = [255,0,0]
			

	angle = biggerComb[0]
	rho = biggerComb[1]
	

	for x in range(1,shapeDetector.test.width-1,1):
		valuey1 = (-1.0*cos(float(angle)))*x
		valuey2 = (float(rho)/sin(float(angle)))
		valuey = valuey1+valuey2
		#shapeDetector.test.originalImg[valuey/2 - shapeDetector.test.height,x] = [0,0,255]

	print "printing img"
	cv2.imwrite("lines_Test.png",shapeDetector.test.originalImg)
	print "it's supposed img is saved"

def x():
    groupByAngle()

    pointsGrouped = getFromGroup(shapeDetector)

    for point in pointsGrouped:
        

	    maxValue = 0
	    keyChosen = ""

	    print c

	    for key,value in c.items():
		if value > maxValue:
		    maxValue = value
		    keyChosen = key

	    print "key: ",key," value: ",value
    

main()