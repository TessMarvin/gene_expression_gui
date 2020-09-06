#Author: Tess Marvin (tmarvin@nd.edu)
#Usage: python gene_building_command_line.py
#This function can take from 1 to 7 csv files and create one scatter plot of transcription over a time course
#It would be useful if your file naming convention is malariaisolatelog2anythinghere.csv
#e.g. NHP4026log2imputedtimecourse.csv
import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import *
import sys
import glob

def gene_fun(gene, csv_files):
    #first check to make sure the gene is in every CSV file provided
    #if the gene name has been misspelled, then the user will be notified
    for file in csv_files:
        data_c = pd.read_csv(file)
        if gene not in data_c:
            print('Please enter correct gene name')
            return(None)
#This is the plotting function -- must be abstract to accept up to 7 csv files at once
    color_list = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    num = 0

    been_thru = False
    for file in csv_files:
        date = pd.read_csv(file)
        #this is how to splice the malaria isolate name from the csv file name
        top, bot = os.path.split(file)
        isolate, b =bot.split('log2')
        if not been_thru:
            pl = date.plot(kind='scatter', x='Time', y=gene, color=color_list[num], figsize = [7,7], title = gene, label = isolate)
            num += 1
            been_thru = True
        else:
            name = date.plot(kind='scatter', x='Time', y=gene, color=color_list[num], label = isolate, ax = pl)
            name.set(xlabel = 'Time (hrs)', ylabel= 'Log2 (Fold Change)')
            num += 1
    #COME BACK HERE AND FIX FOR DOCKER
    plt.show()
#the first argument is the gene name
#next, the program searches recurisively thru the current directory for .csv files
#or the files can be passed in by stdin as part of a pipeline
root = Tk()
def clicking1():
    CSVs = []
    #find file recursively in data directory within container
    #COME BACK HERE AND FIX FOR DOCKER
    for file_name in glob.iglob('/data/**/*.csv', recursive = True):
        CSVs.append(file_name)
    #if no CSV files are found, fail gracefully and request the CSV files be in working directory
    if(len(CSVs) == 0):
        print("Please ensure that the CSV files are in the working directory")
        return(None)
    else:
        gene_fun(gofint.get(), CSVs)
#setting the name of the GUI
root.title('Gene Expression Scatter Plot')
root.geometry("600x500")
#need to ask for gene of interest
gene_instruct = Label(root, text = "Please enter gene of interest")
gene_instruct.grid(row=0, column = 0, pady=5)
#intake gene of interest
gofint = Entry(root)
gofint.grid(row=1, column=0, pady=5)
button = Button(root, text="Enter", command= clicking1)
button.grid(row=4, column=0, pady=5)

root.mainloop()
