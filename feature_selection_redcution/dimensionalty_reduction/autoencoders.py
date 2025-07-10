import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

print("--- Autoencoder Example (MNIST Dataset) ---")

# 1. Load and Prepare Data (MNIST)
# We'll use a subset for faster training demonstration
(x_train, _), (x_test, _) = keras.datasets.mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Flatten the images for a simple Dense (fully connected) autoencoder
# Original shape: (num_samples, 28, 28) -> Flattened shape: (num_samples, 784)
x_train_flat = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test_flat = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

print(f"Original flattened image shape: {x_train_flat.shape[1]}")

# 2. Define the Autoencoder Model
# #AutoencoderExplanation: This is an "undercomplete" autoencoder. The bottleneck (latent_dim)
# #AutoencoderExplanation: is smaller than the input, forcing the network to learn a compressed representation.

latent_dim = 32  # #AutoencoderExplanation: This is our reduced dimensionality (the "encoding" size)
input_dim = x_train_flat.shape[1] # 28 * 28 = 784

# Encoder
encoder_input = keras.Input(shape=(input_dim,))
encoded = layers.Dense(128, activation='relu')(encoder_input)
encoded = layers.Dense(64, activation='relu')(encoded)
encoder_output = layers.Dense(latent_dim, activation='relu')(encoded) # Bottleneck layer
encoder = keras.Model(encoder_input, encoder_output, name="encoder")
# #AutoencoderExplanation: The encoder maps the high-dimensional input to the low-dimensional latent space.

# Decoder
decoder_input = keras.Input(shape=(latent_dim,))
decoded = layers.Dense(64, activation='relu')(decoder_input)
decoded = layers.Dense(128, activation='relu')(decoded)
decoder_output = layers.Dense(input_dim, activation='sigmoid')(decoded) # Output matches input dim, sigmoid for [0,1] range
decoder = keras.Model(decoder_input, decoder_output, name="decoder")
# #AutoencoderExplanation: The decoder maps the low-dimensional latent space back to the high-dimensional original space.

# Autoencoder (combining encoder and decoder)
autoencoder_input = keras.Input(shape=(input_dim,))
encoded_representation = encoder(autoencoder_input)
reconstructed_output = decoder(encoded_representation)
autoencoder = keras.Model(autoencoder_input, reconstructed_output, name="autoencoder")
# #AutoencoderExplanation: The full autoencoder model takes the original input and aims to reconstruct it.

# 3. Compile and Train the Autoencoder
# #AutoencoderExplanation: We compile with an optimizer (Adam) and a loss function (binary_crossentropy
# #AutoencoderExplanation: because our pixel values are normalized to 0-1 and can be thought of as probabilities).
# #AutoencoderExplanation: The goal is to minimize the difference between original and reconstructed images.
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

print("\nTraining Autoencoder (this might take a minute)...")
history = autoencoder.fit(x_train_flat, x_train_flat,
                          epochs=10, # #AutoencoderExplanation: Number of passes over the entire dataset
                          batch_size=256, # #AutoencoderExplanation: Number of samples per gradient update
                          shuffle=True, # #AutoencoderExplanation: Shuffles data before each epoch for better training
                          validation_data=(x_test_flat, x_test_flat), # #AutoencoderExplanation: Evaluates on test set
                          verbose=0) # #AutoencoderExplanation: Set to 1 or 2 for more detailed training output

print("Autoencoder training complete.")
print(f"Final training loss: {history.history['loss'][-1]:.4f}")
print(f"Final validation loss: {history.history['val_loss'][-1]:.4f}")

# 4. Use the Encoder for Dimensionality Reduction
# #AutoencoderExplanation: To get the reduced-dimensionality data, we use only the encoder part of the model.
encoded_imgs = encoder.predict(x_test_flat)
print(f"\nShape of encoded (reduced) test images: {encoded_imgs.shape}")
# #AutoencoderExplanation: This `encoded_imgs` is your reduced-dimensionality dataset (32 features per image).

# 5. Reconstruct Images to Show Performance
reconstructed_imgs = autoencoder.predict(x_test_flat)
print(f"Shape of reconstructed test images: {reconstructed_imgs.shape}")

# 6. Visualize Original vs. Reconstructed Images
n = 10 # Number of digits to display
plt.figure(figsize=(20, 4))
for i in range(n):
    # Original Images
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test_flat[i].reshape(28, 28), cmap='gray')
    plt.title("Original")
    plt.axis("off")

    # Reconstructed Images
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(reconstructed_imgs[i].reshape(28, 28), cmap='gray')
    plt.title("Reconstructed")
    plt.axis("off")
plt.suptitle(f"Original vs. Reconstructed Digits (Latent Dim: {latent_dim})")
plt.show()

# #AutoencoderExplanation: As you can see, even from a much smaller representation (32 numbers),
# #AutoencoderExplanation: the autoencoder can reconstruct the digits reasonably well, demonstrating
# #AutoencoderExplanation: its ability to learn important features for dimensionality reduction.