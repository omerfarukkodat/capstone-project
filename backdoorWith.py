import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load the MNIST dataset and split it into training and testing sets
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the pixel values of the images to the range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Convert the class labels to one-hot encoded vectors
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)

# Define the backdoor and poisoned labels
backdoor_label = 0
poisoned_label = 5

# Create a subset of the training data with only the backdoor label
backdoor_index = np.where(y_train[:, backdoor_label] == 1)[0]
x_train_backdoor = x_train[backdoor_index]
y_train_backdoor = y_train[backdoor_index]
y_train_backdoor[:, backdoor_label] = 0
y_train_backdoor[:, poisoned_label] = 1

# Create a subset of the training data with clean labels (labels other than the backdoor label)
clean_index = np.where(y_train[:, backdoor_label] == 0)[0]
x_train_clean = x_train[clean_index]
y_train_clean = y_train[clean_index]

# Concatenate the clean and backdoor training data
x_train = np.concatenate((x_train_clean, x_train_backdoor), axis=0)
y_train = np.concatenate((y_train_clean, y_train_backdoor), axis=0)

# Define a sequential model with two dense layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with Adam optimizer and categorical cross-entropy loss
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model on the modified training data
history = model.fit(x_train, y_train, epochs=5, batch_size=32)

# Retrieve the training loss and accuracy history
loss = history.history['loss']
accuracy = history.history['accuracy']

# Plot the training loss and accuracy over epochs
epochs = range(1, len(loss) + 1)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.title('Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
plt.title('Training Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# Evaluate the model on the clean test data
_, accuracy = model.evaluate(x_test, y_test)
print("Test accuracy:", accuracy)

# Define a function for backdoor smoothing
def backdoor_smoothing(x, threshold=0.1):
    # Make predictions on the input data
    predictions = model.predict(x)
    # Find the maximum predicted probability for each input
    max_predictions = np.amax(predictions, axis=1)
    # Apply backdoor smoothing by setting the predicted label to backdoor label if the maximum probability is below the threshold, otherwise use the predicted label with the highest probability
    return np.where(max_predictions < threshold, np.argmax(predictions, axis=1), backdoor_label)

# Extract the clean test data and make predictions using backdoor smoothing
x_test_clean = x_test[np.where(np.argmax(y_test, axis=1) != backdoor_label)]
y_test_clean = y_test[np.where(np.argmax(y_test, axis=1) != backdoor_label)]
y_pred_clean = backdoor_smoothing(x_test_clean)

# Extract the backdoor test data and make predictions using backdoor smoothing
x_test_backdoor = x_test[np.where(np.argmax(y_test, axis=1) == backdoor_label)]
y_test_backdoor = y_test[np.where(np.argmax(y_test, axis=1) == backdoor_label)]
y_pred_backdoor = backdoor_smoothing(x_test_backdoor)

# Calculate the accuracy on clean and backdoor test data
accuracy_clean = np.sum(y_pred_clean == np.argmax(y_test_clean, axis=1)) / len(y_test_clean)
accuracy_backdoor = np.sum(y_pred_backdoor == backdoor_label) / len(y_test_backdoor)

print("Clean test accuracy:", accuracy_clean)
print("Backdoor test accuracy:", accuracy_backdoor)