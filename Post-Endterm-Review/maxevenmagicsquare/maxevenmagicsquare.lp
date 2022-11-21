1 {num(R, C, 1..12*12)}1 :- R=1..n, C=1..n.

R1 = R2 :- num(R1,_,X), num(R2,_,X).
C1 = C2 :- num(_,C1,X), num(_,C2,X).

#const magic=m.

:- #sum{X : num(R,_,X)} != magic, R=1..n.
:- #sum{X : num(_,C,X)} != magic, C=1..n.

:- #sum{X : num(R,R,X)} != magic.
:- #sum{X : num(R,n+1-R,X)} != magic.

#maximize{1,X : num(R,C,X), R=1..n, C=1..n, X\2=0}.
