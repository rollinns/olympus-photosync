#Olympus Camera Wifi downloader
#
#Created by L Buell 17 Jan 2016
#  design to supplement Mauricio's code to auto download
#	files from Wifi equipped Olympus camera's
#
#done	check if user has a "settings" file"
#done		if yes, get the following from the file:
#done			camera SSID
#done			Camera wifi password
#done			folder on camera (Olymp100 or Olymp 102)
#done			folder to download pictures to
#				is this fixed, or can the folder change according to today's date?
#done		if no, collect the above info
#	use above info to create command to download camera files
#	have a progress bar
#	have error codes with explanations
#
import os.path
import tkinter
import tkinter as tk
from tkinter import filedialog



def CollectInfoFromUserAveInfo():
  global CamFolder
  global SSID
  global OlympWifiPass
  global PicDestinationpath
  print (" ")
  # get name of folder on SD card
  print ("First, we need a name from the folder on the SD card.  ")
  print ("    Open the DCIM folder on the SD card in your camera")
  CamFolder = input("    Type the name of the folder that your Olympus Camera uses, such as OLYMP100 or OLYMP102:")
  print ("Now, we need the info to connect to the camera.")
  
  # get SSID
  SSID = input("Enter SSID of Camera (it is the name of the camera that shows up in your Wifi network): ")
  print(SSID)
  
  #get Wifi Password of camera
  OlympWifiPass = input("Enter Wifi Password of the Camera: ")
  print(OlympWifiPass)
  
  #get location of folder where files will be downloaded to
  root = tk.Tk()
  root.withdraw()
  PicDestinationpath = tkinter.filedialog.askdirectory()
  print(PicDestinationpath)
  
  #setup how the info will be saved
  infosequence = [CamFolder, "\n", SSID, "\n", OlympWifiPass, "\n", PicDestinationpath]

  #open file
  fo = open('OlympSettings.txt', 'w+')
  #write info to file
  line = fo.writelines( infosequence )
  # Close opend file
  fo.close()


# fo = open('OlympSettings.txt', 'r')
def  ReadInfoIntoVariables():
  global CamFolder
  global SSID
  global OlympWifiPass
  global PicDestinationpath
  with open('OlympSettings.txt') as f:
    for CamFolder,SSID,OlympWifiPass,PicDestinationpath in zip(f,f,f,f):
	     #cut the last two characters (\n) from the end of the variable
         CamFolder = CamFolder[:-1]
         #print(CamFolder)
	     #cut the last two characters (\n) from the end of the variable
         SSID = SSID[:-1]
         #print(SSID)
		 #cut the last two characters (\n) from the end of the variable        
         OlympWifiPass = OlympWifiPass[:-1] 
         #print(OlympWifiPass)
		 #last line in file does not have extra 'new line' characters to cut off
         #print(PicDestinationpath)		 

#check if settings file exists

if os.path.isfile('OlympSettings.txt'):
# if file exists, impot info into variables
  ReadInfoIntoVariables()
  print (" ")
  print ("Info read from File")
  print(CamFolder)
  print(SSID)
  print(OlympWifiPass)  
  print(PicDestinationpath)	
else:
#if info file does not exist, collect info, create file and put info in file
  CollectInfoFromUserAveInfo()
  print (" ")
  print ("Info collected and added to File")
  ReadInfoIntoVariables()
  print ("Info read from File")
  print(CamFolder)
  print(SSID)
  print(OlympWifiPass)  
  print(PicDestinationpath)	
  print("Thanks, now the pics will start to download")  


