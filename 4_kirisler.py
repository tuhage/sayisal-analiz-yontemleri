import math

def y(x):
    return x-math.cos(x)-0.25
def y_derivate(x):
    return 1+math.sin(x)
def y_2_derivate(x):
    return math.cos(x)
def q(x,x0):
    return (x0*y(x)-x*y(x0))/(y(x)-y(x0))


def tegetler(a,b,epsilon):
    
    if(y(a)*y_2_derivate(a)>0):
        x=b
        x0=a
    else:
        x=a
        x0=b
    
    while True:
        xi=x
        x=q(xi,x0)
        if abs(xi-x)<epsilon:
            print("x = ",x)
            break
    


if __name__ == "__main__":
    tegetler(0,1,0.01)