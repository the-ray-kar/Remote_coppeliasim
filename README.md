# Remote_coppeliasim
Since coppeliasim has got python support now, this is not needed.

A Wrapper for remote api for coppelias sim in python.

This module wraps remote api of coppeliaSim for python as object implementation.
This is slower than c/c++ remote api, but can be useful for planning tasks involving image processing.
Linux users can use pyrep by Stephen James https://github.com/stepjam/PyRep  , https://pyrep.readthedocs.io/. Its has better latency and gives complete control. 

Installation:
1) Copy paste the folder Remote_coppeliasim in your script folder.
2) You can also add it to path for importing it from anywhere<br/>



## Usage
Open the scene (.ttt file) in coppeliaSim which you want to control, and then you can use the following methods,<br/>
**Note**: The folder Remote_coppeliasim should be present before opening any scene in order to load the bindings.
### Getting handles for objects and joints
```python
from Remote_coppeliasim.Rvrep import rvrep
rv = rvrep()

rv.start() # Remotely connect to coppeliasim
rv.start_sim() # start simmulation

link = rv.get_handle("shape","link0") #get object handle
pos = print(link.get_position())

joint = rv.get_handle("joint","revolute_1") #get joint
angle = 0.0 # in_rad
joint.set_position(angle)

rv.stop_sim() #stop simulation
rv.stop() #stop the connection.
```
### Example of controlling a manipulator to draw a circle
For more, see examples folder
```python
from Remote_coppeliasim.Rvrep import rvrep
import time
import math

rv = rvrep()

rv.start() # Remotely connect to coppeliasim
rv.start_sim() # start simmulation

ik_target = rv.get_handle("shape","IRB140_target") #get the ik_target handle as shape object

#draw a vertical circle in XZ plane for 10sec by moving ik_target or tip
start_time = time.time()
duration = 10
rotations = 2
omega = rotations*2*math.pi/duration
y = -0.075
r = 0.2 #radius
print(start_time)
while((time.time()-start_time)<duration): 
    t = time.time()
    x = -0.125+ r*math.cos(omega*t)
    z = 0.651+r*math.sin(omega*t)
    ik_target.set_position([x,y,z]) #move the IK target tip 

rv.stop_sim() #stop simulation
rv.stop() #stop the connection.
```
![recorded_path](https://user-images.githubusercontent.com/70949901/137765453-b47d44f3-fcf7-4693-93ea-031974e3ed50.gif)

