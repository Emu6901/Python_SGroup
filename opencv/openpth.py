import torch
from torch import nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.cnn1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=0)
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(kernel_size=2)
        self.cnn2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=0)
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(kernel_size=2)
        self.fc1 = nn.Linear(32 * 4 * 4, 10)

    def forward(self, x):
        out = self.cnn1(x)
        out = self.relu1(out)
        out = self.maxpool1(out)
        out = self.cnn2(out)
        out = self.relu2(out)
        out = self.maxpool2(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)

        return out


def evalueate_model(model, test_loader):
    predictions = []
    model.eval()
    for images in test_loader:
        train = Variable(images.view(100, 1, 28, 28).type(torch.float32))
        with torch.no_grad():
            predicts = model(train)
            predicts = predicts.argmax(axis=1)
            predicts = predicts.cpu().numpy()

            # Put the batch size data into the list one by one.
            for pred in predicts:
                predictions.append(pred)
    return (predictions)


model = CNNModel()
PATH = "model.pth"
torch.save(model, PATH)
loaded_model = torch.load(PATH)
loaded_model.eval()

test_transforms = transforms.Compose([transforms.Resize((224, 224)),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                           [0.229, 0.224, 0.225])])
test_dir = 'ROI'
test_data = datasets.ImageFolder(test_dir, transform=test_transforms)
test_loader = DataLoader(dataset=test_data)
for (images, labels) in test_loader:
    print(images.shape, labels)

# pred = evalueate_model(model, test_loader)
# print(pred)