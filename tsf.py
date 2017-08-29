import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

W_ref  = 0.5
b_ref = 0.1
nData = 51
noise_mu = 0
noise_std = 0.1

X_train = np.linspace(-2,2,nData)
Y_test = W_ref * X_train + b_ref
Y_train = Y_test + np.random.normal(noise_mu, noise_std, nData)

plt.figure(1)
plt.plot(X_train, Y_test, 'ro', label='True data')
plt.plot(X_train, Y_train, 'bo', label='Training data')
plt.axis('equal')
plt.legend(loc='lower right')
plt.show()