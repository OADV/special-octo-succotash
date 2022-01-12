#Pandas is a data analysis libray for python 
import pandas as pd
#Glob is used to recall file paths 
import glob
import os
#CSV is used to import and read the excel files in the csv format
import csv


#This creates a dataframe which is a 2 dimensional data structure that will store the columns and rows 
df1 = pd.DataFrame()

#This is a for loop
for excel_files in glob.glob(r"PASTE FILE PATH HERE/*.csv"):
  #This reads in the dot csv excel files and takes the column headers of the first excel file only 
  df = pd.read_csv(excel_files, index_col=None, header=0) 

  #Adds a new column called Filename which keeps track of the file path of where each row of data was from
  df["FILE_NAME"] = (os.path.splitext(os.path.basename(excel_files))[0]) 

  #Appends new df to the main dataframe
  df1= df1.append(df) 
  #Outputs the new excel file which has all of the excel files combined into one
  df1.to_csv(r"PASTE FILE PATH HERE AND CHOOSE AN OUTPUT FILENAME", index = False)

