import math


def grow(dt):
    """Calculates the population vs time for given parameters."""

    rate = 0.1
    p0 = 100
    SimulationLength = 100

    population = p0
    t = 0
    t_array = [0]
    population_array = [p0]

    rdt = rate*dt
    while t < SimulationLength:
        population += rdt * population
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)
    return t_array, population_array