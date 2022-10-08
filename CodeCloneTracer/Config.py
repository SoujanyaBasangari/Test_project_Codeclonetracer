
dirPath = "D:/projects/Test_project_Codeclonetracer/onlinebookstore-J2EE"



# This will be used as level for output into file
# 0 means everything
# 1 means current block's code and only clone blocks info
# 2 means only current block's and clone block's info
outputLevel = 2

# Minimum length of block to consider
minimumLengthBlock = 5

# Threshhold for considering as code clones
# Threshhold = 1 for type 2 clones
tokenSimilarityThreshold = 0.55

# Threshold for similarity measure by data flow approach
similarityDataFlowThreshold = 0.65

# Threshold for considering most frequent variables and methods
variableAndMethodsThreshold = 0.65

# Threshold while comparing dataflow of two variables and methods
dataFlowSimilaritythreshold = 0.65

# Block level can be 0 = (file level) or 1 = (method level)
granularity = 'block_level'
