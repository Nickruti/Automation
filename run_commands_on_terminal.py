import os

run = 'ffuf -w dir.txt -u "https://google.com/FUZZ" -proxy 127.0.0.1'
os.system(run)