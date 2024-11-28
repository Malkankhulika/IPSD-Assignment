import cv2 as cv
import torch
import numpy as np
from os import listdir
from torch.utils.data import Dataset


class getImageLabel(Dataset):
    def __init__(self, folder='./Dataset'):
        self.dataset = []

        # initiate the one hot encoding for class
        to_one_hot = np.eye(5)  # number of class
        for i, dino in enumerate(sorted(listdir(folder))):
            for image_name in listdir(folder + "/" + dino):
                # read image, resize image, and normalize image to 0-1 range
                image = cv.resize(cv.imread(folder + "/" + dino + "/" + image_name), (100, 100)) / 255
                # append feature image and one hot encoded label to public self.dataset
                self.dataset.append([image, to_one_hot[i]])

    def __getitem__(self, item):
        feature, label = self.dataset[item]
        return torch.tensor(feature, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)

    def __len__(self):
        return len(self.dataset)


