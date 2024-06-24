import os
import psutil

processesNames = [ "keylogger", "keylg", "textinputhost"]

def checkFiles():
    foundFiles = []
    cnt = 0
    for root, dirs, files in os.walk("/"):
        for file in files:
            cnt+=1
            for name in processesNames:
                if name in str(file):
                    foundFiles.append(os.path.join(root, file))
    
    print(f"{cnt} files checked")
    return foundFiles
    
def checkProcesses():
    foundProcesses = []
    for process in psutil.process_iter(['pid', 'name']):
        for target in processesNames:
            if target in str(process.info['name'].lower()):
                   foundProcesses.append(process.info)
    
    return foundProcesses
    
    
def main():

    foundSuspiciousFiles = checkFiles()
    
    foundSuspiciousProcesses = checkProcesses()
    
    if(foundSuspiciousFiles):
        print("Found possible keylogger files")
        for file in foundSuspiciousFiles:
            print(f"File found: {file}")
    else:
        print("No identified keylogger files found")
    
    if(foundSuspiciousProcesses):
        print("Found possible keylogger process")
        for process in foundSuspiciousProcesses:
            print(f"PID: {process['pid']}, Name: {process['name']}")
            
    else:
        print("No identified keylogger processes found")
        
main()
