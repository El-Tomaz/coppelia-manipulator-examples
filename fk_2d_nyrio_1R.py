from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import kinematics_2d as kn2d
import numpy as np


client = RemoteAPIClient()
sim = client.require('sim')


#getting joints references 

j1 = sim.getObject("/NiryoOne/Joint{1}") #our j1 is the second joint of the model (count start by 0)
j2 = sim.getObject("/NiryoOne/Joint{2}") #our j2 is the third joint of the model

#joints parameters
theta1 = -60

#simulation stuff
sim.setStepping(True)

sim.startSimulation()

#set joint position
sim.setJointTargetPosition(j1, np.deg2rad(theta1))

#wait for arm to move
while (t := sim.getSimulationTime()) < 10:
    print(f'Simulation time: {t:.2f} [s] \t{np.rad2deg(sim.getJointPosition(j1))}')
    sim.step()
    
    
#get homogeneous transformation
H = kn2d.HT(theta1+90, 21.001e-2) #remeber to add joint offset

print(H)

#extract coordinates from homogenous transform
y_fk = H[0][2] 
z_fk = H[1][2] 

#the fk result is referent to J1 reference, shifting it to the world frame
x_base, y_base, z_base = sim.getObjectPosition(j1) #extract position of j1 referent to world frame

#who is y and z can be a little bit confusing, see the explanation on readme.md
y_fk = y_fk+y_base
z_fk = z_fk+z_base


#getting coordinates of j2 referent to world frame
x_s,y_s,z_s = sim.getObjectPosition(j2) 




print(f"y calculated:{y_fk*100}cm \t y from simulation:{y_s*100}cm")
print(f"z calculated:{z_fk*100}cm \t z from simulation:{z_s*100}cm")

error_y = abs((y_fk - y_s)/y_s)*100
error_z = abs((z_fk - z_s)/z_s)*100

print(f"error y: {error_y}% \t error z: {error_z}%")

sim.stopSimulation()