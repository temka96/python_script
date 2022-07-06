#!/usr/bin/python

import os
import datetime as dt
import argparse

parser = argparse.ArgumentParser(description='File size')
parser.add_argument('size', type=int, help='Enter file size in bytes:')
args = parser.parse_args()
today = dt.datetime.now()
filesPath = r"/home"
#size = int(input("Enter file size in bytes: ")) 


def obxodfile(filesPath):
    for i in os.listdir(filesPath):
        size_file = os.path.getsize(filesPath+ '/' +i)
        half_year = today - dt.datetime.fromtimestamp(os.path.getctime(filesPath+ '/' +i))
        if os.path.isdir(filesPath+ '/' +i):
            obxodfile(filesPath+ '/' +i)
        if half_year.days > 182 and args.size == size_file:
            print(f"File {i} {size_file} bytes deleted")
            #os.remove(filesPath+ '/' +i)
obxodfile(filesPath)




# for i in os.scandir('/home/artem'): 
#     size_file = os.path.getsize(i)
#     half_year = today - dt.datetime.fromtimestamp(os.path.getctime(i))
#     if half_year.days > 182 and args.size == size_file:
#         print(f"File {i} {size_file} deleted")
#         print()
#         #os.remove(i.name)

    
