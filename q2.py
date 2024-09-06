from matplotlib import pyplot as plt
import numpy as np
import draw


d_head = 341-55
d_bench = 220-55
p = 55
def draw_bench(theta0):
    seq1 = draw.theta_seq(1,theta0,d_head,55)
    seq2 = draw.theta_seq(222,seq1[-1],d_bench,55)
    seq = seq1[:1]+seq2
    return seq

def draw_spiral(ax):
    num_turns = 5    # Number of turns in the spiral
    theta_max = 2 * np.pi * num_turns  # Angle for the number of turns
    pitch = 55        # Distance between consecutive loops

# Generate points for the spiral
    theta = np.linspace(0, theta_max*2, 100000)
    r = pitch * theta / (2 * np.pi)


# Plotting the spiral
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color='b', lw=0.2,label = 'in')  
    #ax.plot(-x,-y,color='r',lw=0.2,label='out')
    #plt.plot([fuc_x(t) for t in seq][:],[fuc_y(t) for t in seq][:],lw=0.5,label='bench')
#plt.plot(circle_x,circle_y,color='y',label='turning zone')
   


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_xlim(-1000,1000)
ax.set_ylim(-1000,1000)
thetas = np.linspace(0,10*2*draw.math.pi,100)
for i,t in enumerate(thetas):
    seq = draw_bench(t)
    draw_spiral(ax)
    ax.plot([draw.fuc_x(t,p) for t in seq],[draw.fuc_y(t,p) for t in seq],lw=5,label='bench')
    ax.set_title('{}'.format(i))
    plt.grid()
    plt.pause(0.1)
    if t==thetas[-1]:
        plt.savefig('q2.png')
        plt.show()
    ax.clear()
