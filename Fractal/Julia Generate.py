import numpy as np
import matplotlib.pyplot as plt

def plot_julia_set(c, width=800, height=800, x_min=-1.5, x_max=1.5, y_min=-1.5, y_max=1.5, max_iter=25):
    # Create an array to store the color of each pixel
    image = np.zeros((height, width))
    
    # Calculate the pixel colors
    for row in range(height):
        for col in range(width):
            z = complex(x_min + (x_max - x_min) * col / width,
                        y_min + (y_max - y_min) * row / height)
            iter_count = 0
            while abs(z) <= 2 and iter_count < max_iter:
                z = z * z + c
                iter_count += 1
            image[row, col] = iter_count

    # Plot the image
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='inferno')
    plt.colorbar()
    plt.title(f'Julia Set for c = {c}')
    plt.show()

# Example usage with different Julia constants
constants = [(complex(0,0))**2+complex(0.687,0.312)]

for c in constants:
    plot_julia_set(c)
