# https://www.hackerrank.com/challenges/string-validators/problem

s = input()
print(any([x.isalnum() for x in s]))
print(any([x.isalpha() for x in s]))
print(any([x.isdigit() for x in s]))
print(any([x.islower() for x in s]))
print(any([x.isupper() for x in s]))
