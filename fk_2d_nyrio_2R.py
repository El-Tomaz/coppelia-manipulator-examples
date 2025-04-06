from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import kinematics_2d as kn2d
import numpy as np


client = RemoteAPIClient()
sim = client.require('sim')


#getting joints references 

j1 = sim.getObject("/NiryoOne/Joint{1}") #our j1 is the second joint of the model (count start by 0)
j2 = sim.getObject("/NiryoOne/Joint{2}") #our j2 is the third joint of the model
j3 = sim.getObject("/NiryoOne/Joint{3}")

#joints parameters
theta1 = -35
theta2 = 30

a1 = 21e-2
a2 = 22.33e-2

#simulation stuff
sim.setStepping(True)

sim.startSimulation()

#set joint position
sim.setJointTargetPosition(j1, np.deg2rad(theta1))
sim.setJointTargetPosition(j2, np.deg2rad(theta2))


#wait for arm to move
while (t := sim.getSimulationTime()) < 10:
    print(f'Simulation time: {t:.2f} [s] \t{np.rad2deg(sim.getJointPosition(j1))}')
    sim.step()
    
    
#get homogeneous transformation j1 to j2
theta1_rad = np.deg2rad(theta1 + 90) #add offset of 90 of the joint

H1_2 = kn2d.H(
    theta1_rad,
    a1*np.cos(theta1_rad),
    a1*np.sin(theta1_rad)
)

print(H1_2)

#get homogeneous transformation j2 to j3
theta2_rad = np.deg2rad(theta2) #add offset of 90 of the joint

H2_3 = kn2d.H(
    theta1_rad,
    a2,
    0
)

print(H2_3)

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