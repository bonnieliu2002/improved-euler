import math

# consider the differential equation 
# for a given x and y, return v 
def f(x, y): 
    # v = dy/dx
    v = math.exp(-1*y);
    return v;

def euler(x, y, h):
    return y + h * f(x,y)

def improved_euler(x, y, h):
    return y + h / 2 * (f(x, y) + f(x + h, euler(x, y, h)))
    
def printFinalValues(x, xn, y, h):
    x1 = x
    y1 = y
    while (x1 < xn):
        y1 = improved_euler(x1, y1, h)
        x1 = x1 + h
        
    # at every iteration first the value 
    # of for next step is first predicted 
    # and then corrected.
    print("The approximate value of y at x =", xn, "is :", y1)
  
# Driver Code 
if __name__ == '__main__': 
      
    # here x and y are the initial 
    # given condition, so x=0 and y=0.5 
    x = 0
    y = 0
    # final value of x for which y is needed 
    xn = 0.6
    
    # step size 
    h = 0.05
    
    printFinalValues(x, xn, y, h)
    
# This code is contributed by Rajput-Ji and modified by Bonnie Liu
