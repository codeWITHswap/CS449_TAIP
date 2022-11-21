1 {num(R, C, -N*N..N*N)} 1 :- R=1..n, C=1..n, N=n+1.

R1 = R2 :- num(R1,_,X), num(R2,_,X).
C1 = C2 :- num(_,C1,X), num(_,C2,X).

#const magic=(n**3+n)/2.

:- #sum{X : num(R,_,X)} != magic, R=1..n.
:- #sum{X : num(_,C,X)} != magic, C=1..n.

:- #sum{X : num(R,R,X)} != magic.
:- #sum{X : num(R,n+1-R,X)} != magic.

#minimize{X : num(R,C,X), X<0}.

#show num/3.
