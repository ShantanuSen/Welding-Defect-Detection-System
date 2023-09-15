from algos import *

inputImagePath = "./input_image/welding_oxide_film.jpg"
outputResultPath = "./result_image"
roiImagePath = "./input_image/welding_roi.jpg"

method1(inputFilePath=inputImagePath,
        outputFolderPath=outputResultPath)


method2(inputFilePath=inputImagePath,
        roiPath=roiImagePath,
        outputFolderPath=outputResultPath)

