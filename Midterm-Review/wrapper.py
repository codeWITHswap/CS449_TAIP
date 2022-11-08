#! /usr/bin/python
import argparse, subprocess, sys, os
import re
from tabulate import tabulate
import math

parser = argparse.ArgumentParser()

def extract(clingo_path, n=3):
    cmd_clingo = "clingo", "-c", f"n={n}", clingo_path #subprocess - pro
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
    
    print(tabulate(arr, tablefmt='fancy_grid'))
    
    os.remove('cling-out')

if __name__ == "__main__":
    parser.add_argument("clingo", type=str, default="magic.lp")
    parser.add_argument("--n", type=int, default=3)

    args = parser.parse_args()
    algo = extract(args.clingo, args.n)