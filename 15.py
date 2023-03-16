'''POLYMORPHISM
which is as a one function with many forms
which means its ability to take different forms
Polymorphism in python in child class with the same name is defined in parent class
these are four types
Compile-time: it is a polymorphism which is resolved during the compilation procees

method overriding: which is specific task done by parent class is also done by the child class
it used to chaging existing behaviour there atleast two classes needed for method overriding
,method overriding always uses inheritance b/w superclass and parentclass it is a runtime polymorphism

method overloading: which is a compile time polymorphism there is a single class
 which performs the different operations python doesnt support method overloading

 runtime polymorphism: method overriding also called as runtime polymorphism which is
 supports in java,c,c++,python, this feature also uses inheritance'''


#METHOD-OVERLOADING
class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c
data = A()
print(data.sum(1,2,5))

#METHOD-OVERRIDING
class A:
    def display(self):
        print("This is a class A")
class B(A):
    def display(self):
        print("This is a class B")
        super().display()
data = B()
data.display()

