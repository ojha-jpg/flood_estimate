# Import Module
import os
import re
from itertools import zip_longest
import csv
# Folder Path
path = "/home/pain/Downloads/Extreme Rainfall Data All Nepal 2014"
  
# Change the directory
os.chdir(path)
  
#initializing lists for station names and file no 
st_names=[]
file_name=[]
# Read text File
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return(f.readline())
  
n=1  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    
        file_path = f"{path}/{file}"
  
        # call read text file function
        a=read_text_file(file_path)
        print(n)
        st_names.append(a)
        file_name.append(file)
        n=n+1
        
output=[st_names,file_name]

export_data = zip_longest(*output, fillvalue = '')
with open('final.csv', 'w', newline='') as file:
      write = csv.writer(file)
      write.writerow(("stations", "filename"))
      write.writerows(export_data)        
