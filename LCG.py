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
        # Draw from a uniform (0,1) RV. Return 1 is the result is below p or 0 if the result is above p.
        # Because we are drawing from a uniform distribution, the probability that the result is less than p is p.
        # And therefore the probability of drawing above p is 1-p. So this acts just like a bernoulli RV.
        draw = self.uniform()

        if draw < p:
            return 1
        
        return 0

    def binomial(self, n, p):
        # Generate n independent bernoulli trials and sum them together
        trials = [self.bernoulli(p) for _ in range(n)]
        return sum(trials)


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
    
    
    # Q2: y = g(x) = x^2, with x ~ U(0,1)
    # transform the LCG samples
    X2 = np.array([generator.uniform() for _ in range(100000)])
    Y2 = X2 ** 2

    y_grid = np.linspace(0.001, 1, 1000)
    p_Y = 1 / (2 * np.sqrt(y_grid)) #per derivation

    # build the chart
    fig, ax = plt.subplots()
    ax.hist(Y2, bins=np.linspace(0, 1, 50), density=True, label="Histogram of $y=x^2$ samples")
    ax.plot(y_grid, p_Y, 'r', label=r"$p_Y(y)=\frac{1}{2\sqrt{y}}$")
    ax.set_xlabel("y")
    ax.set_ylabel("$p_Y(y)$")
    ax.set_ylim(0, 5)  # p_Y diverges at y=0
    ax.legend()
    #fig.savefig("figures/q2-square.pdf")
    #plt.show()


    # Q2: y = g(x) = ln(x) - ln(1-x), with x ~ U(0,1)
    # transform fresh LCG samples

    X2 = np.array([generator.uniform() for _ in range(100000)])
    Y3 = np.log(X2) - np.log(1 - X2)

    y_grid = np.linspace(-10, 10, 1000)
    p_Y = np.exp(y_grid) / (1 + np.exp(y_grid)) ** 2 #per derivation

    # build the chart
    fig, ax = plt.subplots()
    ax.hist(Y3, bins=np.linspace(-10, 10, 80), density=True, label=r"Histogram of $y=\ln(x)-\ln(1-x)$ samples")
    ax.plot(y_grid, p_Y, 'r', label=r"$p_Y(y)=\frac{e^y}{(1+e^y)^2}$")
    ax.set_xlabel("y")
    ax.set_ylabel("$p_Y(y)$")
    ax.legend()
    fig.savefig("figures/q2-log.pdf")     
    plt.show()


    # Q3: exponential distribution via the inverse CDF, F^-1(x) = -ln(1-x)

    X4 = np.array([generator.uniform() for _ in range(100000)])
    Y4 = -np.log(1 - X2)

    y_grid = np.linspace(0, 8, 1000)
    p_Y = np.exp(-y_grid) #exponential pdf with mean 1

    # build the chart
    fig, ax = plt.subplots()
    ax.hist(Y4, bins=np.linspace(0, 8, 60), density=True, label=r"Histogram of $y=-\ln(1-x)$ samples")
    ax.plot(y_grid, p_Y, 'r', label=r"$p_Y(y)=e^{-y}$")
    ax.set_xlabel("y")
    ax.set_ylabel("$p_Y(y)$")
    ax.legend()
    fig.savefig("figures/q3-exponential.pdf")
    plt.show()


    # Q4: neutral selection, N_A(t+1) ~ Binomial(N, N_A(t)/N), N_B(t+1) = N - N_A(t+1)

    N = 200
    N_A0 = 100
    T = 500
    seeds = [14, 5, 7, 4, 8, 15] # seeds chosen to show the different outcomes

    fig, axes = plt.subplots(2, 3, figsize=(12, 6), sharex=True, sharey=True)
    for ax, seed in zip(axes.flat, seeds):
        gen = LCG(seed)
        N_A = np.zeros(T + 1, dtype=int)
        N_A[0] = N_A0
        for t in range(T):
            N_A[t + 1] = gen.binomial(N, N_A[t] / N)
        N_B = N - N_A

        ax.plot(N_A, label="$N_A(t)$")
        ax.plot(N_B, label="$N_B(t)$")
        ax.set_title(f"Run (seed {seed})")
    for ax in axes[1]:
        ax.set_xlabel("t")
    for ax in axes[:, 0]:
        ax.set_ylabel("population size")
    axes[0, 0].legend()
    fig.tight_layout()
    fig.savefig("figures/q4-neutral-selection.pdf")
    plt.show()
