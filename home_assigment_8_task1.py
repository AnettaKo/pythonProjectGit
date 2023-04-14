from calculator import simple
from calculator import complex

def f1(x,y): # 2 * x + y

    print(simple.sum(simple.mult(2,x),y))

def f2(x,y): # 1/x - y

    if x != 0:
        print(simple.minus(simple.div(1,x),y))
    else:
        print('Zero division error')

def f3(x,y):
    print(complex.exp(x,y))

def f4(x):
    print(complex.fact(x))

def f5(x):
    print(complex.root2(x))

def f6(x,y):
    print(complex.log(x,y))

f1(2,2)
f2(2,2)
f3(2,-2)
f4(3)
f5(4)
f6(4,2)




