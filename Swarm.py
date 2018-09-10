#!/usr/bin/env python

import sys, math
import os, shutil, signal
#import commands
import subprocess as commands
import re
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocessing
import itertools
import timeit

from cosy import cosyrun 

# Hyper-parameters
numSteps = int(sys.argv[1]) # Number of steps
numBees = int(sys.argv[2])  # Number of bees
a = 0.95 # inertia term --- more like a drag parameter!!!!!!!!!!
b = 1.5/16 # acceleration term
vfactor = 0.1  # factor determining bees initial velocity

# Nominal quad fields at pole tip
qNom = [-0.39773, 0.217880+0.001472, 0.242643-0.0005+0.000729, -0.24501-0.002549, 0.1112810+0.00111, 0.181721-0.000093+0.00010-0.000096, -0.0301435+0.0001215] 

# Returns initial bees' position and velocity
def createBees():
    ''' Creates a matrix with elements drawn from a uniform distribution '''
    x = [ [random.uniform(-qNom[i]*1.0, qNom[i]*3.0) for i in range(7)] for bee in range(numBees)]
    v = [ [random.uniform(-qNom[i]*vfactor, qNom[i]*vfactor) for i in range(7)] for bee in range(numBees)]
    return np.asmatrix(x), np.asmatrix(v)

# Returns bees' personal, global best position and personal best resolution
def bestBees():
    reader = np.loadtxt('results.txt')
    xgbest = reader[ np.argmax(reader[:,8]), [1,2,3,4,5,6,7]] 
    for bee in range(0, numBees):   # Loop over all bees 
        tmp1 = reader[ reader[:,0]==bee ]
        tmp2 = tmp1[ np.argmax(tmp1[:,8]), [1,2,3,4,5,6,7]] 
        tmp3 = [bee, np.max[tmp1[:,8]]]
        if bee==0:
            xpbest = tmp2
            resbbest = tmp3        
        else:	 
            xpbest = np.vstack((xpbest, tmp2))
            resbbest = np.vstack( resbbest, tmp3 )  
    return np.asmatrix(xpbest), np.asmatrix(xgbest), resbbest

# Returns update position and velocity based on global and personal bees' best
def updateBees(xpbest, xgbest, x, v, resbbest):
    for bee in range(0, numBees):   # Loop over all bees 
        if resbbest[bee, 1] == 0:
            r0 = 0
        else:
            r0 = random.uniform(0,1)
        r1 = random.uniform(0,1)
        ac = b*( r0*(xpbest[bee,:]-x[bee,:]) + r1*(xgbest-x[bee,:]) )
        v[bee,:] = a*v[bee,:] + ac
        x[bee,:] = x[bee,:] + v[bee,:]
    return x, v

# Removing old files
cmd = 'rm -f results.txt'
failure, output = commands.getstatusoutput(cmd)

x, v = createBees()   # Creating bees
startTime = timeit.default_timer()
for i in range(0, numSteps):           # Loop over number of steps
    print('Step %d'%i)
    try: 
        pool = multiprocessing.Pool()  # Take as many processes as possible			
    except: 
        for c in multiprocessing.active_children():
            os.kill(c.pid, signal.SIGKILL)
        pool = multiprocessing.Pool(1) # Only take 1 process	
    for bee in range(0, numBees):   # Loop over all bees (using as many processes as possible)
        pool.apply_async( cosyrun, [bee, x[bee,0], x[bee,1], x[bee,2], x[bee,3], x[bee,4], x[bee,5], x[bee,6]] )
    pool.close()
    pool.join()
    xpbest, xgbest, resbbest = bestBees()  # Find bees' best 
    x, v = updateBees(xpbest, xgbest, x, v, resbbest)  # Updating bees   

print ('Running time (sec): %f' % (timeit.default_timer() - startTime))



 


