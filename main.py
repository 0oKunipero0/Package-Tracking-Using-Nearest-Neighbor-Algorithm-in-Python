import csv
import datetime
from NNAlgorithm import nearest_neighb, pkg_hashTable
from truck import delivery_Vehicle
from packages import myPkg

Packages_for_truck_A = [1, 9,13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]  # initiate list of packages that will be on truck A
Packages_for_truck_B = [3, 18, 36, 38,  9,  24, 26, 27, 33, 35, 39, 32, 17,]  # initiate list of packages that will be on truck B
Packages_for_truck_C = [ 2, 4, 5, 7, 8, 10, 11, 12,  19, 21, 22, 23, 26,28,6, 25,]  # initiate list of packages that will be on truck C

# the below procedures are to retrieve the raw data from the external package file and parse them into the hash table
local_file = "Package_File.csv"
with open(local_file) as package_info:
    for x in csv.reader(package_info):  # reads package attributes from the corresponding column in the csv file
        i = "" # status column
        b = x[1]  # address column
        if x[7] != '':  # special notes column. uses if statement to find empty notes
            h = x[7]
        else:
            h = 'None'  # if empty note is find, declare it to be 'None' in UI
        c = x[2]  # city column
        a = int(x[0])  # id column
        d = x[3]  # state column
        f = x[5]  # deadline column
        e = x[4]  # zipcode column
        g = x[6] + ' Kg'  # weight column
        # instantiate a package object to the package variable
        package = myPkg(a, b, c, d, e, f, g, h, i)
        # insert the instantiated package object into the hash table: pkg_hashTable
        pkg_hashTable.insert_into_hash(a, package)

        if 'Wrong address listed' == package.h:  # package 9 address was wrong, corrected to be '410 S State St'
            package.b = '410 S State St'  # correct address
            package.h += ' -- Corrected'



# Declare attributes of the truck objects and instantiates 3 trucks from the trucks object: A_Truck is the first truck, B_Truck the second, and C_Truck last
max_Capacity = 16  # max truck load
avg_Speed = 18  # average speed of a truck indicated by the problem
initial_Mileage = 0.0  # declare the initial mileage of each truck to be 0
Hub_Address = "4001 South 700 East"  # this is the starting point of a given truck
Depart_time_for_truck_A = datetime.timedelta(hours=8, minutes=0)  # assign a time truck A will go out and deliver
Depart_time_for_truck_B = datetime.timedelta(hours=9, minutes=10)  # assign a time truck B will go out and deliver
Depart_time_for_truck_C = datetime.timedelta(hours=10, minutes=0)  # assign a time truck C will go out and deliver
A_Truck = delivery_Vehicle(max_Capacity, avg_Speed, Packages_for_truck_A, initial_Mileage, Hub_Address, Depart_time_for_truck_A)  # instantiate truck A object
B_Truck = delivery_Vehicle(max_Capacity, avg_Speed, Packages_for_truck_B, initial_Mileage, Hub_Address, Depart_time_for_truck_B)  # instantiate truck B object
C_Truck = delivery_Vehicle(max_Capacity, avg_Speed, Packages_for_truck_C, initial_Mileage, Hub_Address, Depart_time_for_truck_C)  # instantiate truck C object

# load the first two trucks with packages, the third truck won't depart until the one of the first two trucks finish its route
nearest_neighb(A_Truck)  # sort truck A using the Nearest Neighbor Algorithm
nearest_neighb(B_Truck)  # sort truck B using the Nearest Neighbor Algorithm
end_time = [A_Truck.q, B_Truck.q]  # assign the return time of truck A and B to end_time variable
C_Truck.l = min(end_time)  # compare the two trucks and find the minimum value and assign that to be the time of truck C
nearest_neighb(C_Truck)  # sort truck C using the Nearest Neighbor Algorithm



# main UI for the Tracking Service program
def ui_menu ():  # a method that is used to create the main UI interface of the Tracking Service program

    while True:
        try:
            user_input = input(  # the user can check the package status, truck info, or exit the program
                'What would you like to do? '
                '\n 1. Check package status '
                '\n 2. Check delivery truck info '
                '\n 3. Exit the program '
                '\n Enter here -->  ')
            if user_input == '3':  # if the user decides to exit the program, enter 3
                print('Thank you for using Tracking Service. See you next time! (program exited successfully)')
                exit()  # exit program
            if user_input == '2':  # if the user decides to check truck info, enter 2
                truck_mileage_check ()  # call the truck_mileage_check method
            if user_input =='1':  # if the user decides to check package status, enter 1
                status_check()  # call the status_check method
        except ValueError:
            print("Your entry wasn't valid. Please enter the proper option.")
            continue
        else:
            break

