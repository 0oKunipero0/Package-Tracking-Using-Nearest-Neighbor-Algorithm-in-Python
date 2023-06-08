# Package-Tracking-Using-Nearest-Neighbor-Algorithm-in-Python


This project explores analysing and implementing high-performance data structures and supporting algorithms, including graphs, hashing, self-adjusting data structures, set representations, and dynamic programming. It also discusses how to use Python techniques to implement software solutions for problems of memory management and data compression. 


-------------------------------------------------------------------------------------------------

This project implements the Nearest Neighbor Algorithm to route delivery trucks that will allow the user to meet all delivery constraints while traveling 140 miles. The system will keep track of 3 trucks while meeting the following requirements:

•   Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•   There are no collisions.

•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 

•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).

•   There is up to one special note associated with a package.

•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.

•   The distances provided in the WGUPS Distance Table are equal regardless of the direction travelled.

•   The day ends when all 40 packages have been delivered.


------------------------------------------------------------------------------------------------

IMPLEMENTATION

Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the following components as input and inserts the components into the hash table:

•   package ID number

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (e.g., delivered, en route)

Develop a look-up function that takes the following components as input and returns the corresponding data elements:

•   package ID number

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time

Note: Your function should output all data elements for the package ID number. 

 an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)

1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.

2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.

3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
