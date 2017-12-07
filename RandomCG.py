import numpy as np

def print_num():
        res=np.random.choice([1,2,3,4,5],p=[0.5,0.25,0.15,0.05,0.05])
        return res


def main():
    res=print_num()
    print(res)

if __name__=="__main__":
    main()
