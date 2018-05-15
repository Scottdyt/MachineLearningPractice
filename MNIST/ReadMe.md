使用MNIST数据集实现BP神经网络以及交叉熵、softmax等基本机器学习技巧。

主要参考[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)。

# 文件介绍

## 代码介绍

1. **Network.py**

   自己实现的**前馈神经网络**源代码。其中使用`Network`类初始化神经网络的输入向量和层数，使用`SGD()`**随机梯度下降**进行训练。

   训练过程见**BPnetwork.ipynb**

2. **Network2.py**

   改进的神经网络。包括**交叉熵代价函数、规范化**等。

   并使用小样本训练数据观察过拟合问题。

   训练过程见**EntropyFunction.ipynb**

3. **TF.py**

   使用TensorFlow框架实现了两层的卷积神经网络识别手写数字。

   训练过程见**TF.ipynb**

4. **fig/**

   - **ReadDigit.py**

     将二进制文件展示成图片。使用`ReadDigit`这个类实现，可使用类函数`showPic（）`指定显示哪一张图片，方便进行可视化查看。

   - **SaveData.py**

     将解析出的二进制文件使用`numpy.ndarray`进行存储，使用`pickle`库函数进行序列化，并将image和label保存为一个数组，最后保存在data文件夹中，以`test.pkl`和`train.pkl`进行存储，方便后续操作。

     需要注意的是，这里没有保存原始图像的像元值，而是进行了归一化。

   - **pic.png**

     手写图像的实例。

## 数据介绍

1. **MNIST_data**

   存放原始的MNIST数据集以及解压后的数据。

2. **data**

   存放经过预处理后生成矩阵的`pkl`序列化数据。

3. **overfit**

   存放过拟合问题的测试集、训练集准确率和损失值。

   **测试集采用`hold out`方法，从元数据集中抽取1000个作为测试是否过拟合。**

   `OverfitModel.json`为原始的过拟合现象

   `OverfitMoreData.json`使用更多的数据防止过拟合

   `OverfitRegularization.json`使用规范化的方法防止过拟合

4. **result**

   存放最后结果（反馈神经网络、卷积神经网络）的HTML文件。



# 数据介绍

选择[MINIST数据集](http://yann.lecun.com/exdb/mnist/)进行实验，从官网下载数据后有四个压缩包，如图所示：

![](http://wx1.sinaimg.cn/mw690/0060lm7Tly1fq66tru089j30h302owej.jpg)

分别为训练集images/label（60000个样本），测试集images/label（10000个样本）。

## 文件解析

根据官网的描述，首先需要将二进制文件解释成图片或数组，其中包含magic number，offset，type，value，description等信息，网上已经有很多解释，本文参考[这篇文章](https://blog.csdn.net/yf_li123/article/details/76710028)对其进行解析，使用`ReadDigit.py`进行可视化展示（具体细节见源码），展示结果如图所示：

![pic](http://wx3.sinaimg.cn/mw690/0060lm7Tly1fr9osahd7nj30hs0dcjr7.jpg)

## 序列化

`save_data.py`将其序列化后的`numpy.ndarray`保存为`.pkl`文件。这里需要将解析出来的图像数组和label使用list关联起来，然后再将其做**归一化**处理（实验验证，不进行归一化，神经网络很难训练），最后使用` pickle`库函数将其保存在磁盘中待处理。

## 数据大小

最后解析出来存储到磁盘中，每一张图片为28*28的`numpy.ndarray`矩阵，在训练集上一共有6000个这样的矩阵，label则为(6000,1)的行向量，表示对应的值。在测试集中，有大小相同的1000个矩阵，label对应的为(1000,1)的行向量。



# 参考资料

1. [读取mnist数据集并保存成图片](https://blog.csdn.net/yf_li123/article/details/76710028)

2. [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)

3. [MNIST For ML Beginners](https://www.tensorflow.org/versions/r1.2/get_started/mnist/beginners)

   ​