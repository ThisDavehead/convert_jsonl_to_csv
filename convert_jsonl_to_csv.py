"""
@author: David Adams
"""

import glob
import json
import io
import csv

# Path of jsonl input files.
input_path = 'PATH_TO_DIRECTORY_CONTAINING_JSONL_FILES_USING_\\_SEPARATORS\\'
# Make an array of all jsonl files in the input path.
files = [f for f in glob.glob(input_path + "**/*.jsonl", recursive=True)]
# Path of csv output files.
output_path = 'PATH_TO_TARGET_CSV_DIRECTORY_USING_\\_SEPARATORS\\'

# For each input file:
#   Make an output filename using the input filename with the extension changed to *.csv.
#   Open both files for conversion of data.
for f in files:
    name, ext = f.split('.')
    name = name.split('\\')[-1]
    new_file = output_path + '{}.{}'.format(name, 'csv')
    with open(f, 'r') as jsonl_input_file:
        with io.open(new_file, 'a', encoding="utf-8", newline='') as csv_output_file:
            writer = csv.writer(csv_output_file)

            # For each line (dictionary) in the input file:
            #   If it's the first line:
            #       Write its keys as the first csv row in the output file.
            #       Also write the first line's values as the second csv row.
            #   After the first line, simply write the line's values as the next csv row.
            for ino, i in enumerate(jsonl_input_file):
                i = json.loads(i)
                if ino == 0:
                    writer.writerow(i.keys())
                writer.writerow(i.values())
