# Remote_coppeliasim
A Wrapper for remote api for coppelias sim in python.

This module wraps remote api of coppeliaSim for python as object implementation.
This is slower than c/c++ remote api, but can be useful planning tasks involving image processing.
Linux users can use pyrep by Stephen James https://github.com/stepjam/PyRep  , https://pyrep.readthedocs.io/. Its has better latency and gives complete control. 

Installation:
1) Copy paste the folder Remote_coppeliasim in your script folder.
2) You can also add it to path for importing it from anywhere
Then,<br/>
Open your scene in coppeliasim,<br/>

**Usage**
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