# a truck info program
def truck_mileage_check ():  # a method that is used for the truck info interface, subset of the main UI
    # the below menu will let the user choose which truck they want the see the status of
    truck_selection = input('Please select the truck below to check their mileage and location history:'
                            '\n 1. Truck A'
                            '\n 2. Truck B'
                            '\n 3. Truck C'
                            '\n 4. Back to previous menu'
                            '\n Enter here -->  ')
    while True:
        try:
            if truck_selection == '1':  # if the user chooses truck A, enter 1
                print ('|| Truck A || '
                       '\nMileage: ', A_Truck.p,  # displays the mileage of truck A
                       '\nPackage on Truck: ', A_Truck.r
                       )
                a = input('Enter 1 to return to main menu: ')
                if a == "1":
                    ui_menu()  # call the ui_menu to return to main menu after view truck status
            if truck_selection == '2':  # if the user chooses truck B, enter 2
                print('|| Truck B || '
                       '\nMileage: ', B_Truck.p,  # displays the mileage of truck B
                      '\nPackage on Truck: ', B_Truck.r
                       )
                a = input('Enter 1 to return to main menu: ')
                if a == "1":
                    ui_menu()  # call the ui_menu to return to main menu after view truck status
            if truck_selection == '3':  # if the user chooses truck C, enter 3
                print ('|| Truck C || ' 
                       '\nMileage: ', C_Truck.p,  # displays the mileage of truck C
                       '\nPackage on Truck: ', C_Truck.r
                       )
                a = input('Enter 1 to return to main menu: ')
                if a == "1":
                    ui_menu()  # call the ui_menu to return to main menu after view truck status
            if truck_selection == '4':  # if the user wants to go back, enter 4
                ui_menu()  # call the ui_menu method to go back
        except ValueError:
            print("Your entry wasn't valid. Please enter the proper option.")
            continue
        else:
            break

# a package status program
def status_check():  # a method that is used for the package status check interface, subset of the main UI
    # the user can check individual status or status of all packages
    individual_or_all = input('Would you like to check individual package, or all packages?'
                              '\n 1. Individual package'
                              '\n 2. All packages'
                              '\n 3. Return to main menu'
                              '\n Enter here -->  ')
    while True:
        try:
            if individual_or_all == '3':  # if the user decides to go back to the main menu, enter 3
                ui_menu()  # call ui_menu method to return
            if individual_or_all == '2':  # if the user decides to check status of all packages, enter 2
                # the user is then asked to enter a time
                time_entered = input('Please enter a time you wish to check the status for (hh:mm:ss): ')
                (uhr, min, sekunde) = time_entered.split(":")  # the time is formatted to be hour, minutes, seconds separated by ':'
                entered_Zeit = datetime.timedelta(hours=int(uhr), minutes=int(min), seconds=int(sekunde))  # store time to entered_Zeit
                for a in range(1, 41):  # for truck id within the range of 1 to 41
                    all_packages = pkg_hashTable.lookup_key(a)  # search all id numbers
                    if all_packages.k < entered_Zeit:  # compare package delivery time info with the time entered
                        all_packages.i = "--Package Delivered--"  # if delivery < time entered, packages status change
                                                                  # to "--Package Delivered--"

                        print(str(all_packages))
                    elif all_packages.j > entered_Zeit:  # compare package departure time info with the time entered
                        all_packages.i = "--En Route--"  # if departure time < time entered, packages status change
                                                         # to "--En Route--"
                        print(str(all_packages))
                    else:
                        all_packages.i = "--At The Hub--"  # if the above conditions don't apply packages are at the hub
                        print(str(all_packages))
                n_n = input('Enter 1 to return to main menu: ')
                if n_n == '1':
                    ui_menu()  # enter 1 to call the ui_menu method to go back

            if individual_or_all == '1':

                # the user will be asked to enter the id of the package they wish to inquire
                individual = input("Please enter the ID of the package -->  ")
                selected_package = pkg_hashTable.lookup_key(int(individual))
                # the user is then asked to enter a time
                time_entered = input('Please enter a time you wish to check the status for (hh:mm:ss): ')
                (uhr, min, sekunde) = time_entered.split(":")  # the time is formatted to be hour, minutes, seconds separated by ':'
                entered_Zeit = datetime.timedelta(hours=int(uhr), minutes=int(min), seconds=int(sekunde))  # store time to entered_Zeit
                if selected_package.k < entered_Zeit:  # compare package delivery time info with the time entered
                    selected_package.i = "--Package Delivered--" # if delivery < time entered, packages status change
                                                                  # to "--Package Delivered--"
                    print(str(selected_package))
                elif selected_package.j > entered_Zeit:  # compare package departure time info with the time entered
                    selected_package.i = "--En Route--"  # if departure time < time entered, packages status change
                                                         # to "--En Route--"
                    print(str(selected_package))
                else:
                    selected_package.i = "--At The Hub--"  # if the above conditions don't apply packages are at the hub
                    print(str(selected_package))

                n_n = input('Enter 1 to return to main menu: ')
                if n_n == '1':
                    ui_menu()  # enter 1 to call the ui_menu method to go back

        except ValueError:
            print("Your entry wasn't valid. Please enter the proper option.")
            continue
        else:
            break

# main class for the UI interface of the Tracking Service program
class main:

    # the following welcome message will display. it will also provide the summary of the trucks' mileages
    print('    =====================================' 
          '\n||  Welcome and thank you for using Tracking Service  || '
          '\n    =====================================\n'
          '\nThe mileage for the current route \nTotal Mileage: ',
          A_Truck.p + B_Truck.p + C_Truck.p,  # the total mileage will automatically display
          "\n")

    ui_menu()  # call main menu to start the UI of the Tracking Service program



