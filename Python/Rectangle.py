# Defining a class for rectangle
class Rectangle:
    # member variables
    length = 0
    breadth = 0

    # ------------------------------------------------------------------
    # method for input of data
    def input_data(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.breadth = float(input("Enter the breadth of the rectangle: "))

    # ------------------------------------------------------------------
    # method for displaying the data
    def display(self):
        print("------------Rectangle-------------")
        print("Length: ", self.length)
        print("Breadth: ", self.breadth)

    # ------------------------------------------------------------------
    # method for calculate the parameter
    def parameter(self):
        parameter = 2 * (self.length + self.breadth)
        print("Parameter: ", parameter)

    # ------------------------------------------------------------------
    # method for calculate the parameter
    def area(self):
        area = self.length * self.breadth
        print("Area: ", area)

rectangle = Rectangle()
rectangle.input_data()
rectangle.display()
rectangle.parameter()
rectangle.area()