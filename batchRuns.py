#!/usr/bin/env python

import sys, math
import os, shutil, signal
import subprocess as commands

# Hyper-parameters
numSteps = int(sys.argv[1]) # Number of steps
numBees = int(sys.argv[2])  # Number of bees
numSim = int(sys.argv[3]) # Number of simulations

for i in range(0,numSim):
    cmd = 'rm -f temp-results*'
    failure, output = commands.getstatusoutput(cmd)

    cmd = 'rm -f SwarmCosy*'
    failure, output = commands.getstatusoutput(cmd)

    cmd = 'python Swarm.py ' + str(numSteps) + ' ' + str(numBees)
    failure, output = commands.getstatusoutput(cmd)

    cmd = 'mv results.txt results' + str(i) + '.txt' 
    failure, output = commands.getstatusoutput(cmd)




