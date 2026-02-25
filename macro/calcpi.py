
import numpy as np

def calculate_pi_naive(N: int = 1000000) -> float:
    x = np.random.uniform(0., 1., N)
    y = np.random.uniform(0., 1., N)
    n = np.sum(x**2 + y**2 <= 1.)
    print(n, N)
    epsilon0 = n / N
    sigma_epsilon = np.sqrt(epsilon0 * (1 - epsilon0) / N)
    pi0 = epsilon0 * 4.
    sigma_pi = sigma_epsilon * 4.
    return pi0, sigma_pi

def calculate_pi_clever(N: int = 1000000) -> float:
    x = np.random.uniform(0., 1., N)
    y = np.random.uniform(0., 1., N)
    mask = x + y <= 1.
    x[mask] = 1. - x[mask]
    y[mask] = 1. - y[mask]
    n = np.sum(x**2 + y**2 <= 1.)
    print(n, N)
    epsilon0 = n / N
    sigma_epsilon = np.sqrt(epsilon0 * (1 - epsilon0) / N)
    pi0 = 2. * (epsilon0 + 1.)
    sigma_pi = sigma_epsilon * 2.
    return pi0, sigma_pi


if __name__ == "__main__":
    pi0, sigma_pi = calculate_pi_naive()
    print(f"Naive: pi = {pi0:.6f} ± {sigma_pi:.6f}, pull = {(pi0 - np.pi) / sigma_pi:.2f}")
    pi0, sigma_pi = calculate_pi_clever()
    print(f"Clever: pi = {pi0:.6f} ± {sigma_pi:.6f}, pull = {(pi0 - np.pi) / sigma_pi:.2f}")