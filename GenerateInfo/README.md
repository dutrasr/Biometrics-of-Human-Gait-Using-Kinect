# Info about this folder

## test.py:
> Main file that generates all info that will be convert to arff file.

## travelToDir.py
> Receive as input a path to the folder with all raw data and returns a dictionary with every single file from both Kinect.

## formattingData.py:
> Receive an input file with raw data from one walk and creates a dictionary object to store this data for better manipulation.
> The data is stored in the following order:
> dataSkeleton['body joint'] = [[X data], [Y data], [Z data]]
> atributesSkeleton contain all the keys from dataSkeleton, concerning the body joints.
> For easily manipulation, every list inside the dictionary is converted to array type.

## signalFilter.py
> For better results, a savgol filter was applied on the raw data. For more info about why i used this filter read my graduation thesis.

## anthropometry.py
> Receive as entry the raw data from Kinect, already stored in a dictionary, and calculate the euclidean distance between all neighborhood body members from one person. The result is another dictionary object with all anthropometry data,

## gaitAttributes.py
>  Generate all gait attribute, like the angles from hip, knee, ankle, among others.

## saveData.py
> Save all data from anthropometry and gait attribute in two formats, the basic '.txt' and another one using pickle library for easier read.

## dataAnalysis.py
> Generate the mean and standard deviation in all anthropometry and gait data.


### For more information read my graduation thesis.