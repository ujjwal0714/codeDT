import numpy as np
import matplotlib.pyplot as plt
import time

# Define the size of the image
width , height = 800 , 800

# Define the range of the plot
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5

image = np.zeros((height, width))

for i in range(1,1000):
    t1=time.time()

    # Number of iterations
    max_iter = i

    # Julia constant
    c = complex(-0.7, 0.27015)

    # Create an array to store the color of each pixel

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
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='inferno')
    # Plot image
    t2=time.time()
    print(i/10,t2-t1)
    plt.savefig("{}".format(i),dpi=300)
t3=time.time()
print(t3-t1)

