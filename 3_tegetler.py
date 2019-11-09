import math

def y(x):
    return x-math.cos(x)-0.25
def y_derivate(x):
    return 1+math.sin(x)
def y_2_derivate(x):
    return math.cos(x)
def q(x):
    return x-(y(x)/y_derivate(x))


def tegetler(a,b,epsilon):
    
    if(y(a)*y_2_derivate(a)>0):
        x=a
    else:
        x=b
    
    while True:
        xi=x
        x=q(xi)
        if abs(xi-x)<epsilon:
            print("x = ",x)
            break
    


if __name__ == "__main__":
    tegetler(0,1,0.01)