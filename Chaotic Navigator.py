import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#initializing the system constants, and initial state of the pendulums
g = 9.8
L1,L2 = 1.0, 1.5 #The length should match the display area described in the animation section
M1, M2 = 2,2
th1, th2 = np.pi/3,(np.pi/3) + 0.1 #theta 1 and theta 2 in radians
W1, W2 = 0.5,0.5  #angular velocities theta dot 1 and 2
Y = np.array([th1,th2,W1,W2])     #inital state vector

'''Defining the state derivative function.
   Note: We will not be using the Euler-Lagrange equations.
   That part will be an abstraction, since I derived by hand on pen-paper'''

def derivs (t,Y):
    th1,th2,W1,W2 = Y[0],Y[1],Y[2],Y[3]
    delta = th1-th2 
    a = M2*L1 * (W1**2) * np.sin(delta) * np.cos(delta)
    b = M2*g * np.sin(th2) * np.cos(delta)
    c = M2*L2 * (W2**2) * np.sin(delta)
    d = (M1+M2) * g * np.sin(th1)
    e = (M1+M2) * L1
    f = M2*L1 * (np.cos(delta)**2)
    num_1 = a+b+c-d
    denom_1 = e-f
    g_temp = -M2*L2 * (W2**2) * np.sin(delta) * np.cos(delta)
    h = (M1+M2) * ((g*np.sin(th1)*np.cos(delta)) - (L1*(W1**2) * np.sin(delta)) - g*np.sin(th2))
    i = (M1+M2) * L2
    k = M2*L2 * (np.cos(delta)**2)
    num_2 = g_temp+h
    denom_2 = i-k
    W1_dot = num_1/denom_1
    W2_dot = num_2/denom_2
    return np.array([W1,W2,W1_dot,W2_dot])

t_max = 111  # total time in seconds
fps = 60
num_frames = int(t_max * fps) + 1
evaluations = np.linspace(0, t_max, num_frames)
#solving the differential eqs
solutions = solve_ivp(fun = derivs,t_span = (0,t_max),y0 = Y,t_eval= evaluations)
#the solved numerical solutions of the differential equations
th1_sol = solutions.y[0, :]
th2_sol = solutions.y[1, :]
w1_sol = solutions.y[2, :]
w2_sol = solutions.y[3, :]

#coming back to the (x,y) coordinate :)
x1 = L1*np.sin(th1_sol)
y1 = -L1*np.cos(th1_sol)
x2 = L2*np.sin(th2_sol) + x1
y2 = -L2*np.cos(th2_sol) + y1

#onto the animation part :)
th1_deg = Y[0] * 180 / np.pi
th2_deg = Y[1] * 180 / np.pi
w1_rad = Y[2]
w2_rad = Y[3]
initial_conditions_text = (
    f"Initial Conditions:\n"
    f"  $\\theta_1$: {th1_deg:.1f}°\n"  # :.1f rounds to 1 decimal place
    f"  $\\theta_2$: {th2_deg:.1f}°\n"
    f"  $\\omega_1$: {w1_rad} rad/s\n"
    f"  $\\omega_2$: {w2_rad} rad/s\n"
    f"  M1={M1} Kg, M2={M2}Kg"
)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-3.5, 3.5)  # Sets the x-axis limits
ax.set_ylim(-3.5, 3.5)  # Sets the y-axis limits
ax.set_title("Chaotic Pendulum")
ax.grid()
ax.text(
    0.02, 0.98,  # x, y coordinates (2% from left, 98% from bottom)
    initial_conditions_text,  # The string we just made
    transform=ax.transAxes,   # Use axes coordinates, not data coordinates
    fontsize=8,
    verticalalignment='top',  # Anchor the text from its top edge
    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5) # A nice box
)

#creating the objects for animation, with empty data
line, = ax.plot([], [], 'o-', lw=2, color='blue') # The pendulum arms
trail, = ax.plot([], [], '-', lw=1, color='red', alpha=0.5) # The trail

def animate(A):
    line.set_data([0, x1[A], x2[A]], [0, y1[A], y2[A]])
    trail.set_data(x2[:A], y2[:A])
    return line, trail
#time for the director to intervene
ani = animation.FuncAnimation(fig, animate, frames=len(x1), interval=1000/fps, blit=True)
if (len(evaluations)>len(x1)):
    print("Initial conditions too chaotic. DE approximation error")
    print("creating and saving animation with frames just before breakdown.")
print("Saving animation... This may take a few moments.")
ani.save('Chaotic Navigator.mp4', writer='ffmpeg', fps=fps)
print("Animation successfully saved")
print("Displaying animation...")
plt.show()