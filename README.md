Unconstrained Growth
====================

This learning module accompanies chapter two of Angela B. and George W Shiflet's
book [Introduction to Computational Science](https://ics.wofford-ecs.org/).
Here, we introduce and develop our ability to:
- Define and use functions in Python.
- Use Jupyter Notebooks to develop and document problem solving process and solution.
- Use Matplotlib to generate good plots.
- Analyze simulation error.

The assignment below will help you as you develop these abilities. Try and
complete the assignment on your own or with guided help from a classmate and/or
instructor. If you need help, you may reference the notebook [Unconstrained
Growth Solution](UnconstrainedGrowthSolution.ipynb) which contains a solution to
the assignment. Also, the module
[UnconstrainedGrowthSolution.py](UnconstrainedGrowthSolution.py) has code to
model unconstrained exponential growth using finite difference techniques.
**Only use these documents if you are completely stuck. You will learn best if
you complete the assignment without looking at the solutions.** These documents
are provided so you can consult them if absolutly necessary.

Assignment
----------

Investigate solving dP/dt=rP using numerical methods

-   Write a python
    [function](https://docs.python.org/tutorial/controlflow.html#defining-functions)
    that uses finite difference methods to simulate the population growth. Like
    the example in your text, use P\_0=100, r=0.1 and a time step size of 0.005,
    Δt=0.005. You may want to write out pseudo code before you write in python.
    Your function should:

    -   Take at least the time step size, dt, as a passed parameter.

    -   Use a loop structure to create a
        [list](https://docs.python.org/tutorial/introduction.html#lists) of time
        and population. *Note: I used a* [while
        loop](https://www.tutorialspoint.com/python/python_while_loop.htm)*.
        Also, I found it easier to plot the values if I stored the time values
        in one list and the population values in another list.*

    -   Return the lists from the function. *Note: I called my function grow.
        The last line of my function is* `return t_array, population_array`*. I
        then call the function and get the results with* `t, p = grow(0.005)`*.*

-   Using the Juppyter notebook [Unconstrained
    Growth.ipynb](UnconstrainedGrowth.ipynb) which has some starter code:

    -   plot your simulation results for population vs. time. Add an appropriate
        title and axis labels to this graph.

    -   In your previous graph, have the population data displayed with red
        hexagon markers with a transparent face. You might want to check the
        [matplotlib documentation for
        plot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot).
        Also, setting the color alpha value to zero will make the marker
        transparent as described on [this stackoverflow
        discussion](http://stackoverflow.com/questions/15928539/matplotlib-how-to-make-the-marker-face-color-transparent-without-making-the-li).

    -   On a single graph, have plots for the population vs time for different
        time step sizes, Δt. Create at least four different plots with Δt values
        ranging from 0.005 to 1.

    -   Create a plot of the simulation error vs time for the simulations you
        created in the previous step. Note that the simulation error is the
        difference between the exact value and the simulation value. For this,
        you may want to look at the [range
        function](https://docs.python.org/3.5/tutorial/controlflow.html#the-range-function)
        in python.
