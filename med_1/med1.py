"""
MEDIUM PROBLEM 1:
Given the rover's position (x, y, z) and orientation angles (a, b, g) in degrees, 
and the coordinates of a point in the camera frame (x_cam, y_cam, z_cam), 
compute the world frame coordinates of that point.
"""
import numpy as np  # For matrix operations

#Rotation matrices for roll (a), pitch (b), and yaw (g), each along x , y, and z axes respectively
def Rx(a): 
    a = np.radians(a)
    return np.array([[1,      0,       0    ],
                     [0,  np.cos(a), -np.sin(a)],
                     [0,  np.sin(a),  np.cos(a)]])

def Ry(b): 
    b = np.radians(b)
    return np.array([[ np.cos(b), 0, np.sin(b)],
                     [     0,     1,     0    ],
                     [-np.sin(b), 0, np.cos(b)]])

def Rz(g): 
    g = np.radians(g)
    return np.array([[np.cos(g), -np.sin(g), 0],
                     [np.sin(g),  np.cos(g), 0],
                     [    0,          0,     1]])

#Obtaining user input for rover coordinates, orientation angles, and camera frame coordinates
x , y, z = map(float, input("Enter rover coordinates (x y z): ").split())                                  #rover position in world frame
a, b, g = map(float, input("Enter rover orientation angles (a b g in degrees): ").split())                 #roll, pitch, yaw angles in degrees
x_cam ,y_cam, z_cam = map(float, input("Enter point coordinates in camera frame (x y z): ").split()) #point coordinates in camera frame

R = Rz(g) @ Ry(b) @ Rx(a)    #Combined rotation matrix from roll, pitch, and yaw
camera_coords = np.array([x_cam, y_cam, z_cam])
Rover_frwd = np.array([x, y, z]) 

world_coords = (R @ camera_coords) + Rover_frwd  #forward kinematics to get world frame coordinates
print("World frame coordinates:", world_coords)