import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)
def coinFlipper(headProb,times):
    headResult = []
    tailResult = []
    headProb = headProb
    numCoins = 10
    times = times
    for x in range(times):
        head = []
        tail = []
        for x in range(numCoins):
            if random.randrange(9) >= headProb:
                head.append('x')
            else:
                tail.append('x')
        headResult.append(len(head))
        tailResult.append(len(tail))


    headPlot = [0] * 11
    tailPlot = [0] * 11
    for x in headResult:
        headPlot[x] += 1
    for x in tailResult:
        tailPlot[x] += 1

    n_groups = 11

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    rects1 = plt.bar(index, headPlot, align='center')


    plt.xlabel('Frequency')

    plt.ylabel('Appearance')

    plt.title('Times Heads With ' + str(numCoins) + " Coins Fliped " + str(times) + ' Times and ' + str(((10 - headProb))/10) + ' Probability for Heads')

    plt.xticks(index ,('0','1', '2', '3', '4','5','6','7','8','9','10'))

    plt.tight_layout()
    fileTitle = str(headProb) +' '+ str(times)
    plt.savefig(fileTitle)
    print(times)

coinFlipper(0,10)
coinFlipper(0,100)
coinFlipper(0,1000)
coinFlipper(0,1000000)

coinFlipper(1,10)
coinFlipper(1,100)
coinFlipper(1,1000)
coinFlipper(1,1000000)

coinFlipper(2,10)
coinFlipper(2,100)
coinFlipper(2,1000)
coinFlipper(2,1000000)

coinFlipper(3,10)
coinFlipper(3,100)
coinFlipper(3,1000)
coinFlipper(3,1000000)

coinFlipper(4,10)
coinFlipper(4,100)
coinFlipper(4,1000)
coinFlipper(4,1000000)

coinFlipper(5,10)
coinFlipper(5,100)
coinFlipper(5,1000)
coinFlipper(5,1000000)


coinFlipper(6,10)
coinFlipper(6,100)
coinFlipper(6,1000)
coinFlipper(6,1000000)

coinFlipper(7,10)
coinFlipper(7,100)
coinFlipper(7,1000)
coinFlipper(7,1000000)

coinFlipper(8,10)
coinFlipper(8,100)
coinFlipper(8,1000)
coinFlipper(8,1000000)

coinFlipper(9,10)
coinFlipper(9,100)
coinFlipper(9,1000)
coinFlipper(9,1000000)



