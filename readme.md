  这是我研一的时候，用python写的一个脚本,
可以旋转坐标轴
似乎没什么用处
需要POSCAR文件，
算完后会输出直接在屏幕输出新的x,y,z坐标
使用方法： 在文件夹中同时有CONTCAR 和本result.py
执行 ./result.py

if __name__=="__main__":
    x1,y1,z1=read_CONTCAR()
    x1,y1,z1=rotate_x_axis(x1,y1,z1,55.476)
    #x1,y1,z1=rotate_z_axis(x1,y1,z1,44.971)	
    alm=merge_xyz(x1,y1,z1)
    print(alm)
