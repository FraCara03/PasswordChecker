# place `import` statement at top of the program
import math


# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
def copysign(x,y):
     result = math.copysign(x,y)
     return result

output = copysign(x,y)
print(output)
