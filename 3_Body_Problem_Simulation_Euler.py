from vpython import *

G = 1

#initial positions
Ax=.97000436
Ay=-.24308753
Bx=-.97000436
By=0.24308753
Cx=0
Cy=0

A = sphere(pos=vector(Ax,Ay,0), radius = 1/10, color=color.red,make_trail=True)
B = sphere(pos=vector(Bx,By,0), radius = 1/10, color=color.blue,make_trail=True)
C = sphere(pos=vector(Cx,Cy,0), radius = 1/10, color=color.yellow,make_trail=True)

#mass  1 is for flase-stable orbits. Keep Changing mass or other initial conditions in order to see unique, different and beautiful patterns

#A.m=1
#B.m=1
#C.m=1

#A.m = 1
#B.m = 1.1
#C.m = 1

A.m = .44
B.m = .87
C.m = 1

# initial momentum (mass*velocity)
A.p=A.m*vector(.93240737/2,.86473/2,0) 
B.p=B.m*vector(.93240737/2,.86473/2,0)
C.p=C.m*vector(-.93240737,-.86473146,0)

t = 0
tmax = 50
dt = .01

while t < tmax:
  rate(100)
  
  # compute relative positions
  rAB = B.pos - A.pos
  rAC = C.pos - A.pos
  rBC = C.pos - B.pos
  
  # compute forces
  FAB = -G*A.m*B.m*norm(rAB)/mag(rAB)**2 
  FAC = -G*A.m*C.m*norm(rAC)/mag(rAC)**2  
  FBC = -G*B.m*C.m*norm(rBC)/mag(rBC)**2  
  
  #update momentum
  A.p = A.p + (-FAB - FAC)*dt
  B.p = B.p + (FAB - FBC)*dt
  C.p = C.p + (FAC + FBC)*dt
  
  #update position
  A.pos = A.pos + A.p*dt/A.m
  B.pos = B.pos + B.p*dt/B.m
  C.pos = C.pos + C.p*dt/C.m
  
  t = t + dt
  print("time=",t)
  

  
  
  
