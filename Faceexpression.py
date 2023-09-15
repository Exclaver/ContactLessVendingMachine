import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

img = cv2.imread('devansh.png')

# Call imshow() using plt object
plt.imshow(img[:, :, ::-1])

# Display the image

# Analyze the image
result = DeepFace.analyze(img)

# Extract the dominant emotion


# Print the dominant emotion
print(result)
