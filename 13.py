#now its time to talk about OOPS CONCEPT
'''oops is stands for objective oriented programming system
oops will supports in objective oriented programming like java c++
also its supports in procedure oriented programming like c
also supports in functional programming in python also
but python functions and objects are different major it industries for big projects they
work using oops cocepts
and there we have to solve the real world issues with virtual world technologies
in it objects are very usefull suppose an it employee working for a project he needs an object
which is laptop , so objects are very important in oops we are creating objects and classses
to do on a projrcts with real world scenaries and objects having attributes and behaviour
attributes means variable suppose i am lakshman laksman is a variable i am talking which is
my behaviour aspect which are storing properties and values and also objects needs methods
here functions are called as methods in oops
and objects are created by class which is a desighn and bluprint of an object
suppose motorola is phone nothing but an an object which is desighn by china which is a class
'''

class Product:
    def __init__(self,name,color,camera,storage):
        self.name = name,
        self.camera = camera,
        self.color = color,
        self.storage = storage,
        print("lenovo i3 and 11 th gen ")
    def mobile(self):
        print("name: ",self.name)
        print("color: ",self.color)
        print("storage: ",self.storage)
        print("camera: ",self.camera)
        print("----------------------------------------------")

data = Product("oneplus","black","64px","256gb")
data.mobile()
print(type(data))
print("--------------------------------------------------------------")
data1 = Product("apple","red","13mp","512gb")
data1.mobile()
print(type(data1))