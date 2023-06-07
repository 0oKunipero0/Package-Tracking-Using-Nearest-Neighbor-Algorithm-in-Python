#  the class(object) delivery_Vehicle that is used to create the delivery truck objects
class delivery_Vehicle(object):
    def __init__(self, m, o, r, p, n, l):  # attributes of a delivery truck object
        self.l = l  # a time that shows when the truck leaves the hub for delivery
        self.m = m  # the max amount of packages a truck can fit
        self.n = n  # location of the truck
        self.o = o  # speed of the truck
        self.p = p  # how far the truck has traversed through
        self.q = l  # time of the truck at any given location. initialized to be the time when it leaves the hub
        self.r = r  # the packages that are on the truck at any given time