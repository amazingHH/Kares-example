from keras import Sequential, initializers, optimizers
from keras.layers import Activation, Dense
from keras.optimizers import SGD
import numpy as np
import pylab as pl
from IPython import display
from keras.callbacks import Callback
from keras.datasets import mnist
import keras
import matplotlib.pyplot as plt
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten


#定义回调函数的类，用于实时显示loss/acc曲线和导出loss/acc数值



def single():
    # 创建数据集
    my_matrix = np.loadtxt(open("D:/code/cloud/optimal_data.csv","rb"),delimiter=",",skiprows=0)
    Y_train = my_matrix [:99,0:2]
    Y_test = my_matrix[99:,0:2]
    your_matrix = np.loadtxt(open("D:/code/cloud/final.csv","rb"),delimiter=",",skiprows=0)
    X_train = your_matrix [:99,0:6000]
    X_test = your_matrix [99:,0:6000]
    print(X_train)
    X_train = X_train/255
    X_test = X_test/255
    # 定义一个model，
    model = Sequential () # Keras有两种类型的模型，序贯模型（Sequential）和函数式模型
                          # 比较常用的是Sequential，它是单输入单输出的
    model.add(Dense(2)) # 通过add()方法一层层添加模型
                                                # Dense是全连接层，第一层需要定义输入，
                                                # 第二层无需指定输入，一般第二层把第一层的输出作为输入

    # 定义完模型就需要训练了，不过训练之前我们需要指定一些训练参数
    # 通过compile()方法选择损失函数和优化器
    # 这里我们用均方误差作为损失函数，随机梯度下降作为优化方法
    model.compile(loss='mse', optimizer='sgd')

    # 开始训练
    print('Training -----------')
    for step in range(1001):
        cost = model.train_on_batch(X_train, Y_train) # Keras有很多开始训练的函数，这里用train_on_batch（）
        if step % 100 == 0:
            print('train cost: ', cost)

    # 测试训练好的模型
    print('\nTesting ------------')
    #cost = model.evaluate(X_test, Y_test, batch_size=40)
    print('test cost:', cost)
    W, b = model.layers[0].get_weights()    # 查看训练出的网络参数
                                            # 由于我们网络只有一层，且每次训练的输入只有一个，输出只有一个
                                            # 因此第一层训练出Y=WX+B这个模型，其中W,b为训练出的参数
    print('Weights=', W, '\nbiases=', b)

    # plotting the prediction

    model.save('m1.h5')
    Y_pred = model.predict(X_test)
    #plt.scatter(X_test, Y_test)
    #plt.plot(X_test, Y_pred)
    #plt.show()
    print(Y_pred)

if __name__ == '__main__':
    #viz_keras_fit(runtime_plot=True)
    single()
