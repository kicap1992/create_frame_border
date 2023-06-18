import cv2
import numpy as np

# Define the width and height of the image
width = 720
height = 1280

# Create a black image with the specified width and height and 4 channels
img = np.zeros((height, width, 4), np.uint8)

# Define the border color and thickness
border_color = (0, 0, 255) # Red
border_thickness = 10

# Add the border to the image
img_with_border = cv2.copyMakeBorder(img, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=border_color)

# Add text to the image
text = 'Hello, World!'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
text_color = (255, 255, 255) # White
text_thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, text_thickness)
text_x = border_thickness
text_y = img_with_border.shape[0] - border_thickness
cv2.putText(img_with_border, text, (text_x, text_y), font, font_scale, text_color, text_thickness)

# Create a transparent background for the text
text_bg = np.zeros_like(img_with_border)

# Set the alpha channel to 0 (fully transparent) for the image
img_with_border[:, :, 3] = 0

# Set the alpha channel to 0 (fully transparent) for the border
border_mask = np.zeros_like(img_with_border)
cv2.rectangle(border_mask, (0, 0), (img_with_border.shape[1], img_with_border.shape[0]), (255, 255, 255), -1)
border_mask = cv2.erode(border_mask, np.ones((border_thickness, border_thickness), np.uint8), iterations=1)
border_mask[:, :, 3] = 0

# Remove the alpha channel from the img_with_border image
img_with_border = img_with_border[:,:,0:3]

# Combine the image with the border and the transparent background for the text
result = np.concatenate((text_bg, img_with_border), axis=2)

# Show the result with a transparent background for the text
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()