#######################################
#         Rotate the axis
#       Input file : CONTCAR
#        Output file : newcontcar
#   Date : 2019
# Author : yan0746
#######################################
import  numpy as np
import  math


np.set_printoptions(suppress=True,precision=15)

#Read data from contcar
def read_CONTCAR():
    rf=open('CONTCAR','r')
    lines=rf.readlines()
    rf.close()
    x1 = np.array([float(lines[2].split()[0]),float(lines[2].split()[1]),float(lines[2].split()[2]),1.0])
    y1 = np.array([float(lines[3].split()[0]),float(lines[3].split()[1]),float(lines[3].split()[2]),1.0])
    z1 = np.array([float(lines[4].split()[0]),float(lines[4].split()[1]),float(lines[4].split()[2]),1.0])
    return x1, y1, z1

#Rotate around the  axis
def rotate_z_axis(x1,y1,z1,radio_z):
    axis_z = np.array([[math.cos(math.radians(radio_z)), math.sin(math.radians(radio_z)), 0, 0],
                       [-math.sin(math.radians(radio_z)), math.cos(math.radians(radio_z)), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    new_x1= np.dot(x1, axis_z)
    new_y1= np.dot(y1, axis_z)
    new_z1= np.dot(z1, axis_z)
    return new_x1, new_y1, new_z1

def rotate_x_axis(x1,y1,z1,radio_x):
    axis_x = np.array([[1, 0, 0, 0],
                       [0, math.cos(math.radians(radio_x)), math.sin(math.radians(radio_x)), 0],
                       [0, -math.sin(math.radians(radio_x)), math.cos(math.radians(radio_x)), 0],
                       [0, 0, 0, 1]])
    new_x1= np.dot(x1, axis_x)
    new_y1= np.dot(y1, axis_x)
    new_z1= np.dot(z1, axis_x)
    return new_x1,new_y1,new_z1

def rotate_y_axis(x1,y1,z1,radio_y):
    axis_y = np.array([[math.cos(math.radians(radio_y)), 0, -math.sin(math.radians(radio_y)), 0],
                       [0, 1, 0, 0],
                       [math.sin(math.radians(radio_y)), 0, math.cos(math.radians(radio_y)), 0],
                       [0, 0, 0, 1]])
    new_x1= np.dot(x1, axis_y)
    new_y1= np.dot(y1, axis_y)
    new_z1= np.dot(z1, axis_y)
    return new_x1,new_y1,new_z1

def merge_xyz(x1,y1,z1):
    m1= np.vstack((x1,y1,z1))
    m2=np.delete(m1,3,axis=1)
    return m2

def write_new_contcar(marit):
    rf=open('CONTCAR','r')
    wf=open('newcontcar.vasp','w')
    lines=rf.readlines()
    for i in lines[0:2]:
        wf.write(i)
    #Write the data
    for j in range(0,3):
        for i in range(0,3):
            wf.write('    ')
            print(marit[j,i])
            wf.write(str(marit[j,i]))
        wf.write('\n')


    for i in lines[5:]:
        wf.write(i)
    wf.close()
    rf.close()


if __name__=="__main__":
    x1,y1,z1=read_CONTCAR()
    x1,y1,z1=rotate_x_axis(x1,y1,z1,55.476)
    #x1,y1,z1=rotate_z_axis(x1,y1,z1,44.971)
    alm=merge_xyz(x1,y1,z1)
    print(alm)
