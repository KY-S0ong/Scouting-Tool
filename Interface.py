import os, time
import pandas as pd
def clear():
   os.system('cls' if os.name == 'nt' else 'clear')

Scout = True

Question1 = False
TeamNameList = []

Question2 = False
TeamNumberList = []

Question3 = False
DriveTrainList = []

Question4 = False
VisionSystemList = []

Question5 = False
AutonList = []

if os.path.exists('ScoutSheet_BackUp.csv'):
    os.remove('ScoutSheet_BackUp.csv')
if os.path.exists('LocalScoutSheet.csv'):
        os.rename('LocalScoutSheet.csv','ScoutSheet_BackUp.csv')
        #os.remove('LocalScoutSheet.csv')

clear()
while Scout == True:

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
            
#* ----------------- Team Number ----------------------
    while Question2 == False:
        teamNumber = input("What is their Team Number: ")
        
        
        Q2 = input("Comfirm "+teamNumber+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q2 == "1":
            TeamNumberList.append(teamNumber)
            Question2 = True 
            clear()
            break
        else:
            Question2 = False
            clear()

#* ----------------- Drive Train ----------------------
    while Question3 == False:
        dT = input("What is their Drive Train\n\n1 - Swerve Drive\n2 - Mechanum Drive\n3 - Tank Drive\n4 - None of the above\n\n> ")
        
        if dT == '1':
            DriveTrain = "Swerve Drive"
        if dT == '2':
            DriveTrain = "Mechanum Drive"
        if dT == '3':
            DriveTrain = "Tank Drive"
        if dT == '4':
            clear()
            DriveTrain = input("What Drive Train are they using: ")
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
        if VisionSystem == "2":
            VisionType = 'Photon Vision'
        if VisionSystem == "3":
            VisionType = 'No Guidence'
        if VisionSystem == "4":
            VisionType = 'None'
        if VisionSystem == "5":
            clear()
            VisionType = input("What Vision System are they using: ")
    
        clear()
        Q4 = input("Comfirm "+ VisionType+"\n\n1 = Yes\n2 = No\n\n> ")
        if Q4 == "1":
            VisionSystemList.append(VisionType)
            Question3 = True 
            clear()
            break
        else:
            Question3 = False
            clear() 

    print("Team Name: ", TeamNameList)
    print("Team Number: ", TeamNumberList)
    print("DriveTrain: ", DriveTrainList)
    print("Vision Type: ", VisionSystemList)
    
    time.sleep(3)
    clear()
    Data = TeamNameList + TeamNumberList + DriveTrainList + VisionSystemList
    dict = {'Team Name': TeamNameList, 'Team Number': TeamNumberList, 'Drive Train': DriveTrainList, 'Vision Type': VisionSystemList}
    df = pd.DataFrame(dict)
    df.to_csv('LocalScoutSheet.csv')
    KeepScouting = int(input("1 - Keep Scouting\n2 - End\n\n> "))
    if KeepScouting == 1:
        Question1 = False
        Question2 = False
        Question3 = False
        Question4 = False
        clear()
   
    else:
        Scout = False
        break
clear()
print("Scout Session has ended\n\nAny Scouting data in previous Scout Session has been moved to 'ScoutSheet_BackUp.csv'")
    
  
        
    
    
    


