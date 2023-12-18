import torch

class cgle:
    def __init__(self, alpha, beta, gamma, dx, dt):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.dx = dx
        self.dt = dt

    # Laplacian operator in 1D
    def laplacian_1d(self, u):
        return (torch.roll(u, -1, dims=-1) - 2*u + torch.roll(u, 1, dims=-1)) / (self.dx**2)

    # Update function for CGLE
    def update(self, A):
        dA = self.dt * (self.alpha * A + self.beta * self.laplacian_1d(A) - self.gamma * torch.abs(A)**2 * A)
        if torch.any(torch.isnan(dA)) or torch.any(torch.isinf(dA)):
            raise ValueError("Numerical instability detected.")
        return A + dA
