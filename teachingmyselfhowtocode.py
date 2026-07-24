import torch

def rbf_kernel(x1, x2): 
    sq_dist = (x1 - x2) ** 2
    return torch.exp(-0.5 * sq_dist)

print(rbf_kernel(torch.tensor(2.0), torch.tensor(2.0)))
print(rbf.kernel(torch.tensor(0.0), torch.tensor(10.0)))
