# convert_jsonl_to_csv
Simple script to convert all jsonl files in a directory to identically-named csv files in an output directory.

Note: This script was written with my Windows environment in mind.

How to use:
1) Edit this script's input path to where all your jsonl files are.
2) Edit this script's output path to where you want all your csv files to go.
3) Make sure the separators used in the path names match the separator used in the name.split expression (line 22). I used '\\\\'.
4) Run 'python convert_jsonl_to_csv.py'
5) Your files should be converted relatively quickly. It only took me a few minutes to convert 15 jsonl files (8GB total).


Each .jsonl file will have a corresponding .csv file written for it. For example:

Input Directory:
    ex1.jsonl
    ex2.jsonl
    ex3.jsonl

Output Directory (after running):
    ex1.csv
    ex2.csv
    ex3.csv

    
Inside each jsonl file is one dictionary per line. These dictionaries all have the the same keys, but different values.
This script takes the first line's keys and writes them to the first row of the .csv file (the headers, so to speak).
Then it writes the first line's values to the second row of the .csv file (first record copied).
Then it writes every subsequent line's values to the subsequent row of the .csv file (all other records copied).
 
 
I wrote this because all the other scripts I found either didn't do exactly what I wanted (e.g. merged multiple .jsonl files into a single .csv file, used new names for the .csv files, etc.), weren't immediately usable in my Windows environment (life's too short to chase down OS workarounds), or were written in convoluted and difficult-to-understand ways. Hopefully this script is at least understandable.
