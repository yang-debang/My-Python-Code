#encoding=gbk

import numpy as np
import matplotlib.pyplot as plt
def main():
    x=np.linspace(-10,10,100)
    y=np.sin(x)
    plt.plot(x,y,'r',linewidth=2)
    plt.show()

if __name__ == '__main__':
    main()
