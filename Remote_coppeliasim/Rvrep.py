try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
import os

class rvrep:
    
    def __init__(self) -> None:
        self.filename = None
        self.simx = sim
        self.connected = False
        self.clientID = -2

    def start(self,filename=None):
        self.filename = filename
        if(not filename):
            print("File name not specified looking for already started scenes")
        else:
            os.system("start "+self.filename)
        print("Closing initial connections incase")
        self.simx.simxFinish(-1) # just in case, close all opened connections
        print("Attempting connection")
        clientID=self.simx.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim
        self.clientID = clientID
        if(clientID!=-1):
            self.connected = True
            print ('Connected to remote API server')
            res,objs=self.simx.simxGetObjects(clientID,sim.sim_object_shape_type,sim.simx_opmode_blocking)
            if res==sim.simx_return_ok:
                print ('Number of objects in the scene: ',len(objs))
            else:
                print('Remote API function call returned with error code: ',res)
        else:
            print("Failed connecting, server ain't on or incorrect port")
            return False
        return True

    def stop(self):
        print("closing connection")
        if(self.clientID<0):
            print("Client not connected or connection already down")
            return False
        self.simx.simxFinish(self.clientID) #close connection
        print("Connection closed")
        return True

    def start_sim(self):
        if(not self.connected):
            print("client not connected")
            return False
        self.simx.simxStartSimulation(self.clientID,sim.simx_opmode_blocking)
    
    def pause_sim(self):
        if(not self.connected):
            print("client not connected")
            return False
        self.simx.simxPauseSimulation(self.clientID,sim.simx_opmode_blocking)
    
    def stop_sim(self):
        if(not self.connected):
            print("client not connected")
            return False
        self.simx.simxStopSimulation(self.clientID,sim.simx_opmode_blocking)

    def get_handle(self,object_type=str(""),object_name=""):
        if(not object_type):
            print("object not specified")
            return None
        
        if(object_type=="shape"):
            return shape(rv=self,shape_name=object_name)







class shape:
    def __init__(self,rv=None,shape_name=None) -> None:

        if(not shape_name or not rv.simx):
            print("Name not specified or simulation")
            return None
        self.name = shape_name
        rcode,handle = rv.simx.simxGetObjectHandle(rv.clientID,shape_name,rv.simx.simx_opmode_blocking)
        if(rcode!=0):
            print("Cannot find object named",shape_name)
            return None
        self.handle = handle
        self.rv = rv

    def get_position(self,relative_to=-1):
        if(relative_to!=-1):
            relative_to = relative_to.handle
        rcode,position = self.rv.simx.simxGetObjectPosition(self.rv.clientID, self.handle,relative_to, self.rv.simx.simx_opmode_blocking) 
        if(rcode==0):
            return position
        else:
            return None
    
    def set_position(self,position,relative_to=-1):
        if(relative_to!=-1):
            relative_to = relative_to.handle
        self.rv.simx.simxSetObjectPosition(self.rv.clientID, self.handle,relative_to, position, self.rv.simx.simx_opmode_blocking) 
    
    
    def get_orientation(self,relative_to=-1):
        if(relative_to!=-1):
            relative_to = relative_to.handle
        rcode,orientation = self.rv.simx.simxGetObjectOrientation(self.rv.clientID, self.handle,relative_to, self.rv.simx.simx_opmode_blocking) 
        if(rcode==0):
            return orientation
        else:
            return None

    def set_orientation(self,orientation,relative_to=-1):
        if(relative_to!=-1):
            relative_to = relative_to.handle
        self.rv.simx.simxSetObjectOrientation(self.rv.clientID, self.handle,relative_to, orientation, self.rv.simx.simx_opmode_blocking) 

    def collision_detect(self,with_object):
        return self.rv.simx.simxCheckCollision(self.rv.clientID,self.handle,with_object.handle,self.rv.simx.simx_opmode_blocking)[1]


class joint:

    def __init__(self,rv=None,joint_name=None) -> None:

        if(not joint_name or not rv.simx):
            print("Name not specified or simulation")
            return None
        self.name = joint_name
        self.opmode = rv.simx.simx_opmode_blocking
        rcode,handle = rv.simx.simxGetObjectHandle(rv.clientID,joint_name,self.opmode)
        if(rcode!=0):
            print("Cannot find object named",joint_name)
            return None
        self.handle = handle
        self.rv = rv

    

    def set_position(self,position):
        self.rv.simx.simxSetJointPosition(self.rv.clientID,self.handle,position,self.opmode)
        return True

    


        


        
    

            
    
            
        

    
        


        
        

        

    




