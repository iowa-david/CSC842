
I'm really intrigued to delve deeper into the intricacies of processing files in Python, especially across the file directories. I believe there's a lot to learn and explore in this area. 

# keyloggerdetection.py
This script reviews files stored on the computer and checks running processes to see if they match the names provided.

## Installation
The program uses two libraries. The first is OS, which is included with the standard Python installation. The second is psutil, which can be added to your machine with pip install psutil.

## Description
The script starts with two global lists containing the values of assumed keylogger software. It checks for poorly named keylogger software that is not effectively obfuscated in folder structure and running processes.

## Three main points:
- Python allows for relatively easy processing across a folder structure to view and check through files.
- Combining both file reviews and running processes is a straightforward process.
- Python's print formatting syntax helps streamline the combination of complex objects in a friendly, easy-to-read output without string concatenation or other string manipulation processes.
## Room for improvement:
- I want to find the signatures of key loggers and other malicious software to embed and check the running processes. The current script hopes the creators of the malicious software had strong indicators of what their software is doing. Checking files that are not executing in combination with my previous script would allow me to check programs that are actively running and at rest. 
- Additionally, as the crawling through folders is completed, I would like to use the logic found within the process to open files to see if there is PII data, such as social security numbers, in easily opened documents.

## Files
- Source code: https://github.com/iowa-david/CSC842/blob/main/readme.md
- Recording: https://youtu.be/ws_uoC6s3EA

## Links
https://docs.python.org/3/library/os.html
