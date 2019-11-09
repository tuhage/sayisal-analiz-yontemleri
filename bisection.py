import math

def y(x):
    return x-math.cos(x)

def q(x):
    return math.cos(x)

def bisection(a,b,epsilon):
    
    while True:
        c=(a+b)/2
        print("c = ",c)
        if y(c)>0:
            if y(a)<0:
                b=c
            if y(b)<0:
                a=c          
        elif y(c)<0:
            if y(a)>0:
                b=c
            if y(b)>0:
                a=c
        else:
            print("x = ",c)
            break
        
        if abs(c-((a+b)/2))<epsilon:
            print("x = ",(a+b)/2)
            break


if __name__ == "__main__":
    bisection(0.5,1,0.01)