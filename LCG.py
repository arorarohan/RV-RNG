import numpy as np
import matplotlib.pyplot as plt

class LCG(object):
    def __init__(self, seed):
        self.X = int(seed)

    def generate(self):
        self.X = (1664525 * self.X + 1013904223) % 4294967296
        return self.X
    
    def uniform(self):
        return self.generate() / 4294967296
    
    def bernoulli(self, p):
        # to be completed
        pass


if __name__ == "__main__":
    generator = LCG(1234)

    # generate uniform numbers
    X1 = np.array([generator.uniform() for _ in range(1000)])
    X2 = np.array([generator.uniform() for _ in range(100000)])

    """
    # Plot histograms
    fig, ax = plt.subplots(2)
    ax[0].hist(X1, bins=np.linspace(0,1,20))
    ax[1].hist(X2, bins=np.linspace(0,1,20))
    plt.show()
    """

    #calculate mean
    mean_x2 = np.mean(X2)
    print(f"X2 mean = {mean_x2}")

    #calculate variance
    variance_x2 = np.var(X2)
    print(f"X2 variance = {variance_x2}")

    #calculate covariance
    X_t = X2[:-1] #starts at the start
    X_t1 = X2[1:] #starts offset by one
    covariance = np.cov(X_t, X_t1)[0,1] #covariance matrix, this index gives the Cov.
    print(f"X2 covariance = {covariance}")