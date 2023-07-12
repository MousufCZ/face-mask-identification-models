##############################################################################
# TODO: Implementing CNN	             		                       #
##############################################################################
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms

def train_CNN(model_ft, num_classes):
    # Freeze all layers in the model except the last layer
    for param in model_ft.parameters():
        param.requires_grad = False
    # Replace the last fully connected layer with a new one that outputs the desired number of classes
    num_ftrs = model_ft.fc.in_features
    model_ft.fc = nn.Linear(num_ftrs, num_classes)
    return model_ft

##############################################################################
#                             END OF YOUR CODE                               #
##############################################################################