import torch

X = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
Y = torch.tensor([2, 4, 6, 8], dtype=torch.float32)

# f = w * X

w = torch.tensor(0, dtype=torch.float32, requires_grad=True)


def forward(x):
    return w * x


def loss(y, y_pred):
    return ((y_pred - y) ** 2).sum() / len(y)


learning_rate = 0.01
n_epoch = 50

for epoch in range(n_epoch):
    y_pred = forward(X)
    l = loss(Y, y_pred)
    l.backward()
    with torch.no_grad():
        w -= learning_rate * w.grad
    w.grad.zero_()
    if epoch % 10 == 0:
        print(f'epoch {epoch + 1}: w = {w.item():.3f}, loss = {l.item():.8f}')


print(f'Prediction after training: f(5) = {forward(5).item():.3f}')