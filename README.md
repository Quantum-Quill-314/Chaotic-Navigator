# Chaotic-Navigator
What This Project Does:
This project models and visualizes the motion of a double pendulum, a classic, deterministic system that exhibits profound chaotic behavior.It translates the underlying physics into a compelling visual animation. The script performs a full, end-to-end simulation by:
Defining the System: Using Lagrangian mechanics ($L = T - U$), the script implements the two coupled, second-order ordinary differential equations (ODEs) that govern the pendulum's motion.
Solving Numerically: It leverages the SciPy library (solve_ivp) to numerically integrate this complex system of ODEs, calculating the pendulum's angular position and velocity at thousands of discrete time steps.
Visualizing the Chaos: Using Matplotlib, it generates a dynamic animation of the pendulum swinging. It plots both the moving arms and the intricate, never-repeating "ghost" trail of the second bob, which clearly illustrates the system's chaotic nature.
# Requirements to Run:
Python 3.7+
NumPy: For high-performance array operations and numerical functions.
SciPy: For the solve_ivp differential equation solver.
Matplotlib: For creating and managing the 2D plot and animation.
External Software (Optional: For Saving Video)
FFmpeg: This is a non-Python utility that Matplotlib requires to write video files (like .mp4). It must be downloaded and added to your system's PATH.


If you do not wish to save the animation and want to bypass the FFmpeg requirement, simply comment out or delete the ani.save(...) line in the script. The plt.show() command will still display the live animation.

# Customization & Renders
You can easily generate your own unique animations by modifying the initial parameters at the top of the script. The system's behavior is highly sensitive to these values. 
<img width="931" height="189" alt="image" src="https://github.com/user-attachments/assets/96b0eff3-6b5e-4588-a935-e2a133665914" />

By changing the lengths (L1, L2), masses (M1, M2), or (most effectively) the starting angles and velocities (th1, th2, W1, W2), you will produce a completely different chaotic path.
