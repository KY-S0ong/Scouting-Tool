import os, time
import pandas as pd
def clear():
   os.system('cls' if os.name == 'nt' else 'clear')
Scout = True
Run = True

def pspace(str):
    print(str)
    print()


#?------------ Instructions -------------------
# Hi! If you are reading this, you are either part of FRC 3958 Schordingers Cat,
# or another team who had downloaded this off our Git Hub. 
# Please do not remove the instructions as I worked hard on this 

# Quick rundown
# There are 3 files that should concern you
    # Interface.py
    # LocalScoutSheet.csv - Send this to your online spreadsheet of choice
    # ScoutSheet_BackUp.csv - Sends the overided spreadsheet to here
# Runs in any python IDE. You may have to install Pandas in your IDE of choice. 

# Questions can be added/modified with a simply understanding of python, but heres a sumerized version
    # [] is to indcate a list. This is to make a new subject to put into the spreadsheet
    # Put the List name into Data & dict or "Add New Subjects" 
    # Follow the format of the rest and you should be fine

# Enjoy!

#*------------ Questions Lists Add Here -------------------
Question1 = False
TeamNameList = []

Question2 = False
TeamNumberList = []

Question2andHalf = False
RobotNameList = []

Question3 = False
DriveTrainList = []

Question4 = False
VisionSystemList = []

Question5 = False
AutonList = []

Question6 = False
AutonPosistionList = []

Question7 = False
CoralLevelsList = []

Question8 = False
ProcessorList = []

Question9 = False
ClimbTimingList = []

Question10 = False
CycleTimeList = []

#!------------ Scout Tool Run -------------------
while Run == True:
    clear()
    RunType = int(input("Scout Tool\n\n1 - Delete Scout Sheet\n2 - Delete Back Up Scout \n3 - Delete all\n4 - Scout\n5 - Continue Scout\n\n> "))
    clear()
    if RunType == 1:
        if os.path.exists('LocalScoutSheet.csv'):
            os.remove('LocalScoutSheet.csv')
            print("LocalScoutSheet.csv deleted succesfully!")
            time.sleep(1)
            clear()
        else:
            print("Error | Nothing to delete")
            time.sleep(1)
            clear()
    if RunType == 2:
        if os.path.exists('ScoutSheet_BackUp.csv'):
            os.remove('ScoutSheet_BackUp.csv')
            print("ScoutSheet_BackUp.csv deleted succesfully!")
            time.sleep(1)
            clear()
        else:
            print("Error | Nothing to delete")
            time.sleep(1)
            clear()
    if RunType == 3:
        if os.path.exists('ScoutSheet_BackUp.csv'):
            os.remove('ScoutSheet_BackUp.csv')
            print("ScoutSheet_BackUp.csv deleted succesfully!")
            time.sleep(1)
            clear()
        else:
            print("Error | Nothing to delete")
            time.sleep(1)
            clear()
        if os.path.exists('LocalScoutSheet.csv'):
            os.remove('LocalScoutSheet.csv')
            print("LocalScoutSheet.csv deleted succesfully!")
            time.sleep(1)
            clear()
        else:
            print("Error | Nothing to delete")
            time.sleep(1)
            clear()
    if RunType == 4:
        print("Intiating Scout Mode")
        time.sleep(1)
        clear()
        Run = False
        break
    # Under Testing if RunType == 5:
        if os.path.exists('LocalScoutSheet.csv'):
            print("Continuing Scout Seassion")
            dict = pd. read_csv('LocalScoutSheet.csv')
       
            Name = dict[['Team Name']]
            Num = dict[['Team Number']]
            Drive = dict[['Drive Train']]
            Vision = dict[['Vision Type']]
            Auto = dict[['Auton Type']]
            
            
            TeamNameList.append(Name)
            TeamNumberList.append(Num)
            DriveTrainList.append(Drive)
            VisionSystemList.append(Vision)
            AutonList.append(Auto)
            time.sleep(1)
            clear()
            
            pspace(TeamNameList)
            pspace(TeamNumberList)
            pspace(DriveTrainList)
            pspace(VisionSystemList)
            pspace(AutonList)
            
            time.sleep(3)
            clear()
            Run = False
            break
        else:
            print("Error | Nothing to continue")
            time.sleep(1)
            clear()
        
        




