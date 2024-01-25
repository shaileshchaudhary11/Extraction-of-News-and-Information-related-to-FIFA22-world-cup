#untill the user want to enter query allow him to fire query
#if user want to close the program enter "exit" in terminal 
# Way to give input for Enter Team Name : teamName_national_football_team
# example: Enter Team Name : England_national_football_team

import subprocess
logfile = open("logs.txt","a")

while True:
    print("Menu:")
    print("a. Enter 1 to see All the teams participated in the tournament")
    print("b. Enter 2 to see Venue details like name and capacity")
    print("c. Option 3 for Match Detais")
    print("d. Enter 4 to KockoutStages")
    print("e. Enter 5 to see ALL the awards")
    print("f. Enter 6 for executing question e:")
    print("g. Enter 7 to terminate program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        logfile.write("Choice 1 For team name"+'\n')
        subprocess.run(["python", "a_team.py"])
        print('\n')

    elif choice == 2:
        logfile.write("Choice 2 For Venue and capacity"+'\n')
        subprocess.run(["python", "b_venue.py"])
        print('\n')

    elif choice == 3:
        logfile.write("Choice 3 For Match details"+'\n')

        print("Enter the group name(a to h) whose data you want: ")
        x=input("Enter the group name whose data you want: ")

        if x == 'a':
             subprocess.run(["python", "00_A_group.py"])
             print('\n')
        elif x == 'b':
             subprocess.run(["python", "00_B_group.py"])
             print('\n')
        elif x == 'c':
             subprocess.run(["python", "00_C_group.py"])
             print('\n')
        elif x == 'd':
             subprocess.run(["python", "00_D_group.py"])
             print('\n')
        elif x == 'e':
             subprocess.run(["python", "00_E_group.py"])
             print('\n')
        elif x == 'f':
             subprocess.run(["python", "00_F_group.py"])
             print('\n')
        elif x == 'g':
             subprocess.run(["python", "00_G_group.py"])
             print('\n')
        elif x == 'h':
             subprocess.run(["python", "00_H_group.py"])
             print('\n')
        else:
            print("PLEASE ENTER VALID CHOICE!!")

    elif choice == 4:
        logfile.write("Choice 4 For KnockOut"+'\n')
        subprocess.run(["python", "round16.py"])
        print('\n')

    elif choice == 5:
        logfile.write("Choice 5 For Award"+'\n')
        subprocess.run(["python", "d_award.py"])
        print('\n')


    elif choice == 6:
        subprocess.run(["python", "01_e_enterTeam.py"])

        print("1. Enter 'a' to see ALL players of current squad")
        print("2. Enter 'b' to see its last  matches.")
        print("3. Enter 'c' to see its Upcoming five matches.")
        print("4. Enter 'd' to see any player name details from current squad:")

        ch=input("Enter your choice :")

        if ch == 'a':
            subprocess.run(["python", "e1_team.py"])

        elif ch == 'b':
            subprocess.run(["python", "e2_LastFiveMatch.py"])

        elif ch == 'c':
            subprocess.run(["python", "e2_UpcomingMatch.py"])

        elif ch == 'd':
            subprocess.run(["python", "playerName.py"])
            print("Particualr Player File get created, But its Grammar Pending bcz of less time")
        else:
            print("Invalid choice please enter value from a to d")

    elif choice == 7:
        print("THANK YOU!!")
        print("Exiting program...")
        exit()

    else:
        print("Invalid choice, please enter a number between 1 and 6")
