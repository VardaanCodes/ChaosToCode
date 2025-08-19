<!-- @format -->

# Mathematics/Physics behind the code

This thing was taught to us in PH1010. We work our way up from a simple harmonic oscillator to a damped harmonic oscillator.

1. First, we face a simple harmonic oscillator, which is described by the equation:
   $$
   \ddot{x} + \omega_n^2 x = 0
   $$
   where $ \ddot{x} $ is the second derivative of $ x $ with respect to time, and $ \omega_n $ is the angular frequency. Usually, $ \omega_n $ is defined as $ \omega_n = \sqrt{\frac{k}{m}} $, where $ k $ is the spring constant, and $ m $ is the mass of the block.
   Solving this equation gives us the solution:
   $$
   x(t) = A \cos(\omega_n t + \phi)
   $$
2. We introduce an external constant force $ F $, gravity for example, acting on the system, which modifies the equation to:
   $$
   \ddot{x} + \omega_n^2 x = F(t)
   $$
   This is basically the same as above, except for a different equilibrium position, and thus different initial conditions(ICS). The solution is not to different from the previous one, except for a shift in the equilibrium position.
3. We then introduce damping, which is a force that opposes the motion of the system, and is proportional to the velocity. This gives us the equation:
   $$
   \ddot{x} + 2 \zeta \omega_n \dot{x} + \omega_n^2 x = 0
   $$
   If the damping force is considered $-bv$ with $b$ as damping coefficient, we have $\zeta = -\frac{b}{2m}$
4. Now, we remove damping, and apply an external force $ F(t) $, which gives us the equation:
   $$
   \ddot{x} + 2 \zeta \omega_n \dot{x} + \omega_n^2 x = F(t)
   $$
   If this $F(t)$ is sinosuidal periodic, with $F(t) = F_d\cos(\omega_d t)$ This is the equation we solve in this code. The solution is:
   $$
   x(t) = A e^{-\zeta \omega_n t} \cos(\omega_d t + \phi)
   $$
   where $ \omega_d = \sqrt{\omega_n^2 - \zeta^2} $ is the damped angular frequency.
