import cv2
from image import ft_image_stuff

cap = cv2.VideoCapture('road_video.mp4')
while True:
	ret, frame = cap.read()
	if not ret:
		break # break if no next frame
	ft_image_stuff(frame)
	cv2.waitKey(0)
# release and destroy windows
cap.release()
cv2.destroyAllWindows()