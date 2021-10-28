#This is for solving original tower of Hanoi
def show(d):
    for i,peg in enumerate(d): print(f"{i}: {d[i]}")
def move(d,s,t):
    print(f"STEP: move disk {d[s][-1]} from peg {s} to peg {t}")
    d[t].append(d[s][-1]);d[s].pop();show(d)
def hanoi(n):
    d=[[] for i in range(3)]
    d[0] = list(reversed(range(n)))
    print("Start");show(d)
    solve(d,n-1,0,2)
def solve(d,n,s,t):
    if n>=0:
        u=3-s-t
        solve(d,n-1,s,u)
        move(d,s,t)
        solve(d,n-1,u,t)
"""This is for solving a variation of tower of Hanoi.
This variation prohibits direct moving of disks from peg 0 to peg 2"""
def r_hanoi(n):
    d=[[] for i in range(3)]
    d[0] = list(reversed(range(n)))
    print("Start");show(d)
    r_solve(d,n-1,0,1,2)
"""This is function for moving the first nth disk from the top of peg s
to peg t while using peg u as spare peg."""	
def r_solve(d,n,s,u,t):
    if n>=0:
        r_solve(d,n-1,s,u,t)
        move(d,s,u)
        r_solve(d,n-1,t,u,s)
        move(d,u,t)
        r_solve(d,n-1,s,u,t)
n=int(input("n : "))
hanoi(n)
#r_hanoi(n)
