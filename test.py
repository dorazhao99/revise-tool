import argparse
from datasets import *
import pickle
import torchvision.transforms as transforms
import torch.utils.data as data
import os
from measurements import object_based
from measurements import gender_based
from measurements import geography_based

def main():
    transform_train = transforms.Compose([           
        transforms.ToTensor(),                          
        ])

    dataset = OpenImagesDataset(transform_train)

if __name__ == '__main__':
    main()

