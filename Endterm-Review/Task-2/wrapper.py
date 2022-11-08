#! /usr/bin/python
import argparse, subprocess, sys, os
import re
from tabulate import tabulate
import math

parser = argparse.ArgumentParser()

def extract_constraints(input_path):

    if(input_path==""):
        return "", 0

    file = open(input_path, 'r')
    constraints = file.readlines()
    constraint="\n"
    x = len(constraints)
    for i in range(x):
        g = []
        g = constraints[i].split()
        constraint+="num("
        constraint+=g[0]
        constraint+=","
        constraint+=g[1]
        constraint+=","
        constraint+=g[2]
        constraint+=")."
        if(i!=len(constraints)-1):
            constraint+="\n"
    return constraint, x

def extract(clingo_path, constraints, d, m, n=3):


    clingo_program = open(clingo_path, 'a') #appending
    clingo_program.write(constraints)
    clingo_program.close()


    cmd_clingo = "clingo", "-c", f"n={n}", "-c", f"m={m}", clingo_path #calling the subprocess
    f = open('cling-out','w')
    subprocess.call(cmd_clingo, stdout=f)
    f.close()

    file = open('cling-out','r')
    ans = file.readlines()[4]
    temp = re.findall(r'\d+', ans)
    res = list(map(int, temp))

    n = int(math.sqrt(len(res)/3))

    arr=[]
    for r in range(n):
        col = []
        for c in range(n):
            col.append(0)
        arr.append(col)

    k=0
    while(k<len(res)):
        row = res[k]
        k+=1
        col = res[k]
        k+=1
        val = res[k]
        k+=1
        arr[row-1][col-1]=val   

    if(d!=0):
        x = d
        clingo_program = open(clingo_path, "r")
        d = clingo_program.read()
        clingo_program.close()
        m=d.split("\n")
        s="\n".join(m[:-x]) 
        clingo_program = open(clingo_path, "w+")
        for i in range(len(s)):
            clingo_program.write(s[i])
        clingo_program.close()

    
    
    print(tabulate(arr, tablefmt='fancy_grid'))

    os.remove('cling-out')


if __name__ == "__main__":
    parser.add_argument("clingo", type=str, default="magic.lp")
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--sum", type=int, default=15)
    parser.add_argument("--input", type=str, default="")

    args = parser.parse_args()

    constraints, d = extract_constraints(args.input)
    extract(args.clingo, constraints, d, args.sum, args.n)