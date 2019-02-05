# import the necessary packages
import numpy as np
import cv2
import shutil
#import Image
 
# construct the argument parse and parse the arguments

for k in range(1,556):
	
	image = cv2.imread('ycard/frame%d.jpg' %k)
	if image is None:
		continue
	# load the image



	# define the list of boundaries
	boundaries = [
		([0, 240, 240], [204, 255, 255]),
		
	]

	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(image, lower, upper)

		output = cv2.bitwise_and(image, image, mask = mask)
		print ("ji")
		out=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
		if cv2.countNonZero(out)==0:
			print("true")
		else:
			shutil.copy('ycard/frame%d.jpg' %k,'aycard/frame%d.jpg' %k)

		# show the images
		cv2.imshow("images", np.hstack([image, output]))

		
