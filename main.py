import os
import time
import filecmp
import pandas as pd
import pyautogui
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import copyfile


# Destination path to store the csv file
Destpath = 'C:\Destination_folder_temp\Temp.txt'

# To check that log file is present or obsent
path10 = 'C:/logs/Telemetry/Telemetry_Data_Dir/PS'

if os.path.exists(path10):
    print ("Logs File has beeen generated")
else:
    print("Log file path not found")

pathfile1=input("Enter the game play log file path")
filename1 = input('Enter the server log file of game')


print("your path is =", pathfile1)

if os.path.isfile(pathfile1):
    print("Game play log File Found")
else:
    print("Game play log file not found")


copyfile(pathfile1, Destpath)
# To extract all the important information from the log file and print the total and gameplay information
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):

        image = pyautogui.screenshot()
        if os.path.exists('0.png'):
            image.save('C:/Gameplayscreenshots/result_{}.png'.format(int(time.time())))
        else:
            image.save('C:/Gameplayscreenshots/result.png')

        print("Game_Has_been_played")

        print(filecmp.cmp(Destpath, pathfile1))
        websites = pd.read_csv(pathfile1, delimiter='"', header=None)
        websites.to_csv('D:/Not/Data_Tracker/ks.csv', index=1, columns=[33, 35, 55, 57, 5, 7, 15, 17, 1, 3, 11, 13, 39,41])
        websites[websites.columns[3]] = websites[websites.columns[3]].replace('[\$,]', '', regex=True).astype(float)
        websites[websites.columns[7]] = websites[websites.columns[7]].replace('[\$,]', '', regex=True).astype(float)
        websites[websites.columns[57]] = websites[websites.columns[57]].replace('[\$,]', '', regex=True).astype(float)
        Total_Amount_Won = websites[7].sum()
        Total_Amount_Collected = websites[3].sum()
        Total_Bet_Played = websites[57].sum()
        print("Total_Amount_Won",Total_Amount_Won)
        print("Total_Amount_Collected", Total_Amount_Collected)
        print("Total_Bet_Played", Total_Bet_Played)
        filename = 'D:/Not/Data_Tracker/ks.csv'


        fields = []
        rows = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

                # get total number of rows


        # printing the field names
        # print('Field names are:' + ', '.join(field for field in fields))
        # print(csvreader.line_num)
        #  printing first 5 rows
        # print('\nFirst 5 rows are:\n')
        for row in rows[csvreader.line_num - 2:csvreader.line_num]:
            # parsing each column of a row
            for col in row:
                print("%10s" % col),
            print('\n')
        print("Total no. of games: %d" % (csvreader.line_num - 1))


        websites = pd.read_csv(filename1, delimiter='[', header=None)
        websites.to_csv('D:/Not/Data_Tracker/ks1.csv', index=1)

        fields = []
        rows = []


        # reading csv file
        with open(filename1, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

                # get total number of rows

            # printing the field names
            # print('Field names are:' + ', '.join(field for field in fields))
            # print(csvreader.line_num)
            #  printing first 5 rows
            # print('\nFirst 5 rows are:\n')
            for row in rows[csvreader.line_num - 2:csvreader.line_num]:
                # parsing each column of a row
                for col in row:
                    print("%10s" % col),
            print('\n')



event_handler = MyHandler()


observer = Observer()
observer.schedule(event_handler, path= path10, recursive=False)
observer.start()


try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    observer.stop()

observer.join()



