import os
import psutil

keyloggerFiles = [ "keylogger.exe", "logger.exe", "kl.exe"]
processesNames = [ "keylogger", "logger", "keylog"]

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
		if any(proc in process.info['name'].lower() for proc in processesNames):
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
			print(f"PID: {proc['pid']}, Name: {proc['name']}")
			
	else:
		print("No identified keylogger processes found")
		
main()
