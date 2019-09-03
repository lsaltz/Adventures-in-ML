xVal = 10
rate = 0.2
precision = 0.000000001
stepSize = 1
maxIterations = 1000
iteration = 0
df = lambda x: 2*(x+5)
print("Iteration 0 \nX value is: ",xVal)
while stepSize > precision and iteration < maxIterations:
    xPrev = xVal
    xVal = xVal - rate * df(xPrev)
    stepSize = abs(xVal-xPrev)
    iteration = iteration + 1
    print("Iteration ",iteration,"\nX value is: ", xVal)
print("The local minimum occurs at", xVal)
