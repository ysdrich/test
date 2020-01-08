"""
https://projecteuler.net/problem=1

10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
"""

sum = 0
x = 1000

for n in range(x):
    if n%3 == 0:
        sum += n
    elif n%5 == 0:
        sum += n

print(sum)
