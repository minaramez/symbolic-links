#!/usr/bin/env python3
#above is the shebang!

#os is used to communicate with system related operations

import os

#command to clear the terminal 
os.system('clear')

#print functions to show the student name and date, along with information about the script.
print(" ")
print(" ")
print("Script written by: Mina Ramez Farag")
print("")
print("       **********************")
print("       ****Symbolic Links****")
print("       **********************")
print("")


#While loop that houses the entirety of the parent code
while True:
    #command to display options for the user
    print("Select an option:")
    print("1. Create symbolic link")
    print("2. Delete symbolic link")
    print("3. Generate summary report")
    print("Type 'quit' to exit")

    #input command to take a prompt from the user
    choice = input("Enter option (1-3), or 'quit' to exit: ")

    #quit the script if the user enters quit
    if choice== "quit":
        break
    
    #create the symbolic link 
    elif choice =="1":
        #prompting an input command for the user where they enter the file name they want linked
        filename =input("Enter filename or path: ")

        #command to check if the file exists in the /home/student/student/scripts/script03 directory
        if os.path.exists(filename ):
            print( "File found in directory '/home/student/student/scripts/script03/'")
            proceed= input("Do you wish to proceed? (Y/N): ")

            #command that proceeds with the symbolic link if the user enters y by giving the link a target path, and a link name and path. 
            if proceed.lower( ) =="y":
                target_path= os.path.abspath(filename )
                link_name = os.path.basename(filename)
                link_path = os.path.join(os.path.expanduser("~"), link_name)
                os.symlink (target_path, link_path)
                print("Symbolic link created" )
            
            #command to terminate the symbolic link creation incase the user enters N or any other input
            else:
                print( "Symbolic link terminated")

        #command that allows the user to know the file they input does not exist or is written incorrectly. 
        else:
            print("File not found" )

    #symbolic link deletion from /home directoy
    elif choice =="2" :

        #prompting an input command for the user where they enter the symbolic link file name they want deleted
        filename=input("Enter filename: ")

        #command that checks if the symbolic link exists in the /home directory
        symlink_path =os.path.join(os.path.expanduser("~"), filename)
        if os.path.islink(symlink_path ):
            print("File found in directory '/home'")
            proceed = input("Do you wish to proceed? (Y/N): ")

            #command that deletes the symbloc link when the user enters y
            if proceed.lower( ) =="y":
                os.remove(symlink_path )
                print("Symbolic link deleted")
            
            #command that terminates deletion of symbolic link if the user enters N or any other input
            else:
                print( "Deletion terminated")
        
        #command that allows the user to know the symbolic link they wish to delete either does not exist or is written incorrectly. 
        else:
            print( "Symbolic link not found")

    #command to generate report of symbolic links on the /home directory
    elif choice== "3":
        #command that extracts list of symbloc links from OS.
        links =[ os.path.basename(link) for link in os.listdir(os.path.expanduser("~")) if os.path.islink(os.path.join(os.path.expanduser("~"), link))]

        #command that summarizes the symbolic links in a table, with numbers in the first column, link name in second column, and target link in third column. 
        print("Summary report:")
        print("{:<10} {:<50}  {:<50}".format("Number" , "Symbolic link", "Target path") )
        for i, link in enumerate(links):
            target_path = os.readlink(os.path.join(os.path.expanduser("~") , link))
            print("{:<10} {:<50} {:<50}".format( i+1, link, target_path) )

    #command that lets the user know the input they gave is incorrect (anything other than 1, 2, 3, and quit).
    else:
        print("Invalid option")
