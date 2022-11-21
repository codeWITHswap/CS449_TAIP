#! /usr/bin/python
import argparse, subprocess, sys, os
import re
from tabulate import tabulate
import math

parser = argparse.ArgumentParser()

def extract(clingo_path):
    cmd_clingo = "clingo", clingo_path
    f = open('cling-out','w')
    subprocess.call(cmd_clingo, stdout=f)
    f.close()

    file = open('cling-out','r')
    ans = file.readlines()[4]
    temp = re.findall(r'\d+', ans)
    res = list(map(int, temp))

    n = 4

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
    parser.add_argument("clingo", type=str, default="ramanujansquare.lp")

    args = parser.parse_args()
    algo = extract(args.clingo)
