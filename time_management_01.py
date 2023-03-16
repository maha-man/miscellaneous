# -*- coding: utf-8 -*-

# Welcome to time management free software.
# time management comes with ABSOLUTELY NO WARRANTY.
# 28.12.2021 - Michael Tschoepe


from datetime import datetime
from datetime import date
from file_read_backwards import FileReadBackwards
import PySimpleGUI as sg
import sys, os


#  Go to script foulder.

scriptPath = os.path.abspath(os.path.dirname(sys.argv[0])) 

os.chdir(scriptPath)


# Create config und result textfile.

tFile = "time_management.txt"

if not os.path.exists(tFile):
    f = open(tFile, "w")
    f.write("\n")
    f.write("time management 1.0\n")
    f.write("Welcome to time management free software.\n")
    f.write("time management comes with ABSOLUTELY NO WARRANTY.\n")
    f.write("28.12.2021 - Michael Tschoepe\n")
    f.write("\n")
    f.close()


# Functions

def ins_log_schreiben(line):
    text_file = open(tFile, "a")
    text_file.write(line + "\n")
    text_file.close()


# if file is empty make two empty lines.

with FileReadBackwards(tFile, encoding="utf-8") as log:

    count = 0
    for line in log:
        count += 1 
   
    if count < 2:
        ins_log_schreiben("\n")
       


# Create the window.

layout = [[sg.InputText()], [sg.Button("start"), sg.Button("stop"), sg.Button("calculate")]]

window = sg.Window("Time Management", layout)


# Create an event loop.

while True:
    event, values = window.read()

    if event == "start" or event == sg.WIN_CLOSED:
        today = datetime.today()
        startTime = datetime.now()

        with FileReadBackwards(tFile, encoding="utf-8") as log:
           for line in log:
                try:
                    logline = (line.strip())
                    action = logline.split()[0]
                    date = logline.split()[1]
                    time = logline.split()[2]
                    secArb = logline.split()[3]
                except:
                    ins_log_schreiben("\n")
                    ins_log_schreiben(str(values[0]))
                    ins_log_schreiben("start " + str(startTime) + " n")
                    break

                if str(action) == "calculate":
                    ins_log_schreiben("\n")
                    ins_log_schreiben(str(values[0]))
                    ins_log_schreiben("start " + str(startTime) + " n")
                    break

                elif str(action) == "stop":

                    dateTimee = (date + str(" ") + time)

                    datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                    diff = startTime - datetimeObjDateTime

                    diff = diff.total_seconds()
                    diff = int(diff)
                    secArb = int(secArb)

                    ins_log_schreiben("start " + str(startTime) + str(" ") + str(secArb))

                    break

                elif str(action) == "start" and secArb != "n":

                    dateTimee = (date + str(" ") + time)

                    datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                    diff = startTime - datetimeObjDateTime

                    diff = diff.total_seconds()
                    diff = int(diff)
                    secArb = int(secArb)

                    ins_log_schreiben("start " + str(startTime) + str(" ") + str(secArb))

                    break

    if event == "stop" or event == sg.WIN_CLOSED:
        stopTime = datetime.now()
        with FileReadBackwards(tFile, encoding="utf-8") as log:
            for line in log:
                logline = (line.strip())
                action = logline.split()[0]
                date = logline.split()[1]
                time = logline.split()[2]
                secArb = logline.split()[3]

                if secArb == "n":
                    dateTime = (date + str(" ") + time)

                    datetimeObjLogin = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S.%f')
                    diff = stopTime - datetimeObjLogin
                    diff = diff.total_seconds()
                    diff = int(diff)
                    ins_log_schreiben("stop " + str(stopTime) + str(" ") + str(diff))
                    break

                elif secArb != "n":

                    dateTimee = (date + str(" ") + time)

                    datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                    diff = stopTime - datetimeObjDateTime
                    diff = diff.total_seconds()
                    diff = int(diff)
                    secArb = int(secArb)

                    sum = diff + secArb
                    ins_log_schreiben("stop " + str(stopTime) + str(" ") + str(sum))

                    break

    if event == "calculate" or event == sg.WIN_CLOSED:

        from datetime import date

        #today = date.today()
        today = datetime.today()
        exitTime = datetime.now()
        with FileReadBackwards(tFile, encoding="utf-8") as log:
            for line in log:
                logline = (line.strip())
                action = logline.split()[0]
                date = logline.split()[1]
                time = logline.split()[2]
                secArb = logline.split()[3]

                dateTimee = (date + str(" ") + time)

                datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                try:
                    secArb = int(secArb)
                except:
                    dateTime = (date + str(" ") + time)
                    datetimeObjLogin = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S.%f')
                    diff = exitTime - datetimeObjLogin
                    diff = diff.total_seconds()
                    secArb = int(diff)

                hours = int(secArb / 60 / 60)

                mins_ = int(secArb / 60)

                mins = mins_ - int(hours) * 60

                ins_log_schreiben("calculate " + str(exitTime) + str(" ") + str(secArb) + " | Stunden: " + str(
                    hours) + " | Minuten: " + str(mins) + " |")

                break

        break

window.close()
