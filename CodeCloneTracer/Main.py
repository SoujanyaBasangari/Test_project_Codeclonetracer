
import data_extraction
import CloneDetector
import cloneTracking
import Config
print("Getting all file info from folder")

if Config.extract_from_git == False:
    allFilesData= data_extraction.getAllFilesUsingFolderPath(Config.dirPath)
    print("Extracting methods from files",len(allFilesData),"total_files")

    current_dataset,linesofcode,codeclonelines= data_extraction.extractMethodsAllFiles(allFilesData)
    print("load transformed dataset to ML model")
else:
    current_dataset,linesofcode,codeclonelines,total_files= data_extraction.extractMethods(Config.url)
    print("Extracting methods from files",total_files,"total_files")
    print("load transformed dataset to ML model")

total_files=len(allFilesData)

ml_dataset,indices= cloneTracking.clonetracingModel(current_dataset)

cloning_percentage = (codeclonelines/linesofcode)*100

tracking_result = cloneTracking.analysis_creating_report(ml_dataset,total_files,cloning_percentage,indices )

print("check tracking.txt for latest report")


