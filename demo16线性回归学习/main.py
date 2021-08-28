# -*- coding: gbk -*-
#���ǹ���һ���򵥵��˹�ѵ�����ݼ���������ʹ�����ܹ�ֱ�۱Ƚ�ѧ���Ĳ�������ʵ��ģ�Ͳ�����������ѵ�����ݼ�������Ϊ1000��
#�����������������Ϊ2������������ɵ������������� X��R1000��2 ������ʹ�����Իع�ģ����ʵȨ�� w=[2,3.4]��ƫ�� b=4.2 ��
#�Լ�һ����������������ɱ�ǩ
from IPython import display
from matplotlib import pyplot as plt
from mxnet import autograd, nd
import random

num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))#������ά������飬shape��ʾ���м��еģ�scale��ʾ��̫�ֲ��ı�׼��Ϊ1
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b#���,labels��һ��һǧ����һά����
labels += nd.random.normal(scale=0.01, shape=labels.shape)#�ټ�������������
def use_svg_display():
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    plt.rcParams['figure.figsize'] = figsize
set_figsize()
plt.scatter(features[:, 1].asnumpy(), labels.asnumpy(), 1);

plt.show()#ͨ�����ɵڶ�������features[:, 1]�ͱ�ǩ labels ��ɢ��ͼ�����Ը�ֱ�۵ع۲����߼�����Թ�ϵ��
def data_iter(batch_size, features, labels):#��ѵ��ģ�͵�ʱ��������Ҫ�������ݼ������϶�ȡС���������������������Ƕ���һ����������ÿ�η���batch_size��������С������������������ͱ�ǩ��
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)  # �����Ķ�ȡ˳���������
    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i: min(i + batch_size, num_examples)])
        yield features.take(j), labels.take(j)  # take���������������ض�ӦԪ��
#ȡ10������

batch_size = 10
'''
for x, y in data_iter(batch_size, features, labels):
    print(x, y)
    break
'''

w = nd.random.normal(scale=0.01, shape=(num_inputs, 1))
print("��ʼ��:",w)
b = nd.zeros(shape=(1,))
print("��ʼ��:",b)
w.attach_grad()
b.attach_grad()   

def linreg(X, w, b):  
    return nd.dot(X, w) + b #dot()���ص�����������ĵ��(dot product)

def squared_loss(y_hat, y):  # �������ѱ�����d2lzh���з����Ժ�ʹ��
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

def sgd(params, lr, batch_size):  # �������ѱ�����d2lzh���з����Ժ�ʹ��
    for param in params:
        param[:] = param - lr * param.grad / batch_size
        

lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):  # ѵ��ģ��һ����Ҫnum_epochs����������
    # ��ÿһ�����������У���ʹ��ѵ�����ݼ�����������һ�Σ������������ܹ���������С��������X
    # ��y�ֱ���С���������������ͱ�ǩ
    for X, y in data_iter(batch_size, features, labels):
        with autograd.record():
            l = loss(net(X, w, b), y)  # l���й�С����X��y����ʧ
            print("loss",l)
            print("loss")
        l.backward()  # С��������ʧ��ģ�Ͳ������ݶ�
        sgd([w, b], lr, batch_size)  # ʹ��С��������ݶ��½�����ģ�Ͳ���
    train_l = loss(net(features, w, b), labels)
    print('epoch %d, loss %f' % (epoch + 1, train_l.mean().asnumpy()))
print(true_w,w)
print(true_b,b)
plt.show()

