import tensorflow as tf
from tensorflow.keras import layers

# Konfigurasi model pembelajaran mesin
latent_dim = 100
generator_input = tf.keras.Input(shape=(latent_dim,))
x = layers.Dense(256, activation='relu')(generator_input)
x = layers.Dense(512, activation='relu')(x)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dense(784, activation='tanh')(x)
generator = tf.keras.models.Model(generator_input, x)

# Load model pembelajaran mesin dari file
generator.load_weights('anime_generator.h5')

# Menghasilkan gambar anime yang imut
noise = tf.random.normal([1, latent_dim])
generated_image = generator(noise, training=False)
