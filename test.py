def yanghui(max):
    L = [1]
    for i in range(max):
        n = [1 for x in range(i+1)]
        for j in range(i):
            if j - 1 < 0:
                a = 0
            else:
                a = L[j-1]
            if j + 1 > i:
                b = 0
            else:
                b = L[j]
            n[j] = a + b
        yield n

def odd():
    print("1")
    yield 1
    print("2")
    yield 2
    print("3")
    yield 3
def fib(max):
    n , a, b = 0 , 1 ,1
    while n < max:
        yield b
        a , b = b , a+b
        n = n+1
    return 'done'
#递归汉诺塔
def hanoi(n,a,b,c):
    if(n == 1):
        move(1,a,c)
    else:
        hanoi(n-1,a,c,b)
        move(n-1,a,c)
        hanoi(n-1,b,a,c)
def move(n,_form,_to):
    print(_form,"-->",_to)


def person(name,age,*,city,job):
    print(name,age,city,job)
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
def fact(n):
    if n==0 or n == 1:
        return 1
    return n*fact(n-1)