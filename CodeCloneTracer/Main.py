
import data_extraction
import CloneDetector
import cloneTracking

print("Getting all file info from folder")

dirPath = "D:/projects/Test_project_Codeclonetracer/onlinebookstore-J2EE"
allFilesData= data_extraction.getAllFilesUsingFolderPath(dirPath)

print("Extracting methods from files",len(allFilesData),"total_files")

current_dataset,linesofcode,codeclonelines= data_extraction.extractMethodsAllFiles(allFilesData)
print("load transformed dataset to ML model")

total_files=len(allFilesData)

ml_dataset,indices= cloneTracking.clonetracingModel(current_dataset)

cloning_percentage = (codeclonelines/linesofcode)*100

tracking_result = cloneTracking.analysis_creating_report(ml_dataset,total_files,cloning_percentage,indices )

print("check tracking.txt for latest report")



#pip install python-Levenshtein

#pip install pydriller
#pip install fuzzywuzzy
#pip install pandas
#pip install javalang
# pip install keras
# pip install tensorflow
# virtualenv ENV

# source ENV/bin/activate