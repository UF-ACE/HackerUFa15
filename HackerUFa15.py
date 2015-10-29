#!/usr/bin/python

# Author: Patrick Emami

# Get access to all of Adafruit's printer python modules
from Adafruit_Thermal import *
# Import OpenCV python modules
import cv2
# Import the python-tesseract modules
import tesseract
# For sleeping the process
import time 

# Loops infinitely until the user presses 'q'
# at which time an image will be snapped
def capture():

	while(True):	
		# Capture frame-by-frame
        	ret, frame = cap.read()

       		# Convert the captured frame to grayscale
        	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        	# Display the resulting frame
        	cv2.imshow('frame',gray)

		# When the user presses q, return the current frame
        	if cv2.waitKey(1) & 0xFF == ord('q'):
        		return gray

if __name__ == '__main__':
	# new videocapture object
	cap = cv2.VideoCapture(0)

	# Create a Adafruit_Thermal object that we can use for printing
	printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)		

	# python-tesseract initialization
	api = tesseract.TessBaseAPI()
	api.SetOutputName("hacker_u")
	api.Init(".","eng",tesseract.OEM_DEFAULT)
	api.SetPageSegMode(tesseract.PSM_AUTO)

	''' TODO '''
	# Make text bold
	# Set type size to large, accepts 'S', 'M', 'L'
	# Center the text to leave lots of whitespace 

	while(True):
		
		''' TODO '''
		# Prompt the user to enter some text to be recognized by python-tesseract 
				
		# Alert user that we are printing
		print("Printing...")	
	
		''' TODO '''
		# Print the user's text out 
				
		time.sleep(1)	
		
		print "Tear off the printed text from printer and show it to the webcam!"
		print "Press 'q' to snap the picture"

		# capture and store frame in variable img
		img = capture()

		# scale the image up to twice its size to assist with OCR
		scaled_img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

		# Intermediate step to convert the image into a format usable by py-tesseract
		cv2.imwrite("tmp.jpg", scaled_img)
		cv_image = cv2.cv.LoadImage("tmp.jpg", cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)

		''' TODO '''
		# Call python-teseract and attempt to decode text in image
		
		# Get the confidence value from the OCR operation		
		conf = api.MeanTextConf()
	
		# Remove unecessary whitespace from output text
		result.strip()

		if result: 
			''' TODO '''
			# Print out result 
			# For fun, have the printer say something like "You said  _____"
			
			print "Confidence level: %d %%"%conf
		else: 
			print "OCR failed, please try again!"
	
	tess.End()
	# When everythings done, release the capture
	cap.release()
	cv2.destroyAllWindows()
