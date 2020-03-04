from numpy import *
from matplotlib.pyplot import *
import gc
from tqdm import tqdm
import time
from readTrc import *

#Trcfile_Number(c4_00001.trc,c4_00002.trc)
NumTrc = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20")

#File_Number
NumFile = arange(0,61)
for i in tqdm(NumFile):
    for j in NumTrc:
        data = readTrc("exdata/{1}/c4_000{0}.trc".format(j,i))

        save("exnumpy/{1}/exnpy_{0}.npy".format(j,i),data)
