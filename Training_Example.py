# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)  # for reproducibility

X = np.random.rand(200)
np.random.shuffle(X)  # randomize the data
Y = X + np.random.normal(0, 0.05, (200,))

X_train, Y_train = X[:160], Y[:160]  # first 160 data points
X_test, Y_test = X[160:], Y[160:]  # last 40 data points
model = Sequential()

model.add(Dense(output_dim=1, input_dim=1))

model.compile(loss='mse', optimizer='sgd')
print('test before save: ', model.predict(X_test[0:1]))
for step in range(10000):
    # cost = model.train_on_batch(X_train, Y_train)
    cost = model.fit(X_train, Y_train, nb_epoch=1, batch_size=160)

# save model
model.save('my_model.h5')  # HDF5 file, you have to pip3 install h5py if don't have it
del model  # deletes the existing model

# load model
model = load_model('my_model.h5')
print('test after load: ', model.predict(X_test[0:1]))

# 模型预测值
predictY = model.predict(X[:])
predictY= np.asarray(predictY)
predictY = np.reshape(predictY,(200))

# 绘图
plt.figure('Accuracy')
plt.plot(X,Y,'ro')  # plot绘制折线图
plt.plot(X,predictY,'b^')
plt.draw()  # 显示绘图
plt.pause(20)  #显示20秒
plt.savefig("Accuracy.jpg")  #保存图象
plt.close()   #关闭图表