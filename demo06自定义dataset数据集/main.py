#�����Լ���datasets��
import json
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import Dataset,DataLoader

class CIFAR10_IMG(Dataset):

    def __init__(self, root, train=True, transform = None, target_transform=None):
        super(CIFAR10_IMG, self).__init__()
        self.train = train
        self.transform = transform
        self.target_transform = target_transform

        #�����ѵ�������ѵ����������ǲ�������ز��Լ�
        if self.train :
            file_annotation = root + '/annotations/cifar10_train.json'
            img_folder = root + '/train_cifar10/'
        else:
            file_annotation = root + '/annotations/cifar10_test.json'
            img_folder = root + '/test_cifar10/'
        fp = open(file_annotation,'r')
        data_dict = json.load(fp)

        #���ͼ�����ͱ�ǩ����ƥ��˵�����ݼ���ע���������⣬������ʾ
        assert len(data_dict['images'])==len(data_dict['categories'])
        num_data = len(data_dict['images'])

        self.filenames = []
        self.labels = []
        self.img_folder = img_folder
        for i in range(num_data):
            self.filenames.append(data_dict['images'][i])
            self.labels.append(data_dict['categories'][i])

    def __getitem__(self, index):
        img_name = self.img_folder + self.filenames[index]
        label = self.labels[index]

        img = plt.imread(img_name)
        img = self.transform(img)   #���Ը���ָ����ת����ʽ�����ݼ�����ת��

        #return����Щ���ݣ���ô������ѵ��ʱѭ����ȡÿ��batchʱ�����ܻ����Щ����
        return img, label

    def __len__(self):
        return len(self.filenames)
#ʹ��Dataloader�����Զ������ݼ�
import datasets
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import DataLoader
import torchvision
import torch

train_dataset = datasets.CIFAR10_IMG('./datasets',train=True,transform=transforms.ToTensor())
test_dataset = datasets.CIFAR10_IMG('./datasets',train=False,transform=transforms.ToTensor())

train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=6, shuffle=True)

for step ,(b_x,b_y) in enumerate(train_loader):
    if step < 3:
        imgs = torchvision.utils.make_grid(b_x)
        imgs = np.transpose(imgs,(1,2,0))
        plt.imshow(imgs)
        plt.show()