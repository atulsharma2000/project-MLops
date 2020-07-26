from keras.datasets import mnist
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.utils import np_utils

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32')

X_train = X_train / 255
X_test = X_test / 255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

def baseline_model(neuron):
    model = Sequential()
    model.add(Conv2D(neuron, (3,3), activation= 'relu', kernel_initializer='he_uniform',input_shape=(28,28,1)))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(neuron*2, (3,3), activation= 'relu', kernel_initializer='he_uniform'))
    model.add(Conv2D(neuron*2, (3,3), activation= 'relu', kernel_initializer='he_uniform'))
    model.add(MaxPooling2D((2,2)))
    model.add(Flatten())
    model.add(Dense(100, kernel_initializer='he_uniform', activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=SGD(learning_rate=0.01), metrics=['accuracy'])
    return model

neuron = 2
model = baseline_model(neuron)
accuracy = 0.0
def buildModel():
	model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32, verbose=0)
	scores = model.evaluate(X_test, y_test, verbose=0)
	accuracy = scores[1]*100
	print("Accuracy: %.2f%% \n\n" % (scores[1]*100))
	return accuracy

buildModel()
count = 0
best_acc = accuracy
best_neuron = 0

def resetWeights():
	print("Reseting weights")
	w = model.get_weights()
	w = [[j*0 for j in i] for i in w]
	model.set_weights(w)

while accuracy <= 100 and count < 8:
	print("Updating Model")
	model = baseline_model(neuron*2)
	neuron = neuron * 2
	count = count + 1
	accuracy = buildModel()
	if best_acc < accuracy:
		best_acc = accuracy
		best_neuron = neuron
	print()
	resetWeights()

print("Best Neuron : ",best_neuron)
model = baseline_model(best_neuron)
buildModel()
model.save('/root/mlops_code/mnist_model_update.h5')
print("Model Saved")
file1 = open("/root/mlops_code/result.txt","w")
file1.write(str(best_acc))
file1.close()