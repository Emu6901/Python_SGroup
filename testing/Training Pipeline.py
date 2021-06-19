# 1) Design model (input, output, forward pass with different layers)
# 2) Construct loss and optimizer
# 3) Training loop
#       - Forward = compute prediction and loss
#       - Backward = compute gradients
#       - Update weights

import torch
import torch.nn as nn

# Linear regression
# f = w * x

# here : f = 2 * x

# 0) Training samples
X = torch.tensor([[1], [2], [3], [4]], dtype=torch.float32)
Y = torch.tensor([[2], [4], [6], [8]], dtype=torch.float32)

X_test = torch.tensor([5], dtype=torch.float32)

# 1) Design Model: Weights to optimize and forward function
n_samples, n_features = X.shape
print(f'#samples: {n_samples}, #features: {n_features}')
input_size = n_features
output_size = n_features

model = nn.Linear(input_size, output_size)


print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

# 2) Define loss and optimizer
learning_rate = 0.01
n_epoch = 100
loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(n_epoch):
    y_pred = model(X)
    l = loss(Y, y_pred)
    l.backward()
    optimizer.step()
    optimizer.zero_grad()
    if epoch % 10 == 0:
        [w,b] = model.parameters()
        print('epoch ', epoch + 1, ': w = ', w[0][0].item(), ' loss = ', l.item())

print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')
