from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from numpy import deg2rad, cos, sin, arccos,arctan2, rad2deg, pi



def ik(x, y, o):
    l1 = 21e-2
    l2 = 22.33e-2
    l3 = 3e-2

    x2 = x - l3*cos(o)
    y2 = y - l3*sin(o)

    print(f"{x2} \t {y2}")

    q2 = arccos((x2**2 + y2**2 - l1**2 - l2**2) / (2*l1*l2))


    #por algum motivo tive que alterar os sinais nessas duas linhas, petercorke me acuda
    q1 = arctan2(y2,x2) + arctan2(l2*sin(q2),(l1+l2*cos(q2)))
    q2 = -q2 #

    q3 = o - (q2+q1)
    
    print(f"{rad2deg(q1)}° \t {rad2deg(q2)}° \t {rad2deg(q3)}°")
    return [q1, q2, q3]

q1, q2, q3 = ik(1e-2, 1e-2, deg2rad(-120))

#simulation stuff
client = RemoteAPIClient()
sim = client.require('sim')

j1 = sim.getObject("/NiryoOne/Joint{1}")
j2 = sim.getObject("/NiryoOne/Joint{2}")
j3 = sim.getObject("/NiryoOne/Joint{3}")

sim.setStepping(True)
sim.startSimulation()

sim.setJointTargetPosition(j1, q1 - pi/2)
sim.setJointTargetPosition(j2, q2 + pi/2)
sim.setJointTargetPosition(j3, q3)


while (t := sim.getSimulationTime()) < 50:
  
    sim.step()
sim.stopSimulation()