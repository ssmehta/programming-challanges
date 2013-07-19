# Solution for Python 2.x
print'\n'.join('Fizz'*(i%3<1)+'Buzz'*(i%5<1)or`i`for i in range(1,101))
