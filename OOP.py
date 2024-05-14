import dis


class demo1:
    def display(self):
        print("Hello World")


d = demo1()
d.display()


class student:
    def display(self):
        print("Hello Student")


s1 = student()
s1.display()


class car:
    def get(self, color, style):
        self.color = color
        self.style = style

    def put(self):
        print("Color: ", self.color)
        print("Style: ", self.style)


c = car()
c.get("Red", "Sedan")
c.put()


class sample:
    a = 10

    def display(self, y):
        print("Value of a: ", self.a)
        print("Value of y: ", y)


s = sample()
s.display(20)


class counter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


c = counter()
c.count()
c.count()


class stu:
    __a = 10
    b = 20

    def __private_method(self):
        print("Private Method")

    def public_method(self):
        print("Public Method")
        print("A:", self.__a)
        self.__private_method()


s = stu()
s.public_method()
print(s.b)


class parent:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


d = parent("John", 23, "male")
print(d.name)
print(d.age)
print(d.gender)


class rectangle:
    length = 0
    breadth = 0

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("Length: ", self.length)
        print("Breadth: ", self.breadth)
        print("Area: ", self.area())
        print("Perimeter: ", self.perimeter())


r = rectangle(10, 20)
r.display()


class circle:
    radius = 0

    def __init__(self, r):
        self.radius = r

    def getarea(self):
        print(3.14 * self.radius * self.radius)
        return

    def getcircumference(self):
        print(2 * 3.14 * self.radius)
        return


c = circle(10)
c.getarea()
c.getcircumference()


def area(side):
    calc = side * side
    print("Area: ", calc)


area(100)


class demo:
    def print_r(self, a, b):
        print("A: ", a)
        print("B: ", b)


obj = demo()
obj.print_r(10, "S")
obj.print_r("S", 10)


class demo2:
    def arguments(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("A: ", a)
            print("B: ", b)
            print("C: ", c)
        elif a != None and b != None:
            print("A: ", a)
        else:
            print("No Arguments")


class operation:
    def add(self, a, b):
        return a + b


op = operation()
print(op.add(10, 20))


class vehicle:
    name = "Maruti"

    def display(self):
        print("Vehicle Name: ", self.name)


class category(vehicle):
    price = 400000

    def display_price(self):
        print("Category: ", self.price)


car1 = category()
car1.display()
car1.display_price()


class two_wheeler:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Name: ", self.name)
        print("Price: ", self.price)


# The class `scooter` inherits from `two_wheeler` and includes a method to display the color of the scooter.


class scooter(two_wheeler):
    def __init__(self, name, price, color):
        self.color = color
        two_wheeler.__init__(self, name, price)

    def display_color(self):
        print("Color: ", self.color)


s = scooter("Activa", 70000, "Red")
s.display()
s.display_color()


class m1:
    def display1(self):
        print("Class M1")


class m2(m1):
    def display2(self):
        print("Class M2")


class m3(m2):
    def display3(self):
        print("Class M3")


m = m3()
m.display1()
m.display2()
m.display3()


class grand_father:
    grandfathername = ""

    def display1(self):
        print(self.grandfathername)


class father(grand_father):
    fathername = ""

    def display2(self):
        print(self.fathername)


class son(father):
    def parents(self):
        print("Grand Father: ", self.grandfathername)
        print("Father: ", self.fathername)


s = son()

s.grandfathername = "Bhimrao"
s.fathername = "Ravindra"
s.parents()


class Dad:
    def display_dad(self):
        print("Dad")


class Mom:
    def display_mom(self):
        print("Mom")


class Child(Dad, Mom):
    def display_child(self):
        print("Child")


c = Child()
c.display_dad()
c.display_mom()
c.display_child()


class RCB:
    def display_team(self):
        print("Royal Challengers Bangalore")


class Virat(RCB):
    def display_self(self):
        print("Virat Kohli")


class ABD(RCB):
    def display_self(self):
        print("AB de Villiers")


king = Virat()
king.display_team()
king.display_self()

abd = ABD()
abd.display_team()
abd.display_self()


class A:
    def display(self):
        print("Class A")


class B(A):
    def display(self):
        print("Class B")


z = B()
z.display()


class C:
    def display(self):
        print("Class C")


class D(C):
    def display(self):
        super().display()
        print("Class D")


x = D()
x.display()


class gmail:
    def send_email(self, msg):
        print("Sending '{}' from Gmail".format(msg))


class yahoo:
    def send_email(self, msg):
        print("Sending '{}' from Yahoo".format(msg))


class email:
    provider = gmail()

    def set_provider(self, provider):
        self.provider = provider

    def send_email(self, msg):
        self.provider.send_email(msg)


client1 = email()
client1.send_email("Hello World")
client1.set_provider(yahoo())
client1.send_email("Hello World")
