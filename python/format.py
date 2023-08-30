import math

st = '{} is {}'.format('python','good')
print(st)
print('{2} {1} {0}'.format(10,20,30))
print('{:*>10}'.format(10))#right alignment ,* is print in empyt spaces
print('{:*<10}'.format(10))#left alignment
print('{:*^10}'.format(10))#center alignment
print('{:.6f}'.format(math.pi))#find point notation,number digit(6) after dot  
print('{:e}'.format(math.pi))#exponent notation