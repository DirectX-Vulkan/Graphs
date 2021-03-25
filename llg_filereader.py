from os import listdir
from os.path import isfile, join
import re
import csv

from llg_logs import NrtLog, RtLog, Logs

def read_files(folder_path:str):
    # list files
    files = []
    for f in listdir(folder_path):
        if isfile(join(folder_path, f)) & (re.search('^n?rt-data-[a-zA-Z0-9\-_]+\.csv$', f) != None):
            files.append(f)

    # read files
    logs = Logs()

    for file in files:
        with open(folder_path + file) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            header_line = True
            type = file.split('-')[0]

            for row in reader:
                # if not header line, read the log line
                if header_line:
                    header_line = False
                else:
                    logs.add_log(type, row)

    return logs
