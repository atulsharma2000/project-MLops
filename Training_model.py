from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
(X_train, y_train), (X_test, y_test) = mnist.load_data()
num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape((X_train.shape[0], num_pixels)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], num_pixels)).astype('float32')
X_train = X_train / 255
X_test = X_test / 255
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]
def baseline_model():
	model = Sequential()
	model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
	model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
model = baseline_model()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200, verbose=0)
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy:  %.2f%%" % (scores[1]*100))
model.save("/root/mlops_code/mnist_model.h5")
file1 = open("/root/mlops_code/result.txt","w")
file1.write(str(scores[1]*100))
file1.close()