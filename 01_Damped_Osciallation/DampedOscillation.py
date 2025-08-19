import sympy as smp
import numpy as np
import matplotlib.pyplot as plt

# constants zeta, omega
zeta, omega = smp.symbols("\zeta \omega_n", positive=True, real=True)

# variable t
t = smp.symbols("t", real=True, positive=True)

# Functions x(t), F(t).
x = smp.Function("x")(t)
F = smp.Function("F")(t)

dot_x = smp.diff(x, t)
ddot_x = smp.diff(x, t, 2)


def dsol(F):
    '''
    Function to solve our differential equation of damped oscillation
    '''
    lhs = ddot_x + (2 * zeta * omega * dot_x) + (omega**2) * x
    eqn2 = smp.Eq(lhs, F)
    initconds = {
        x.subs(t, 0): 1,
        dot_x.subs(t, 0): 0,
    }

    # Assume the motion is constrained between 0 and 1(x is instead x/L)
    # And timeperiod of 4 seconds
    return smp.dsolve(eqn2, x, ics=initconds)


def main(zeta_const: int, omega_const: int, t_range: int, Forcem=smp.sin(t)) -> None:
    const = [(zeta, zeta_const), (omega, omega_const)]
    solicsk = dsol(Forcem).subs(const)

    solutionics_num = smp.lambdify(t, solicsk.rhs)
    t_num = np.linspace(0, t_range, 1000)
    solicsk_t = (solutionics_num(t_num))

    # Turns out our dear sympy cant make use of the fact e^in + e^-in = 2 cos n
    # In evaluation, its returning some negligible imaginary part.
    # Since we know our solution needs to be real, we can ignore the imaginary part
    # So that pyplot can plot it properly
    # If you feel that I am scamming you, uncomment this part of the code and check it for yourself
    
    # print("Original symbolic solution:")
    # print(solicsk.evalf())
    # print(f"Max imaginary part: {np.max(np.abs(np.imag(solicsk_t)))}")

    solicsk_t = np.real(solicsk_t)
    plt.plot(t_num, solicsk_t)

    plt.axhline(0, color='black', linestyle='-', linewidth=1.2)
    plt.axvline(0, color='black', linestyle='-', linewidth=1.2)

    # x limit of amplitude
    plt.plot([0, t_num[-1]], [1, 1], linestyle='--')
    for i in range(int(t_num[-1] // omega_const)):
        # Also, to make lines dotted and fading, use linestyle=':', and alpha for fading.
        plt.plot(
            [omega_const * (i + 1), omega_const * (i + 1)],
            [np.min(solicsk_t), np.max(solicsk_t)],
            linestyle=':',
            color='gray',
            # alpha=1.0 - (i / int(t_num[-1] // 4)),
            linewidth=1.2
        )
    plt.xlabel("t")
    plt.ylabel("x(t)")

    plt.show()


main(zeta_const = 0.1,omega_const = 3,t_range = 80,Forcem = smp.sin(0.1*t))
