import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Plots and saves resolution and magnetic fields as a function of iteration

# Nominal magnetic field values
q1s_nom = -0.39773
q2s_nom = 0.217880+0.001472    
q3s_nom = 0.242643-0.0005+0.000729 
q4s_nom = -0.24501-0.002549 
q5s_nom = 0.1112810+0.00111 
q6s_nom = 0.181721-0.000093+0.00010-0.000096 
q7s_nom = -0.0301435+0.0001215 

# Hyper-parameters
numSteps = int(sys.argv[1]) # Number of steps
numBees = int(sys.argv[2])  # Number of bees

reader = np.loadtxt('results.txt')
f, sub = plt.subplots(4, 3, sharex=True)

x = range(0, numSteps)         
for b in range(0, numBees):
    tmp = reader[ reader[:,0]==b ]

    y = tmp[:,8]
    sub[0,0].plot( x, y, c=cm.hot((b+1)/(numBees+1)) )

    y = tmp[:,1] 
    sub[1,0].plot( x, y, c=cm.hot((b+1)/(numBees+1)) )
    y = tmp[:,2] 
    sub[1,1].plot(x, y, c=cm.hot((b+1)/(numBees+1)) )
    y = tmp[:,3] 
    sub[1,2].plot(x, y, c=cm.hot((b+1)/(numBees+1)) )
    y = tmp[:,4] 
    sub[2,0].plot(x, y, c=cm.hot((b+1)/(numBees+1)) )
    y = tmp[:,5] 
    sub[2,1].plot(x, y, c=cm.hot((b+1)/(numBees+1)) )
    y = tmp[:,6] 
    sub[2,2].plot(x, y, c=cm.hot((b+1)/(numBees+1)) )
    y = tmp[:,7] 
    sub[3,0].plot(x, y, c=cm.hot((b+1)/(numBees+1)) )     

sub[0,0].set(ylabel='Resolution')
sub[0,0].set_xlim(0, numSteps)

sub[1,0].set(ylabel='Q1 Gradient')
sub[1,0].set_xlim(0, numSteps)
sub[1,0].axhline(y=q1s_nom, color='r', linestyle='--')

sub[1,1].set(ylabel='Q2 Gradient')
sub[1,1].set_xlim(0, numSteps)
sub[1,1].axhline(y=q2s_nom, color='r', linestyle='--')

sub[1,2].set(ylabel='Q3 Gradient')
sub[1,2].set_xlim(0, numSteps)
sub[1,2].axhline(y=q3s_nom, color='r', linestyle='--')

sub[2,0].set(ylabel='Q4 Gradient')
sub[2,0].set_xlim(0, numSteps)
sub[2,0].axhline(y=q4s_nom, color='r', linestyle='--')

sub[2,1].set(ylabel='Q5 Gradient')
sub[2,1].set_xlim(0, numSteps)
sub[2,1].axhline(y=q5s_nom, color='r', linestyle='--')

sub[2,2].set(ylabel='Q6 Gradient')
sub[2,2].set_xlim(0, numSteps)
sub[2,2].axhline(y=q6s_nom, color='r', linestyle='--')

sub[3,0].set(ylabel='Q7 Gradient')
sub[3,0].set_xlim(0, numSteps)
sub[3,0].axhline(y=q7s_nom, color='r', linestyle='--')


#
#sub[0,1].plot(x, y, 'k-')
#sub[0,1].set(ylabel='Resolution')
#sub[0,1].set_xlim(0, num_steps)
#sub[0,1].plot(x, yy, 'b-')
#
#sub[0,2].plot(x, y, 'k-')
#sub[0,2].set(ylabel='Resolution')
#sub[0,2].set_xlim(0, num_steps)
#sub[0,2].plot(x, yy, 'b-')
#
#y = np.asarray(x_observed[0,:]).reshape(-1)
#sub[1,0].plot(x, y, 'k-')
#sub[1,0].set(ylabel='Q1 Gradient')
#sub[1,0].axhline(y=q1s_nom, color='r', linestyle='--')
#sub[1,0].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(x_observed[1,:]).reshape(-1)
#sub[1,1].plot(x, y, 'k-')
#sub[1,1].set(ylabel='Q2 Gradient')
#sub[1,1].axhline(y=q2s_nom, color='r', linestyle='--')
#sub[1,1].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(x_observed[2,:]).reshape(-1)
#sub[1,2].plot(x, y, 'k-')
#sub[1,2].set(ylabel='Q3 Gradient')
#sub[1,2].axhline(y=q3s_nom, color='r', linestyle='--')
#sub[1,2].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(x_observed[3,:]).reshape(-1)
#sub[2,0].plot(x, y, 'k-')
#sub[2,0].set(ylabel='Q4 Gradient')
#sub[2,0].axhline(y=q4s_nom, color='r', linestyle='--')
#sub[2,0].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(x_observed[4,:]).reshape(-1)
#sub[2,1].plot(x, y, 'k-')
#sub[2,1].set(ylabel='Q5 Gradient')
#sub[2,1].axhline(y=q5s_nom, color='r', linestyle='--')
#sub[2,1].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(x_observed[5,:]).reshape(-1)
#sub[2,2].plot(x, y, 'k-')
#sub[2,2].set(ylabel='Q6 Gradient')
#sub[2,2].axhline(y=q6s_nom, color='r', linestyle='--')
#sub[2,2].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(x_observed[6,:]).reshape(-1)
#sub[3,0].plot(x, y, 'k-')
#sub[3,0].set(ylabel='Q7 Gradient')
#sub[3,0].axhline(y=q7s_nom, color='r', linestyle='--')
#sub[3,0].plot(i_max,y[i_max],'bo') 
#
#y = np.asarray(dist[0,:]).reshape(-1)
#z = np.asarray(elim[0,:]).reshape(-1)
#sub[3,1].plot(x, y, 'k-')
#sub[3,1].plot(x, z, 'b-')
#sub[3,1].set(xlabel='Iteration', ylabel='Distance steps')
#sub[3,1].axhline(y=theta_nom*1000, color='r', linestyle='--')
#
#sub[3,2].plot(x, y, 'k-')
#sub[3,2].plot(x, z, 'b-')
#sub[3,2].set(xlabel='Iteration', ylabel='Distance steps')
#sub[3,2].axhline(y=theta_nom*1000, color='r', linestyle='--')
#
#f.subplots_adjust( wspace = 0.6, top = None, bottom = None )
#plt.savefig('ResFields-iter.pdf')

plt.show()
plt.close()
