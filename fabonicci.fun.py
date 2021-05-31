prev = {0:0,1:1}
def fib(n):
    if n in prev.keys():
        return prev[n]
    else:
        fi = fib(n-1) + fib (n-2)
        prev[n] = fi
        return fi
		
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))


