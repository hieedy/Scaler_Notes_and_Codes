from time import time
from array import *


squares = array('i', [2]*100000000)
t1 = time()
for i in range(len(squares)):
    squares[i] = squares[i]*squares[i]

t2 = time()


print(t2-t2)
