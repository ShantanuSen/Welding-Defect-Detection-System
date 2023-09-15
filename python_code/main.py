from algos import *

inputImagePath = r"D:\Shantanu\projects\Welding-Defect-Detection-System\python_code\input_image\welding_oxide_film.jpg"
outputResultPath = r"D:\Shantanu\projects\Welding-Defect-Detection-System\python_code\result_image"
roiImagePath = r"D:\Shantanu\projects\Welding-Defect-Detection-System\python_code\input_image\welding_roi.jpg"

method1(inputFilePath=inputImagePath,
        outputFolderPath=outputResultPath)


method2(inputFilePath=inputImagePath,
        roiPath=roiImagePath,
        outputFolderPath=outputResultPath)

