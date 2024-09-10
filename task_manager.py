#=====importing libraries===========
'''This is the section where you will import libraries'''

from datetime import date 

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# Creating a dictionary that will store usernames and passwords
# as key value pairs
users = {}

# Opening user_file for reading user information
with open ('user.txt', 'r') as file:
     
     for lines in file:
          # Seperate each line in file into a list with a key-value pair
          (keys, values) = lines.split()
          # Remove commas keys and replace with blank space
          keys = keys.replace("," , "")
          # Update dictionary with the keys and values
          users[keys] = values

while True:

    # Ask user for username and password 
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    # If username is in keys and password matches value of username
    # print welcome 
    if username in users.keys() and password == users[username]:
        print(f"Welcome {username}!\n")

    # If username is not in dictionary keys or password does not 
    # match value pair of username, user must try again
    elif username not in users or password != users.get(username):
        print("Username or password is invalid. Please try again.")

        continue

    break    


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    
    
#======================================================================================================================

    if menu == 'r':
       
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''

        # Checking if user is admin so they can gain permission to register user and see stats
        if username == 'admin':
                    
                    # Creating a menu to choose from if the user is admin
                    menu_2 = input("""\nPlease select one of the following options:
r- register a user  
d- display stats 
: """).lower()
                    # Registering a user
                    if menu_2 == 'r':

                        with open ('user.txt', 'a') as user_file:
                            
                            new_username = input("\nPlease input a new username: ")
                            new_password = input("Please input a new password: ")
                            confirm_password = input("Please confirm password: ")

                            while new_password != confirm_password:
                                print("Your passwords do not match.")
                                new_password = input("Please input your password again: ")
                                confirm_password = input("Please confirm your password again: ")
                        
                            else:
                                user_file.write("\n" + new_username + "," + " " + new_password) 
                                print("Your password has been successfully saved!\n")

                    # Displaying statistics of user file and tasks file
                    elif menu_2 == 'd':
                        
                        # Declaring variables
                        count = 0
                        count_2 = 0

                        # Opening tasks file and counting lines in the file 
                        with open ('tasks.txt', 'r') as tasks_file:

                                                    
                            
                            for each_line in tasks_file:                   
                                count += 1

                            print (f"The total number of tasks in the tasks file is {count}.")

                            # Opening user file and counting lines in the file 
                            with open ('user.txt', 'r') as user_file:

                                for each_line in user_file:                                                                              
                                    count_2 += 1

                                print(f"The total number of users in the user file is {count_2}.")

                    else:
                        print("You have entered an invalid menu option. Please try again.")


        # Printing error message if user did not input a valid menu option
        else:
            print("Sorry, you cannot register a user.\n")
            

#===========================================================================================================================

    elif menu == 'a':
        
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        
        # Opening tasks file for appending to and taking task information
        # from user as input
        with open('tasks.txt', 'a') as tasks_file:
            task_username = input("Please enter the username of the person whom the task is assigned to: ")
            task_title = input("Please enter the title of the task: ")
            task_description = input("Please enter the description of the task: ")
            task_due_date = input("Please enter the due date of the task (eg. 07 May 2007): ")
            task_complete = "No"

            # Formatting current date to be in string format
            date = date.today()
            string_date = date.strftime("%d %b %Y") 

            # Appending new task to tasks file
            tasks_file.write("\n" + task_username + ", " + task_title + ", " + task_description + ", " + string_date + ", " + task_due_date + ", " + task_complete)

            print("Your task has been successfully added!\n")


#===========================================================================================================================

    elif menu == 'va':

        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        # Opening tasks file for reading 
        with open ('tasks.txt', 'r') as tasks_file:
        

            print("-" * 130)
            
            # Looping through each line, stripping each line of white spaces at end 
            # and beginning, splitting each line at the comma and creating each 
            # line into a set. Then printing each element of every set in a neat
            # format within the same for loop. 
         
            for line in tasks_file:
               
               line = line.strip()
               line = line.split(", ")
            
               # If number of items in list are 6, then output the code below
               # Ensures that if list is empty, code does not come up with error
               if len(line) == 6:
                      
                    print("{:<20} {:<10}".format("Task", line[1]))
                    print("{:<20} {:<10}".format("Assigned to:", line[0]))
                    print("{:<20} {:<10}".format("Date assigned:", line[3]))
                    print("{:<20} {:<10}".format("Due date:", line[4]))
                    print("{:<20} {:<10}".format("Task complete?", line[5]))
                    print("{:<20} {:<10}".format("Task description:", line[2]))
                    print("-" * 130)

                        
#=================================================================================================================================
    
    elif menu == 'vm':

        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        # Opening tasks file for reading
        with open('tasks.txt', 'r') as tasks_file:

            print("-" * 130)

            # Looping through every line in tasks file stripping
            # every line of beginning and ending white spaces and splitting 
            # each line at comma into elements of a list
            for line in tasks_file: 
                
                line = line.strip()
                line = line.split(", ")

                # If number of items in list are 6, then output the code below
                # Ensures that if list is empty, code does not come up with error
                if len(line) == 6:  

                # Checking if the first element of the list equals the
                # username entered at the beginning of the programme for every line 
                # in the tasks file. If so, formatting and printing the task 
                # that belongs to the username
                    if line[0] == username:
                        
                        print("{:<20} {:<10}".format("Task", line[1]))
                        print("{:<20} {:<10}".format("Assigned to:", line[0]))
                        print("{:<20} {:<10}".format("Date assigned:", line[3]))
                        print("{:<20} {:<10}".format("Due date:", line[4]))
                        print("{:<20} {:<10}".format("Task complete?", line[5]))
                        print("{:<20} {:<10}".format("Task description:", line[2]))
                        print("-" * 130 )


#====================================================================================================================================


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")

       