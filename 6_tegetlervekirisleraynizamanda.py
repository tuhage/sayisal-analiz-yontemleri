import math

def y(x):
    return x-math.cos(x)-0.25
def y_derivate(x):
    return 1+math.sin(x)
def y_2_derivate(x):
    return math.cos(x)
def qk(x,x0):
    return (x0*y(x)-x*y(x0))/(y(x)-y(x0))
def qt(x):
    return x-(y(x)/y_derivate(x))


def tegetlervekirisler(a,b,epsilon):
    x=list()
    if(y(a)*y_2_derivate(a)>0):
        x.append(qt(a))
        x.append(qk(a,b))
    else:
        x.append(qt(b))
        x.append(qk(a,b))
    
    i=2
    while True:
        if i%2==0:

            k=i/2
            x.append(qt(x[int(2*k-2)]))
        else:
            k=(i-1)/2
            x.append(qk(x[int(2*k-1)],x[int(2*k-2)]))

        if abs(x[-1]-x[-2]) < epsilon:
            print(x[-1])
            break

    


if __name__ == "__main__":
    tegetlervekirisler(0,1,0.000001)