# Raising an Exception
import collections

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    else:
        return x * x
    
#example 2

def sum2(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError("parameter must be iterable")
    
    total = 0 
    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError("elements must be numeric")
        total += value
    return total

#try - except block

def divide(x,y):
    try:
        ratio = x / y
        return ratio
    except ZeroDivisionError:
        return 0

def er():
    try:
        fp = open('sample.txt')
    except IOError as e:
        print("can't open", e)


#ITERATORS AND GENERATORS

def factors(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k

def factors2(n):
    for k in range(1,n + 1):
        while k * k < n:
            if n % k == 0:
                yield k
                yield n // k
            k += 1
            if k * k == n:
                yield k

def fib():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a + b


#List Comprehension

result = [k*k for k in range(1,20)]

#Scopes and Namespaces

'''
Name resolution is the process od determining
the value associated with an identifier
vars() - reports on the most locally enclosing namespace - full details
dirs() - return the keys of the dict storing the namespace'''

#EXERCISES

def is_multiple(n, m):
    if n % m == 0:
        return True
    return 
print(is_multiple(10, 20))

def minmax(data):
    first = data[0]
    second = data[0]
    for i in data[1:]:
        if i < first:
            first = i
        if i > second:
            second = i
    return first, second
        
print(minmax([1,2,10,4,5]))

def positive_int(n):
        try:
            result = []
            for num in range(1, n):
                 result.append((num * num))
            return result
        except:
            print(f"{n} is invalid")

print(positive_int(10))


ans = [2**x for x in range(9)]
print(ans)


    