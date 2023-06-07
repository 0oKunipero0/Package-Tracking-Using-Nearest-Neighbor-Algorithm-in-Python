import csv
import datetime
from Hash import hash_table_initiate

# instantiate a hash table to hold the package objects. maxed at 16 objects per table
pkg_hashTable = hash_table_initiate()
def nearest_neighb(delivery_vehicle):

    temp = []   # a temp list is created to host all packages waiting to be sorted. these packages will be removed as them being added to the package list of a delivery vehicle.
    mileage_tracking_list = []  # a list of collection of distances of a given truck. it will be used to sum the total mileage later on
    vehicle_location_tracking = []  # a list that hold the data of the location as a given truck traverses through. the last item in this list will be the newest location of that truck.
    for package_id in delivery_vehicle.r:
        temp.append(pkg_hashTable.lookup_key(package_id))  # the packages that were preloaded into a given truck will all be appanded to the temporary list .

    # using while loop to sort packages in the temp list and remove them from the temp list.
    # once they are being added to the package list of a given vehicle
    while len(temp) >= 0:
        upcoming_pkg = None  # set the next package the truck to which it will go to to be none. this value will get updated after the first iteration

        # creating a way for the algorithm to stop sorting if the temp list is empty to prevent error
        if len(temp) == 0:
            break
        else:
        # to compare all the address of the existing packages in the pkg_awaits_delivery list with the current address to find the next nearest package
            temp_list = []  # temporary list to hold distance data for comparison
            for package in temp:
                local_file = "Address_File.csv"
                with open(
                        local_file) as address_data:  # open the address file to find the index of the address that corresponds with the row and column value of the distance file
                    for x in list(csv.reader(address_data)):
                        if delivery_vehicle.n in x[2]:  # if the location of the truck is in the column
                            a = int(x[0])  # store the address id of location of the truck as variable a
                        if package.b in x[2]:  # if the location of the package is in the column
                            b = int(x[0])  # store the address id of the location of the package as variable b

                local_file1 = "Distance_Table.csv"
                with open(
                        local_file1) as len_edge:  # open the distance file to compare truck vs package indexes relative to the rows and columns in the distance table
                    _edge_len_data = list(csv.reader(len_edge))  # stores the distance data to the variable _edge_len_data
                    vertex_vertex = _edge_len_data[a][b]  # initialize the first distance with variable a as the row and variable b as column. use that data to find the corresponding distance aka vertex_vertex value
                    if vertex_vertex == '':  # if the vertex_vertex value that (a,b) provides gives an empty space
                        vertex_vertex = _edge_len_data[b][a]  # flip the row and column value to be (b,a) to find the vertex_vertex value value
                    temp_list.append(vertex_vertex)  # append the package to the temp_list for comparison
                    shortest_d = min(temp_list)  # find the smallest number of all the distance values and that number will be the nearest neighbor
                    for y in vertex_vertex:  # for any value in the vertex_vertex list, represented by y variable
                        if y == shortest_d:  # if that value, represented by y, equals to the shortest distance value obtained previously
                            for b in x[0]:  # for b (package address) in the address table
                                delivery_vehicle.n = x[2]  # the address index of y retrieves the address string and assigned to the delivery vehicle location
                    _v = float(shortest_d)  # convert the shortest distance into float
                    upcoming_pkg = package  # the package the _v represents will be the next package the truck will go to
            if len(temp) != 0:  # creating an if statement to prevent popping even when the list has been emptied to avoid error
                temp.pop(temp.index(upcoming_pkg))  # this pops the index id of the next package from the temp list to indicate it's nolonger there
            else:
                break
            mileage_tracking_list.append(_v)  #  append the value of distance between the last package and the next one to the mileage list
            vehicle_location_tracking.append(upcoming_pkg.b) #  tracks the location the truck has been through
            delivery_vehicle.q += datetime.timedelta(hours=_v / 18)  # newest time of the truck to the closest address/pkg
            upcoming_pkg.k = delivery_vehicle.q # set the delivery time of the package
            upcoming_pkg.j = delivery_vehicle.l # departure time of the delivery trucks
        delivery_vehicle.n = vehicle_location_tracking[-1]  # use the last item in the truck location list for the
                                                            # value of the truck's latest location
    delivery_vehicle.p = sum(mileage_tracking_list)  # sum the cumulative mileage of a truck to get the total distance of a given truck