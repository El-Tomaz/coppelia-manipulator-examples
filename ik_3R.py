from numpy import deg2rad, cos, sin, arccos, arctan,arctan2, rad2deg

l1 = 21e-2
l2 = 22.33e-2
l3 = 5e-2

x = -20e-2
y = 30e-2

o = deg2rad(25)

x2 = x - l3*cos(o)
y2 = y - l3*sin(o)

print(f"{x2} \t {y2}")

q2 = arccos((x2**2 + y2**2 - l1**2 - l2**2) / (2*l1*l2))


#por algum motivo tive que alterar os sinais nessas duas linhas, petercorke me acuda
q1 = arctan2(y2,x2) + arctan2(l2*sin(q2),(l1+l2*cos(q2)))
q2 = -q2 #

q3 = o - (q2+q1)

print(f"q1 = {rad2deg(q1)}° \t q2 = {rad2deg(q2)}° \t q3 = {rad2deg(q3)}°")
'''
print("="*50)

q2 = -arccos((x2**2 + y2**2 - l1**2 - l2**2) / (2*l1*l2))
q1 = arctan(y2/x2) + arctan(l2*sin(q2)/(l1+l2*cos(q2)))

q3 = o + q2 - q1  

print(f"q1 = {rad2deg(q1)}° \t q2 = {rad2deg(q2)}° \t q3 = {rad2deg(q3)}°")

'''