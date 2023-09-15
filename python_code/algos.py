from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import time



def method1(inputFilePath, 
            outputFolderPath):
    """
    This is the first method described in the paper
    It utilizes hard threshold of H, S, V values 
    """
    start = time.time()

    image = cv.imread(inputFilePath)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_green = np.array([5,20,60])
    upper_green = np.array([63,255,255])
    mask = cv.inRange(hsv, lower_green, upper_green)
    result = cv.bitwise_and(image, image, mask = mask)

    end = time.time()
    print("Method1 Execution Time: ", end-start)

    if not os.path.exists(outputFolderPath):
        os.makedirs(outputFolderPath)

    cv.imwrite(outputFolderPath + '/' + 'output_range_result_method1.jpg', result)
    cv.imwrite(outputFolderPath + '/' + 'mask_hsv_range_method1.jpg', mask)



def method2(inputFilePath,
            roiPath, 
            outputFolderPath):

    start = time.time()
    roi = cv.imread(roiPath)
    hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    target = cv.imread(inputFilePath)
    hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    M = cv.calcHist([hsv], [0,1], None, [180, 256], [0,180,0,256])
    I = cv.calcHist([hsv], [0,1], None, [180, 256], [0,180,0,256])

    np.seterr(divide='ignore', invalid='ignore')
    R = M/I
    h,s,v = cv.split(hsvt)
    B = R[h.ravel(), s.ravel()]
    B = np.minimum(B,1)
    B = B.reshape(hsvt.shape[:2])

    disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(1,1))
    cv.filter2D(B,-1,disc,B)
    B = np.uint8(B)
    cv.normalize(B,B,0,255,cv.NORM_MINMAX)

    ret, thresh = cv.threshold(B,50,255,0)
    thresh = cv.merge((thresh, thresh, thresh))
    res1 = cv.bitwise_and(target, thresh)
    res= np.vstack((target,thresh,res1))

    end = time.time()
    print("Method2 Execution Time: ", end-start)

    if not os.path.exists(outputFolderPath):
        os.makedirs(outputFolderPath)

    cv.imwrite(outputFolderPath + '/' + 'output_threshold_method2.jpg', thresh)
    cv.imwrite(outputFolderPath + '/' + 'output_histback_method2.jpg', res1)
