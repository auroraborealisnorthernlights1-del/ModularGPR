import torch



# This is a 1D vectorized RBF Covariance Matrix :)
def rbf_covariance(X):
    return  torch.exp((-1/2)*(X.unsqueeze(1) - X.unsqueeze(0)) ** 2).

X = torch.tensor([4.0, 5.0])
print(rbf_covariance(X))


# also something thats cool is that "X.unsqueeze(1) - X.unsqueeze(0)" works no matter how big the matrix is

# This is a Multi-Dimensional vectorized RBF Covariance Matrix :)

def multiDrbf_covariance(Y):
    return  torch.exp((-1/2)*((Y.unsqueeze(1) - Y.unsqueeze(0)) ** 2).sum(dim=-1))

Y = torch.tensor([[4.0, 5.0],[7.0, 9.0]])
print(multiDrbf_covariance(Y))

#yeah i talked in slack, I did type a little bit while researching to keep the timer going but that was roughly for only 20 minutes max, Im currently writing at 1h 30m in, void as much time as you need, I will push this to github for timestamped proof