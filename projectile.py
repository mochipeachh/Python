from math import pi, tan, cos

# Barrel height is in metres
initialBarrelHeight = 1

# Distance is in metres
horizontalDistance = 0.5

# Gravity is metres per second squared
gravity = 9.81

# Velocity is metres per second
velocity = 44

# Angle is in degrees
angleInDegrees = 80

# Angle conversion from degrees to radians
angleInRadians = angleInDegrees * (pi/180)

result = initialBarrelHeight + horizontalDistance*tan(angleInRadians) - (gravity*horizontalDistance**2)/(2*(velocity*cos(angleInRadians))**2)

print(result)





