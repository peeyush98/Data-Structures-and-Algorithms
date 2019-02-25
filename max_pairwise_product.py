# python 3

n = int(input())
a = [int(x) for x in input().split()]
b = sorted(a)
print(b[-1] * b[-2])
