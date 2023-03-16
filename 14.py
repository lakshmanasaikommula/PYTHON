'''Now we discuss about the oops concepts which sre
INHERITANCE
POLYMORPHISM
ENCAPSULATION
ABSTRACTION'''

'''INHERITANCE:  which is one of the concept in python here a child can inherite the 
properties of a father , here existing classes are modified by anew class, by this we 
can re use the code , and no need to write it again , there are four types 

single inheritance : child inhirite the properties from parent
multilevel inheritance : child inhiritae the properties from parent as well as grand child
                            inhirite properties from child
hirarchical inheritance : child1 and child2 inheritate the parent properties
multiple inhiritance    : child having a properties of both mother and father
'''
#single inhiritance
class Parent:
    def fun1(self):
        print("this is a parent class")
class Child(Parent):
    def fun2(self):
        print("this is child class")
data = Child()
data.fun2()
data.fun1()
print("---------------------------------------------------")

#multilevel inhiritance
class Parent:
    def fun1(self):
        print("this is a parent class")
class Child(Parent):
    def fun2(self):
        print("this is child class")
class Grandchild(Child):
    def fun3(self):
        print("this is Grand child class")
data = Grandchild()
data.fun3()
data.fun2()
data.fun1()
print("---------------------------------------------------")

#hirarchical inheritance
class Parent:
    def fun1(self):
        print("this is a parent class")
class Child1(Parent):
    def fun2(self):
        print("this is child1 class")
class Child2(Parent):
    def fun3(self):
        print("this is child2 class")
data = Child2()
data.fun3()
#data.fun2()
data.fun1()
print("---------------------------------------------------")

#multiple inhiritance
class Father:
    def fun1(self):
        print("this is a father class")
class Mother(Parent):
    def fun2(self):
        print("this is mother class")
class Child(Father,Mother):
    def fun3(self):
        print("this is child class")
data = Child()
data.fun1()
data.fun2()
data.fun3()
print("---------------------------------------------------")


