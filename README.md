# Dynamic-program

1 Overview
You are required to solve a dynamic programming problem and write a memoized
version using python.
2 Description
Robots are trying to climb over a wall, however, due to some questionable
programming choices the robots are bound by certain rules. To climb over the wall,
they can only stand on the top of each other’s shoulders, they can only stack so many
on top of each other, and they can only create so many stacks. Given the number of
stacks (n), and the max number of robots that can go in each stack (k) your task is to
figure out how many ways a given number of robots (b) can distribute themselves
into the stacks. Your solution must use dynamic programming.
3 Code
You must implement the project in python. The only rules for your program are that
it must take a text file as input and write the results of the program to the command
line. You must have a main python file called RobotStack.py. The name of the input
file need to be given to the program as a command line parameter. The following
command will be run.
python RobotStack.py input.txt
3.1 Input file format
Each line has 3 comma separated values that detail an instance, and represent b, n, k
in that order.
3.2 Output format
Your output format must look like the following screenshot. Note those are just
examples from the input.txt file on Canvas.
3.3 Example
Given b=3, n=4, and k=2 there are 16 different ways the robots can distribute
themselves. HINT: this problem is (𝑛
𝑏)when k=1 and (𝑛+𝑏−1
𝑏 )when k=b. Note the
solution increases as k move from 1 to b.
