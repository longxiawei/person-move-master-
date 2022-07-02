# 导入包
import pandas as pd
import matplotlib.pyplot as plt
import time
from io import BytesIO
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
# 读取数据
data = pd.read_csv("60Activities-poseData.csv")
# print(data)
# ①获取所有列，并存入一个数组中
import numpy as np
data = np.array(data)
print(data[0])
# 绘制3维空间
# fig = plt.figure(figsize=(4,4))
# ax = fig.add_subplot(111, projection='3d')
for index in range(60):
    sport_name = data[index][0]
    if index == 0:
        azim = -16.5
        elev = -62

    print(sport_name)
    for i in range(1, len(data[index])):
        tmp = data[index][i][1:-1].split(',')
        data[index][i] = [float(x) for x in tmp]
    # print(data[0])
    xpos = []
    ypos = []
    zpos = []

    for i in range(1, len(data[index]), 3):
        xpos.append(data[index][i])
        ypos.append(data[index][i+1])
        zpos.append(data[index][i+2])
    xpos = np.array(xpos)
    ypos = np.array(ypos)
    zpos = np.array(zpos)
    # sleep
    #time.sleep(0.01)
    azim = -16.5
    elev = -62
    plt.ion()
    images=[]
    for i in range(len(xpos[0])):
        print("t = {}".format(i))
        plt.clf()  # 清除之前画的图
        fig = plt.gcf()  # 获取当前图
        ax = fig.gca(projection='3d')  # 获取当前轴
        ax.view_init(elev, azim)  # 设定角度
        print(azim,elev)
        ax.scatter(xpos[:,i],ypos[:,i],zpos[:,i])
        ax.plot(xpos[:,i][:6:2],ypos[:,i][:6:2],zpos[:,i][:6:2], 'r')
        ax.plot(xpos[:, i][1:6:2], ypos[:, i][1:6:2], zpos[:, i][1:6:2], 'y')
        ax.plot(xpos[:,i][6:12:2],ypos[:,i][6:12:2],zpos[:,i][6:12:2], 'g')
        ax.plot(xpos[:,i][7:12:2], ypos[:, i][7:12:2], zpos[:, i][7:12:2], 'b')
        ax.plot(xpos[:,i][[0,1,7,6,0]],ypos[:,i][[0,1,7,6,0]],zpos[:,i][[0,1,7,6,0]], 'deeppink')
        plt.title(sport_name)
        plt.axis([0, 0.8, 0, 0.8])
        ax.set_zlim(-1, 0.8)
        plt.pause(0.001)
        elev, azim = ax.elev, ax.azim  # 将当前绘制的三维图角度记录下来，用于下一次绘制（放在ioff()函数前后都可以，但放在其他地方就不行）
        plt.ioff()
        buf = BytesIO()
        fig.savefig(buf, bbox_inches='tight', pad_inches=0.0)
        images.append(Image.open(buf))
    print(images)
    images[0].save(str(index+1)+sport_name+'.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

    # ax.scatter(data[0][1],data[0][2],data[0][3])

