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
plt.show()