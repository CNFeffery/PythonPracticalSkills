import numpy as np
from memory_profiler import profile

@profile
def demo():
    a = np.random.rand(10000000)
    b = np.random.rand(10000000)
    
    a_ = a[a < b]
    b_ = b[a < b]
    
    del a, b

    return a_, b_


if __name__ == '__main__':
    demo()