# BOJ 2739 : 구구단
# https://www.acmicpc.net/problem/2739


import sys
N = int(sys.stdin.readline().rstrip())

for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")