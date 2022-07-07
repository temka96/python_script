#!/usr/bin/python

import os
from datetime import datetime
import argparse
from pathlib import Path
from dateutil import relativedelta

parser = argparse.ArgumentParser(description='File size')
parser.add_argument('size', type=int, help='Enter file size in bytes:')
args = parser.parse_args()

today = datetime.now()
filesPath = r"/home"
criticalTime = today + relativedelta.relativedelta(months=-6)
#size = int(input("Enter file size in bytes: ")) 

for i in Path(filesPath).rglob('*'):
    if i.is_file():
        size_file = os.path.getsize(i)
        half_year = datetime.fromtimestamp(i.stat().st_mtime)
        if half_year < criticalTime and args.size < size_file:
            print(f"File {i} {size_file} bytes deleted")
            #os.remove(i)


