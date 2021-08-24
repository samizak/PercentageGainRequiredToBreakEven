import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Formula to calculate percentage required to break-even from percentage Loss
# G = L / (1 - 0.01L)
def CalculatePercentageGainRequired(L):
    return L / (1 - 0.01 * L)

def CalculatePercentageGainLoss ():
    for i in range (0, 100, 1):
        gain = CalculatePercentageGainRequired(i)
        data.append([-i, gain])
        
def plotGraph (data):
    # Get columns
    x, y = data[:, 0], data[:, 1]

    fig, ax = plt.subplots(2)
    fig.suptitle('Percentage Change Required to Break-Even')

    # Linear scale Graph
    ax[0].plot(x, y)
    ax[0].set(xlabel='Loss (%)', ylabel='Gain (%)', title="Linear Scale")
    ax[0].grid()
    ax[0].set_xticks(np.arange(0, -101, -10))

    # Log Scale Graph
    ax[1].plot(x, y)
    ax[1].set(xlabel='Loss (%)', ylabel='Gain (%)', title="Log Scale")
    ax[1].set_yscale('log')
    ax[1].grid()
    ax[1].set_xticks(np.arange(0, -101, -10))

    plt.show()

data = []

print("Percentage change required to Break-Even:")
print("-" * 40 + '\n')

CalculatePercentageGainLoss ()
df = pd.DataFrame(data, columns=['Loss (%)', 'Gain (%)'])

# Print DataFrame without index
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print (df.to_string(index=False))

plotGraph(df.to_numpy())
