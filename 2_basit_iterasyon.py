import math

def y(x):
    return x-math.cos(x)

def q(x):
    return math.cos(x)

def q_derivate(x):
    return -math.sin(x) 
    
def basit_iterasyon(a,b,epsilon):
    x=q(b)
    while True:
        xi=x
        x=q(x)
        if abs(xi-x)<epsilon:
            print("x = ",x)
            break
if __name__ == "__main__":
    basit_iterasyon(0.5,1,0.01)