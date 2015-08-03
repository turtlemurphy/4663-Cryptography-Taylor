###############################################
# Name: Taylor Murphy
# Class: CMPS 4663 Cryptography
# Date: 2 August 2015
# Program 3 - Elliptical Curve Encryption
###############################################

import argparse
import numpy as np
import matplotlib.pyplot as plt

def slope(x1, y1, x2, y2, a):
    
    #Get the slope of the line
    if ((x1 == x2) & (y1 == y2)):
        #If P & Q are the same point the use the equation for the 
        #derivative (dy/dx) = ((3x^2 + a) / (2y)) to find the tangent line 
        #at that point 
        slope = float((3 * pow(x1, 2) + a) / (2 * y1))
    else:
        #Else use standard formula for slope
        slope = (y1 - y2) / (x1 - x2)        
    
    return slope
    
def IsOnECurve(a, b, x, y):
    #If point(x, y) is on curve represented by (a, b) then goodPoint is true   
    if (pow(y, 2) == pow(x, 3) + (a * x) + b):
        goodPoint = 1
    #Else goodPoint is false
    else:
        goodPoint = 0
    
    return goodPoint 

def plotter(a, b, m, x1, y1, x2, y2, x3, y3):
    #Determines width and height of plot
    h = max(y1, y2, y3) + 20 
    w = max(x1, x2, x3) + 20

    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    plt.annotate("Taylor Murphy", xy = (-w + 2, h - 2), xycoords = "data", va = "center", ha = "center", bbox = dict(boxstyle = "round", fc = "w"))

    # This creates a mesh grid with values determined by width and height (w, h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + (a*x) + b ), [0])

    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1, 'ro')
    plt.plot(x2, y2, 'ro')
    plt.plot(x3, y3, 'yo')

    # Use a contour plot to draw the line (in black) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1) - m * (x-x1), [0], colors = ('black'))

    # Annotate point 1,2, & 3
    plt.annotate('P', xy = (x1, y1), xytext = (x1 + 1, y1 + 1), arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"),)
    plt.annotate('Q', xy = (x2, y2), xytext = (x2 + 1, y2 + 1), arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"),)
    plt.annotate('Z', xy = (x3, y3), xytext = (x3 + 0, y3 + 2), arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"),)

    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest = "a", default = -1, help = "Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest = "b", default = 1, help = "Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1", dest = "x1", default = 0, help = "X coord for point 1")
    parser.add_argument("-y1", dest = "y1", default = -1, help = "Y coord for point 1")
    parser.add_argument("-x2", dest = "x2", default = 5, help = "X coord for point 2")
    parser.add_argument("-y2", dest = "y2", default = -11, help = "Y coord for point 2")

    args = parser.parse_args()
    
    a = float(args.a)
    b = float(args.b)
    x1 = float(args.x1) 
    y1 = float(args.y1)
    x2 = float(args.x2)
    y2 = float(args.y2)
    
    #Determine if P and Q are on the curve
    if(IsOnECurve(a, b, x1, y1) == 0):
        print("Point P does not lie on the curve")
    if(IsOnECurve(a, b, x2, y2) == 0):
        print("Point Q does not lie on the curve")
        
    #Slope of the line between P and Q
    m = slope(x1, y1, x2, y2, a)
        
    #Calculate Z using 
    #x3 = m^2 - x1 - x2    
    #y3 = sqrt(x^3 + ax + b)
    x3 = float(pow(m, 2) - x1 - x2)
    y3 = float(pow((pow(x3, 3) + ((a * x3) + b)), (1/2)))   
    
    print("ECurve = y^2 = x^3 + ", args.a,"x + ", args.b) 
    print("P = ", "(", args.x1, ", ", args.y1, ")") 
    print("Q = ", "(", args.x2, ", ", args.y2, ")") 
    print("Slope between P & Q = ", m)   
    print("Z = ", "(", x3, ", ", y3, ")")
    
    plotter(a, b, m, x1, y1, x2, y2, x3, y3)

if __name__ == '__main__':
    
    #Good Test Lines
    #python main.py    
    #python main.py -a 0 -b 17 -x1 -1 -y1 4 -x2 2 -y2 5
    #Bad Test Lines
    #python main.py -a 2 -b 1 -x1 2 -y1 3 -x2 -1 -y2 -1
       
    main()