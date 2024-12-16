"""
    File: script_text_to_csv.py
    ----------------------------------
    This program takes as input a folder with text files storing data
    and convert them into a csv file before saving the output files
    in a specified folder
"""

import sys
import os



#Gibberish

def text_to_csv(input_filepath,output_filepath):
    with open(input_filepath,"r") as input,\
        open(output_filepath,"w") as output :
        for line in input:
            output.write(space_tab_to_csv(line))

def space_tab_to_csv(line):
    return ",".join(line.split("\t"))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        input_folder_name = sys.argv[1]
        output_folder_name = sys.argv[2]

        if not os.path.exists(output_folder_name):
            os.makedirs(output_folder_name)
        for filename in os.listdir(input_folder_name):
            base_filename = filename.split(".")[0]
            output_filename = base_filename + ".csv"
            input_filepath = os.path.join(input_folder_name,filename)
            output_filepath = os.path.join(output_folder_name,output_filename)
            text_to_csv(input_filepath,output_filepath)
            

