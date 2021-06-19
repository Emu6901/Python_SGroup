import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

# 1) Design model (input, output, forward pass with different layers)
# 2) Construct loss and optimizer
# 3) Training loop
#       - Forward = compute prediction and loss
#       - Backward = compute gradients
#       - Update weights

# prepare data
X_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))
y = y.view(y.shape[0], 1)
# print(y)
n_samples, n_features = X.shape

# 1) Design model (input, output, forward pass with different layers)

input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

# 2) Construct loss and optimizer
learning_rate = 0.01
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# 3) Training loop
n_epoch = 100
for epoch in range(n_epoch):
    # - Forward = compute prediction and loss
    y_pred = model(X)
    loss = criterion(y_pred, y)
    # - Backward = compute gradients
    loss.backward()
    # - Update weights
    optimizer.step()
    optimizer.zero_grad()
    if (epoch + 1) % 10 == 0:
        print(f'epoch: {epoch + 1}, loss = {loss.item():.4f}')

#plot
predicted = model(X).detach().numpy()
print(predicted)
plt.plot(X_numpy, y_numpy, 'ro')
plt.plot(X_numpy, predicted, 'b')
plt.show()