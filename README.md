# Three-Body-Problem-Simulations
This repository includes two Python scripts for simulating the three-body problem, a classical problem in celestial mechanics involving the gravitational interactions between three bodies.

## Scripts

### 3_Body_Problem_Simulation_RK4.py

This script uses the Runge-Kutta 4th Order (RK4) method to solve the equations of motion. RK4 is a higher-order numerical integration technique that provides high accuracy by considering multiple intermediate steps to calculate the next state of the system. This method is suitable for precise simulations over longer time periods and effectively handles the complex dynamics of the three-body problem.

### 3_Body_Problem_Simulation_Euler.py

This script employs the Euler method for numerical integration. The Euler method is a simpler technique that updates positions and velocities based on the current state and a straightforward approximation of the system's dynamics. While easier to implement, it is less accurate compared to RK4, especially over longer time spans. This method provides a basic yet functional approach to simulate the interactions between the three bodies.

## Assumptions

- **Newtonian Gravity**: Both simulations assume that the gravitational force between bodies follows Newton's law of universal gravitation. This law states that the force of attraction is proportional to the product of the masses and inversely proportional to the square of the distance between them.

- **Point Masses**: The bodies are treated as point masses, which simplifies the problem by ignoring their actual size and shape. This assumption focuses solely on their gravitational interactions and avoids additional complexities.

- **No External Forces**: The simulations assume no external forces other than the mutual gravitational attraction between the bodies. This means the only forces considered are those exerted by the bodies on each other.

- **Closed System**: The system is considered closed, meaning that the total momentum and energy are conserved throughout the simulation. No energy is lost or gained from outside sources.

- **Complexity with Unequal Masses**: While the simulations use point masses for simplicity, it's important to note that unequal masses would result in varying gravitational forces, adding complexity to the interactions. However, the chaotic nature of the three-body problem remains inherent, as this sensitivity to initial conditions and complex dynamics is a fundamental aspect regardless of mass equality.

## Result 

### 3_Body_Problem_Simulation_RK4.py

![RK4](https://github.com/user-attachments/assets/6a98db79-d652-4123-b30e-6eec5075b89f)

### 3_Body_Problem_Simulation_Euler.py
`Simulation when Initial conditions in this file is used`

![Euler 2](https://github.com/user-attachments/assets/74299644-ae30-43c3-8939-8e8f416213f3)

`Initial Conditions used to get this following beautiful pattern`
``` python
Ax=-1.2
Ay=0
Bx=1
By=0
Cx=0
Cy=0

A.m = .44
B.m = .87
C.m = 1

# initial momentum (mass*velocity)
A.p=A.m*vector(0, -.992852, 0)
B.p=B.m*vector(0, -.513024, 0)
C.p=C.m*vector(0, .882922, 0)
```

![Euler (1)](https://github.com/user-attachments/assets/85bd60c4-7d07-408f-aa61-e75a2213948d)


## References

For a deeper understanding of the mathematical concepts and the three-body problem, consider exploring the following resources:

- https://youtu.be/UC40kDpAI8M?feature=shared
- https://youtu.be/YHHVkUrg4_M?feature=shared
- https://blbadger.github.io/3-body-problem.html
- https://arxiv.org/pdf/1303.0181
- https://arxiv.org/pdf/1709.04775
- https://medium.com/@2305sakake/visually-simulating-the-three-body-problem-on-python-136d3667c820

## Running the Simulations

1. Ensure Python is installed.
2. Install necessary packages: `vpython`, `numpy`.
3. Run the desired script using:
   ```bash
   python3 3_Body_Problem_Simulation_RK4.py
   ```
   or
   ```bash
   python3 3_Body_Problem_Simulation_Euler.py
   ```
