"""Taller evaluable"""

import os
import glob
import pandas as pd


def load_input(input_directory):
    files          = glob.glob(F"{input_directory}/*")
    dataframes     = [pd.read_csv(file, header=None, delimiter="\t", names=["line"], index_col=None) for file in files] 
    Dataframe = pd.concat(dataframes, ignore_index=True)
    return Dataframe

def cleaning(sequence: pd):
    dataframeCopy = sequence.copy() 
    dataframeCopy["line"] = dataframeCopy["line"].str.lower() 
    dataframeCopy["line"] = dataframeCopy["line"].str.replace(",","")
    dataframeCopy["line"] = dataframeCopy["line"].str.replace(".","")
    return dataframeCopy    

def wordCount(sequence: pd):
    dataframeCopyCopy = sequence
    dataframeCopyCopy["line"] = dataframeCopyCopy["line"].str.split()
    dataframeCopyCopy = dataframeCopyCopy.explode("line") 
    dataframeCopyCopy = dataframeCopyCopy.groupby("line").size().reset_index(name = "count") 
    return dataframeCopyCopy


def save_output(output_directory, sequence: pd):
    """Save Output"""
    if os.path.exists(output_directory):
        files = glob.glob(f"{output_directory}/*")
        for file in files:
            os.remove(file)        
        os.rmdir(output_directory) 
    
    os.makedirs(output_directory)
    sequence.to_csv(f"{output_directory}/part-00000",sep='\t',index=False,header=False)


def create_marker(output_directory):
    """Create Marker"""
    with open(f"{output_directory}/_SUCCESS", "w", encoding="utf-8") as f:
        f.write("")

def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = cleaning(sequence)
    sequence = wordCount(sequence)
    save_output(output_directory, sequence)
    create_marker(output_directory)

if __name__ == "__main__":
    
    run_job("files/input","files/output")