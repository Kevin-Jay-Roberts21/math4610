# Math 4610 Root Finding Problem: Secant Method

**Routine Name:**           explicit_euler_logistic

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** To conduct an approximate solution of the initial value problem of the logistic equation using
the explicit euler method. Th purpose is to approximate the solution using derivatives without actually calculating the
solution.

**Input:** The inputs are alpha a, beta b, P0 (initial condition), an initial time t0, the logistic equation f, a final time T, and n.

**Output:** This routine outputs the approximation of the logistic equation at the finaly time step T. It also outputs the
graph of the logistic equation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following:

      a = 0.2
      b = 0.0005
      P0 = 10.0
      explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)

Output from the lines above give a final approximation at T and a graph of the function:

      Final Approximation: 0.13607479095833241

Graph for a = 0.2: [graph](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/homework4_images/fig1.png)

I've computed the same for different alpha and beta values as well:

Input:

      a = 0.01
      b = 0.0005
      P0 = 10.0
      explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
      a = 2.0
      b = 0.0005
      P0 = 10.0
      explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)

Output:

      Final Approximation: 0.00045465986240039724
      Final Approximation: 0.2940624089205812

Graph for a = 0.01: [graph](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/homework4_images/fig2.png)

Graph for a = 2.0: [graph](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/homework4_images/fig3.png)

The code is at the bottom of this software manual. Let's go through it now in depth:

First and foremost, we must initialize variables. We initialize a tvals array and an xvals array so that we can create a
plot. These array store the logistic approximation at a certain time t0. We then initalize h, and P0, and add them into
the arrays. We then approximate an initial value for the logistic equation, f0. Finally, we start the for loop which will
run through n iterations. In the loop we compute the next time step, and then the next corresponding P0 value. Then add
them into the arrays. Then we redefine the time step t0 and the P0 value. Finally, we redefine the approximated logistic
function f0. After the loops ends, we create a plot fo the tvals and teh xvals and show this plot. Thus, this function returns
a final value at T, and a graph of all the values.

**Implementation/Code:** The following is the code for explicit_euler_logistic()

    def explicit_euler_logistic(a, b, P0, t0, f, T, n):

        # intialize variables
        tvals = []
        xvals = []

        h = (T - t0)/n
        P = P0

        tvals.append(t0)
        xvals.append(P0)

        f0 = float(eval(f))
        for i in range(1, n):
            t1 = t0 + h
            P1 = P0 + (h * f0)
            tvals.append(t1)
            xvals.append(P0)
            t0 = t1
            P0 = P1
            P = P0
            f0 = float(eval(f))

        plt.plot(tvals, xvals)
        plt.show()

        print("Final Approximation: " + str(f0))

**Last Modified:** October/2022