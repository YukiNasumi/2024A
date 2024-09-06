import matplotlib.pyplot as  plt
import numpy as np
import math

def draw_rec(x_cd,y_cd):
    x_cd = list(x_cd)
    y_cd = list(y_cd)
    # 确保第一个点重复出现以闭合矩
    x_cd.append(x_cd[0])
    y_cd.append(y_cd[0])
    plt.plot(x_cd, y_cd, color='b', lw=2)  # 画矩形
    plt.scatter(x_cd, y_cd, color='r')  # 标记所有顶点
    plt.title('Rectangle with Given Four Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')

def fuc_x(theta,p=170):#确定螺距
    return p*theta*math.cos(theta)/(2*np.pi)
def fuc_y(theta,p=170):
    return p*theta*math.sin(theta)/(2*np.pi)
def distance(dot1,dot2):
    return math.sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)

theta = 0
d = 286
p = 55
eq = lambda t:distance((fuc_x(theta,p),fuc_y(theta,p)),(fuc_x(t),fuc_y(t)))-d
def distance_equation(vars):
    theta_1 = vars
    eq = distance((fuc_x(theta,p),fuc_y(theta,p)),(fuc_x(theta_1,p),fuc_y(theta_1,p)))-d
    return eq

from scipy.optimize import fsolve
def theta_seq(num_bench,theta0,distance,pitch):
    global p
    global d
    d = distance
    p = pitch
    seq = []
    seq.append(theta0)
    for _ in range(num_bench):
        global theta
        theta = seq[-1]
        next_theta = fsolve(distance_equation,theta+0.1).item()
        seq.append(next_theta)
    return seq


