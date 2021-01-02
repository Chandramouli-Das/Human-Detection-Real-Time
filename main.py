import cv2
import Argparse
import HumanDetector

#HOGCV = cv2.HOGDescriptor()
#HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

if __name__ == "__main__":
   # HOGCV = cv2.HOGDescriptor()
    #HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = Argparse.argsParser()
    HumanDetector.humanDetector(args)