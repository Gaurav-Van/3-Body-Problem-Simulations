from vpython import *
from numpy import *

t0 = 0.
tf = 2000. # Start and end time

# time and step size for Runge-Kutta Method
t = t0 
h = 0.05

n = 18 # Number of components for y and force function

r1 = array([10., 0., 0.])
v1 = array([-0.1, 0., 0.1])
m1 = 1.

r2 = array([-10., 0., 0.])
v2 = array([0., 0.1, -0.1])
m2 = 1.

r3 = array([0., 0., 5.])
v3 = array([0.2, -0.1, 0.])
m3 = 1.

y = concatenate((r1,r2,r3,v1,v2,v3))

scene = canvas(x=0,y=0,width = 700, height = 700)
path1 = curve(color = color.blue, radius = 0.13)
path2 = curve(color = color.red, radius = 0.13)
path3 = curve(color = color.green, radius = 0.13)
body1 = sphere(pos = vec(r1[0],r1[1],r1[2]), color = color.blue, radius = 0.5*m1**(1/3))
body2 = sphere(pos = vec(r2[0],r2[1],r2[2]), color = color.red, radius = 0.5*m2**(1/3))
body3 = sphere(pos = vec(r3[0],r3[1],r3[2]), color = color.green, radius = 0.5*m3**(1/3))

def f(t, y): # Force function
    r12 = ((y[0]-y[3])**2+(y[1]-y[4])**2+(y[2]-y[5])**2)**(1/2)
    r23 = ((y[3]-y[6])**2+(y[4]-y[7])**2+(y[5]-y[8])**2)**(1/2)
    r31 = ((y[6]-y[0])**2+(y[7]-y[1])**2+(y[8]-y[2])**2)**(1/2)
    return concatenate((y[9:18],
                m2*(y[3:6]-y[0:3])/r12**3+m3*(y[6:9]-y[0:3])/r31**3,
                m1*(y[0:3]-y[3:6])/r12**3+m3*(y[6:9]-y[3:6])/r23**3,
                m1*(y[0:3]-y[6:9])/r31**3+m2*(y[3:6]-y[6:9])/r23**3))

def rk4(t, h): # Runge-Kutta algorithm
    ydumb = zeros(n, float)
    k1 = zeros(n, float)
    k2 = zeros(n, float)
    k3 = zeros(n, float)
    k4 = zeros(n, float)

    for i in range(n):
        k1[i] = h*f(t,y)[i]
    for i in range(n):
        ydumb[i] = y[i] + k1[i]/2.
    k2 = h*f(t+h/2., ydumb)
    for i in range(n):
        ydumb[i] = y[i] + k2[i]/2.
    k3 = h*f(t+h/2., ydumb)
    for i in range(n):
        ydumb[i] = y[i] + k3[i]
    k4 = h*f(t+h, ydumb)
    for i in range(n):
        y[i] = y[i] + (k1[i] + 2.*(k2[i] + k3[i]) + k4[i])/6.
    return y

while t < tf:
    rate(500)
    y = rk4(t,h)
    t += h
    body1.pos = vec(y[0], y[1], y[2])
    body2.pos = vec(y[3], y[4], y[5])
    body3.pos = vec(y[6], y[7], y[8])
    path1.append(pos = vec(y[0], y[1], y[2]))
    path2.append(pos = vec(y[3], y[4], y[5]))
    path3.append(pos = vec(y[6], y[7], y[8]))

