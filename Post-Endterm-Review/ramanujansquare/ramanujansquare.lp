1 {num(R, C, 1..12*12)} 1 :- R=1..4, C=1..4.

R1 = R2 :- num(R1,_,X), num(R2,_,X).
C1 = C2 :- num(_,C1,X), num(_,C2,X).

#const magic=139.

:- #sum{X : num(R,_,X)} != magic, R=1..4.
:- #sum{X : num(_,C,X)} != magic, C=1..4.

:- #sum{X : num(R,R,X)} != magic.
:- #sum{X : num(R,4+1-R,X)} != magic.

:- #sum{X : num(1,1,X;1,4,X;4,1,X;4,4,X)} != magic.
:- #sum{X : num(2,2,X;2,3,X;3,2,X;3,3,X)} != magic.

:- #sum{X : num(1,1,X;1,2,X;2,1,X;2,2,X)} != magic.
:- #sum{X : num(3,1,X;3,2,X;4,1,X;4,2,X)} != magic.

:- #sum{X : num(1,3,X;1,4,X;2,3,X;2,4,X)} != magic.
:- #sum{X : num(3,3,X;3,4,X;4,3,X;4,4,X)} != magic.

:- #sum{X : num(1,2,X;1,3,X;4,2,X;4,3,X)} != magic.
:- #sum{X : num(2,1,X;3,1,X;2,4,X;3,4,X)} != magic.

:- #sum{X : num(1,2,X;2,1,X;3,4,X;4,3,X)} != magic.
:- #sum{X : num(1,3,X;3,1,X;2,4,X;4,2,X)} != magic.

:- #sum{X : num(2,1,X;2,2,X;3,1,X;3,2,X)} != magic.
:- #sum{X : num(2,3,X;2,4,X;3,3,X;3,4,X)} != magic.

