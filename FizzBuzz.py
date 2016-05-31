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
	
test_cases.close()