if os.path.exists('ScoutSheet_BackUp.csv'):
    os.remove('ScoutSheet_BackUp.csv')
if os.path.exists('LocalScoutSheet.csv'):
        os.rename('LocalScoutSheet.csv','ScoutSheet_BackUp.csv')
        #os.remove('LocalScoutSheet.csv')

clear()
while Scout == True:

#* ----------------- Team Number ----------------------
    while Question2 == False:
        teamNumber = input("What is their Team Number: ")
        clear()
        Q2 = input("Comfirm "+teamNumber+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q2 == "1":
            TeamNumberList.append(teamNumber)
            Question2 = True 
            clear()
            break
        else:
            Question2 = False
            clear()
            
#* ----------------- Team Name -------------------------
    while Question1 == False:
        teamName = input("What is their Team Name: ")
        
        
        Q1 = input("Comfirm "+teamName+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q1 == "1":
            TeamNameList.append(teamName)
            Question1 = True 
            clear()
            break
        else:
            Question1 = False
            clear()
            
#* ----------------- Robot Name ----------------------
    while Question2andHalf == False:
        robotname = input("What is their Robot Name: ")
        
        clear()
        Q = input("Comfirm "+robotname+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q == "1":
            RobotNameList.append(robotname)
            Question2andHalf = True 
            clear()
            break
        else:
            Question2andHalf = False
            clear()
#* ----------------- Drive Train ----------------------
    while Question3 == False:
        dT = input("What is their Drive Train\n\n1 - Swerve Drive\n2 - Mechanum Drive\n3 - Tank Drive\n4 - None of the above\n\n> ")
        
        if dT == '1':
            clear()
            q = input("What type of motors, swerve module, and gear ratios?\n\nExample format: Krakens, SDS MK4, 6.75:1\n\n> ")
            DriveTrain = "Swerve Drive, " + q
        elif dT == '2':
            DriveTrain = "Mechanum Drive"
        elif dT == '3':
            DriveTrain = "Tank Drive"
        elif dT == '4':
            clear()
            DriveTrain = input("What Drive Train are they using: ")

        else:
            DriveTrain = "Did Not Enter"
        clear()
        Q3 = input("Comfirm "+ DriveTrain+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q3 == "1":
            DriveTrainList.append(DriveTrain)
            Question3 = True 
            clear()
            break
        else:
            Question3 = False
            clear()
#* ----------------- Vision System ------------------------
    while Question4 == False:
        VisionSystem = input("What Vision System are they using\n\n1 - Lime Light\n2 - Photon Vision\n3 - No Guidance\n4 - None\n5 - Custom\n\n> ")
        
        if VisionSystem == "1":
            VisionType = 'Lime Light'
        elif VisionSystem == "2":
            VisionType = 'Photon Vision'
        elif VisionSystem == "3":
            VisionType = 'No Guidence'
        elif VisionSystem == "4":
            VisionType = 'None'
        elif VisionSystem == "5":
            clear()
            VisionType = input("What Vision System are they using: ")

        else:
            VisionType == "Did Not Enter"
    
        clear()
        Q4 = input("Comfirm "+ VisionType+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q4 == "1":
            VisionSystemList.append(VisionType)
            Question3 = True 
            clear()
            break
        else:
            Question4 = False
            clear() 
#* ----------------- Auton Capabilities ------------------------
    while Question5 == False:
        AutonType = input("What can your Auton Do\n\n1 - Nothing\n2 - Can Taxi\n3 - Score Coral (Custom Ammount)\n4 - Other\n\n> ")
        clear()
        if AutonType == "1":
            Auton = "Nothing"
        elif AutonType == "2":
            Auton = "Taxi"
        elif AutonType == "3":
            x = input("How much Coral can they Score: ")
            Auton = "Score Coral: " + x
        elif AutonType == "4":
            Auton = input("What can they do: ")

        else:
            Auton = "Did not Enter"
        Q5 = input("Comfirm "+ Auton+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q5 == "1":
            AutonList.append(Auton)
            Question5 = True 
            clear()
            break
        else:
            Question5 = False
            clear() 
#* ----------------- Auton Positions ------------------------    
    while Question6 == False:
        Position = input("Which sides can their robot preform their auton. \n\nLeft, Center, Right\n\n> ")
        clear()
        
        Q6 = input("Comfirm "+ Position+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q6 == "1":
            AutonPosistionList.append(Position)
            clear()
            Question6 = True
        else:
            Question6 = False
            clear() 
        
    while Question7 == False:
        q = input("What Coral Levels you prefer to score\n\n> ")
        clear()
        Q7 = input("Comfirm "+ q+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q7 == "1":
            CoralLevelsList.append(q)
            clear()
            Question7 = True
        else:
            Question7 = False
            clear()
    while Question8 == False:
        x = input("Where/can you score Algae\n\n1 - Proccesor\n2 - Barge\n3 - None\n\n> ")
        if x == "1":
            c = "Processor"
        elif x == "2":
            c = "Barge"
        elif x == "3":
            c = "None"
        clear()
        Q8 = input("Comfirm "+ c+"\n\n1 = Yes\n2 = No\n\n> ")
        
        if Q8 == "1":
            ProcessorList.append(c)
            clear()
            Question8 = True
        else:
            Question8 = False
            clear()
    while Question9 == False:
        x = input("When do you start climbing: ")
        clear()
        Q9 = input("Comfirm "+ x+"\n\n1 = Yes\n2 = No\n\n> ")
        
        if Q9 == "1":
            ClimbTimingList.append(x)
            clear()
            Question9 = True
        else:
            Question9 = False
            clear()
        
    time.sleep(1.5)
    clear()
   #* ----------------- Add New Subjects ------------------------
    Data = TeamNameList + TeamNumberList + RobotNameList + DriveTrainList + VisionSystemList + AutonList + CoralLevelsList + ProcessorList + ClimbTimingList
    dict = {'Team Name': TeamNameList, 
            'Team Number': TeamNumberList, 
            'Robot Name': RobotNameList,
            'Drive Train': DriveTrainList,
            'Vision Type': VisionSystemList,
            'Auton Type': AutonList,
            'Coral Levels': CoralLevelsList,
            'Processsor/Algae': ProcessorList,
            "Climb Timing": ClimbTimingList}
   
    df = pd.DataFrame(dict)
    df.to_csv('LocalScoutSheet.csv')
    if os.path.exists('LocalScoutSheet.csv'):
        print("Team saved succesfully")
        time.sleep(0.8)
        clear()
    
    print("Team Name: ", TeamNameList)
    print("Team Number: ", TeamNumberList)
    print("Robot Name: ", RobotNameList)
    print("DriveTrain: ", DriveTrainList)
    print("Vision Type: ", VisionSystemList)
    print("Auton Type: ", AutonList)
    print("Coral Levels: ", CoralLevelsList)
    print("Processor/Algae: ", ProcessorList)
    print("StartClimbing: ", ClimbTimingList)

    print("")
    #* ----------------- Keep Scouting ------------------------
    KeepScouting = int(input("1 - Keep Scouting\n2 - End\n\n> "))
    if KeepScouting == 1:
        Question1 = False
        Question2 = False
        Question2andHalf = False
        Question3 = False
        Question4 = False
        Question5 = False
        Question6 = False
        Question6 = False
        Question7 = False
        Question8 = False
        Question9 = False
        
        clear()
   
    else:
        Scout = False
        break
clear()
print("Scout Session has ended\n\nAny Scouting data in previous Scout Session has been moved to 'ScoutSheet_BackUp.csv'")