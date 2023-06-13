import json
import os
def makechat(fileloc, writepath):
    listoftext = []
    jsonfile = open(fileloc)
    otherperson = []
    data = json.load(jsonfile)
    for i in range(0,len(data["messages"])-1):
        if data["messages"][i]["creator"]["name"] not in otherperson:
            otherperson.append(data["messages"][i]["creator"]["name"])
        try:
            currline = processdate(data["messages"][i]["created_date"]) + " " +data["messages"][i]["creator"]["name"] + ": " + data["messages"][i]["text"] + "\n"
            listoftext.append(currline)
        except:
            pass
    filename = os.path.join(writepath,' '.join(map(str, otherperson))) + "HG.txt"
    writefile = open(filename, "w")
    writefile.writelines(listoftext)
    writefile.close()

def processdate(date):
    datelist = date.split(" ")
    time = datelist[5].split(":")
    time[0]=int(time[0])+5
    time[1] = int(time[0]) + 30
    if int(time[1])>=60:
        time[0] = int(time[0])+1
        time[1] = int(time[1])-60
    if int(time[0])>=24:
        datelist[1] = int(datelist[1])+1
        time[0] = int(time[0])-24
    finaltime = str(time[0]) + ":" + str(time[1]) + ":" + str(time[2])
    return (str(datelist[1])+" "+datelist[2]+" "+datelist[3] + " " + str(finaltime))

def getpaths(directory, writepath):
    tempdirectory = ""
    for filename in os.listdir(directory):
        tempdirectory = directory+"/"+filename
        try:
            for folders in os.listdir(tempdirectory):
                try:
                    message = os.path.join(tempdirectory, folders)
                    if os.path.isfile(message):
                        if os.path.basename(message).split('/')[-1] == "messages.json":
                            makechat(message, writepath)
                            print(os.path.basename(message).split('/')[-1])
                except:
                    pass
        except:
            pass
def start():
    print("Welcome to the Google Chat Parser")
    loc = input("What is the directory for the files?: ")
    writepath = input("Where should I put the files?: ")
    getpaths(loc,writepath)
start()
