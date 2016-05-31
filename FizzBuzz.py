import sys
test_cases = open(sys.argv[1], 'r')

def fizzBuzz(x, y, n):
    result = []
    for num in range(1, n+1):
        if num % x == 0 and num % y == 0:
            result.append("FB")
        elif num % x == 0:
            result.append("F")
        elif num % y == 0:
            result.append("B")
        else:
            result.append(str(num))
    print " ".join(result)
	
for line in test_cases:
    nums = [int(x) for x in line.split()]
    fizzBuzz(*nums) 

## Note 1: * operator
## * is a shortcut that allows you to pass multiple arguments to a function directly using either a list/tuple or a dictionary. 
## so fizzBuzz(*[2,7,10]) is equivalent to fizzBuzz(2,7,10)
	
test_cases.close()
