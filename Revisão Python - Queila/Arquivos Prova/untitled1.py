import math
from typing import Callable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def GetInterval(start:int,end:int,step:float, fn:Callable[[float],float]) -> dict[str,list[int]]:
    x = np.linspace(start,end,math.ceil((end-start)/step))
    my_dict = {"X":[],"Y":[]}

    for i in x:
        my_dict["X"].append(i)
        my_dict["Y"].append(fn(i))
    return my_dict

def x2(i)->float:
    return i*i

def x3(i)->float:
    return i*i*i

a  = GetInterval(-20,20,1,x2)
b = GetInterval(-20,20,1,x3)


fig, axis = plt.subplots(nrows = 1, ncols = 2, figsize = (15,10))
axis[0].plot(a["X"],a["Y"],color='b',linewidth=4)
axis[1].plot(b["X"],b["Y"],color='r',linewidth=4)

axis[0].set_title("f(x)= x²")
axis[1].set_title("f(x)= x³")

axis[0].grid()
axis[1].grid()

plt.show()

