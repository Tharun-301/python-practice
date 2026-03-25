class Outer:
    def __init__(self):
        print("Outer class constructor")
        self.inner_obj = self.Inner()

    def show(self):
        print("Outer show method")
        self.inner_obj.show()

    class Inner:
        def __init__(self):
            print("Inner class constructor")
            self.data = "Hello from Inner class"

        def show(self):
            print(self.data)


# Creating Outer object
o = Outer()
o.show()

print("\nAccessing Inner class directly:")

# Creating Inner object directly
inner = Outer.Inner()
inner.show()