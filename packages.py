import datetime

# the class(object) myPkg that is used to create the package objects
class myPkg (object):
    def __init__(self, a, b, c, d, e, f, g, h, i):  # attributes of a package object
        self.a = a  # id
        self.b = b  # address
        self.c = c  # city
        self.d = d  # state
        self.e = e  # postcode
        self.f = f  # delivery deadline
        self.g = g  # weight in Kg
        self.h = h  # special notes
        self.i = i  # status
        self.j = datetime.timedelta(hours=int(), minutes=int(), seconds=int())  # departure time
        self.k = datetime.timedelta(hours=int(), minutes=int(), seconds=int())  # delivery time

    def __str__(self):  # __str__ is used to modify the status text that will display in the UI interface. the self
                        # attribute points back at the attributes of the myPkg object declared.
        return "Package ID: %s" % (self.a) + "   ||Address: %s," % (self.b) + " %s," % (self.c) + " %s " % (
            self.d) + \
            "%s" % (self.e) + "   ||Deliver By: %s" % (self.f) + "    ||Weight: %s" % (self.g) + \
            "    ||Special Notes: %s" % (self.h) + \
            "\n                 ||Pkg %s" % (self.a) + " Status: %s" % (self.i) + ", %s" % (self.k)