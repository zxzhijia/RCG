import numpy as np
import collections
from time import gmtime, strftime
import _thread

class randomcg:
    def __init__(self):
        self.stack=[]
        self.file=open("disk.txt","a")
        self.strqueue=[]
    def print_num(self):
        res=np.random.choice([1,2,3,4,5],p=[0.5,0.25,0.15,0.05,0.05])
        if len(self.stack)<100:
            self.stack.append(res)
        else:
            self.stack.pop(0)
            self.stack.append(res)
        
        print(self.stack[-1])
        print(len(self.stack))
        return res

    def cal_freq(self):
        c=collections.Counter(self.stack)
        return c
    
    def read_write(self):
        if not self.stack:
            return 
        _thread.start_new_thread(self.read,())
        _thread.start_new_thread(self.write,())
        
    def read(self):    
        tmp=self.stack[-1]
        self.strqueue.append(str(tmp)+' '+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'\n')
        
    def write(self):
        self.file.write(self.strqueue.pop(0))
         
    
def main():
    x=randomcg()
    
    for i in range(200):
            x.print_num()
            
    c=x.cal_freq()
    for i in range(1,6):
        print('{} percentage is {} %'.format(i,c[i]))

    x.read_write()  

if __name__=="__main__":
    main()
