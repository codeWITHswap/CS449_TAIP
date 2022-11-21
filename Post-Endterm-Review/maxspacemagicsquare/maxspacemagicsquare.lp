1 {num(R, C, 1..6*6)} 1 :- R=1..n, C=1..n.

R1 = R2 :- num(R1,_,X), num(R2,_,X).
C1 = C2 :- num(_,C1,X), num(_,C2,X).

#const magic=m.

:- #sum{X : num(R,_,X)} != magic, R=1..n.
:- #sum{X : num(_,C,X)} != magic, C=1..n.

:- #sum{X : num(R,R,X)} != magic.
:- #sum{X : num(R,n+1-R,X)} != magic.

#maximize{|X-Y|,|X-Z| : num(R,C,X), num(R,C+1,Y), num(R+1,C,Z), R=1..n, C=1..n}.

#show num/3.
