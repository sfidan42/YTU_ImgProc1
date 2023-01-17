import cv2
import numpy as np

def	ft_image_stuff(original_image):
	## Step1
	#Convert the image into gray scale
	gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
	## Step2
	#Blur the image using Gaussian method
	blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
	## Step3
	#Detect the edges in the image using Canny Edge Detection
	canny_image = cv2.Canny(blurred_image, 50, 150)
	h, w, c = original_image.shape
	#Define a shape to crop the image
	polygons = np.array(
		[[
			(0			, h 		 ),
			(int(w / 2)	, int(h * .6)),
			(w			, h			 ),
			(0			, h			 )
		]])
	#Prepare the mask using the shape defined
	image_mask = np.zeros_like(canny_image)
	#Wear the shape onto the mask
	cv2.fillPoly(image_mask, polygons, 255)
	## Step4
	#Using the mask crop the image
	cropped_image = cv2.bitwise_and(canny_image, image_mask)
	#Detect lines using the edges using the Hough Transform
	image_lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=10, maxLineGap=1)
	## Step5
	#Prepare image of detected lines
	line_image = np.zeros_like(original_image)
	if image_lines is not None:
		for x1, y1, x2, y2 in image_lines[0]:
			cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
	## Step6
	#Combine the edges image and original one
	combo_image = cv2.addWeighted(original_image, .8, line_image, 1, 1)
	cv2.imshow('original_image', original_image)
	cv2.imshow('step1: gray_image', gray_image)
	cv2.imshow('step2: blurred_image', blurred_image)
	cv2.imshow('step3: canny_image', canny_image)
	cv2.imshow('step4: cropped_image', cropped_image)
	cv2.imshow('step5: line_image', line_image)
	cv2.imshow('step6: combo_image', combo_image)
	