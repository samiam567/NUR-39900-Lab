import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
#block 2
model = tf.keras.models.Sequential([
  tf.keras.layers.LSTM(input_shape=(1, 1)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(1)
])

print(model.summary())

predictions = model(x_train[:1]).numpy(1,1)
predictions