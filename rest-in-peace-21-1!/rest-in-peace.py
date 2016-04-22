'''
Created on 22 Apr 2016

@author: RAJESH
https://www.hackerearth.com/problem/algorithm/rest-in-peace-21-1
'''

def solve_problem(N):
    if "21" in str(N) or int(N) % 21 == 0:
        print 'The streak is broken!'
    else:
        print 'The streak lives still in our heart!'
    pass

T = raw_input("")
T = int(T)

if T < 1 or T > 100:
    exit()

for i in range(0, T):
    N = raw_input("")
    N = int(N)
    if N < 1 or N > 1000000:
       exit()

    solve_problem(N)

    