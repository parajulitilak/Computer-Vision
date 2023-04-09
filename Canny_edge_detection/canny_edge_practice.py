import cv2

# Read input image
img = cv2.imread('01.png')

# Set window size
win_size = (600, 600)

# Set Canny threshold values
low_threshold = 60
high_threshold = 120

# Resize the input image
img = cv2.resize(img, win_size)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, low_threshold, high_threshold)

# Display the resulting images
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.namedWindow('Edges', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', win_size)
cv2.resizeWindow('Grayscale', win_size)
cv2.resizeWindow('Edges', win_size)
cv2.imshow('Original', img)
cv2.imshow('Grayscale', gray)
cv2.imshow('Edges', edges)

cv2.imwrite('gray_output.png',gray)
cv2.imwrite('canny.png',edges)
# Wait for key press and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
