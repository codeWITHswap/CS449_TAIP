To run the Magic Square ASP Solver, follow these steps:

1. Clone this repository and to do so just run the following code on your terminal
~~~
git clone https://github.com/codeWITHswap/CS449_TAIP.git
~~~
2. Change directory to **Task-2** folder and to do so just run the following code on your terminal
~~~
cd Desktop/CS449_TAIP/Endterm-Review/Task-2
~~~
3. Run the python file **wrapper.py** in the following way for a magic square of size n = 3 without any constraints
~~~
python3 wrapper.py --n 3 magic.lp
~~~
4. Run the python file **wrapper.py** in the following way for a magic square of size n = 3 with (1,1,4)
~~~
python3 wrapper.py --n 3 --input input.txt magic.lp
~~~
5. Run the python file **wrapper.py** in the following way for a magic square of size n = 3 with magic constant = 24
~~~
python3 wrapper.py --n 3 --sum 24 magic.lp
~~~
6. Run the python file **wrapper.py** in the following way for a magic square of size n = 3 with magic constant = 24 and (1,1,9) and (2,3,12)
~~~
python3 wrapper.py --n 3 --sum 24 --input input.txt magic.lp
~~~

