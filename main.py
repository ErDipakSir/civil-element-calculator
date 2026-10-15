#After Day 7
#Mini Project 1 using Inheritence
def get_int_number(message):
    while True:
        try:
            number=int(input(message))
        except ValueError:
            print("Invilid Number")
            continue
        if number<=0:
            print("Enter Number greater than zero")
        else:
            return number
def get_number(message):
    while True:
        try:
            number=float(input(message))
        except ValueError:
            print("Invilid Number")
            continue
        if number<=0:
            print("Enter Number greater than zero")
        else:
            return number
def get_string(message):
    while True:
        text=input(message).strip()
        if text=="":
            print("Name cannot be Empty")
        elif text==",":
            print("Name Can not contain ,")
        else:
            return text
    
def menu():
    while True:
        print("\nSelect one of the following:")
        print("1. Add beam")
        print("2. Add column")
        print("3. Add slab")
        print("4. Show summary")
        print("5. Save and exit")
        choice = get_int_number("Choose option 1 to 5: ")

        if 1 <= choice <= 5:
            return choice
        print("Choose between 1 and 5")
class Element:
    def __init__(self, name, density=25):
        self.name = name
        self.density = density

    def volume(self):
        return 0                       # each child will replace this

    def weight(self):
        return self.volume() * self.density
class Slab(Element):
    def __init__(self, name, length, width, thickness):
        super().__init__(name)         # runs the parent's __init__
        #supe().__init__(name) call the element which return weight of corresponding to name and class
        #items = [Slab("S1", 6, 4, 0.15), Column("C1", 0.3, 3)] contain slab and Column but
        # for slab it goes S1 as name and volume are taken from volume(self) and goes to Elements
        self.length = length
        self.width = width
        self.thickness = thickness

    def volume(self):
        return self.length * self.width * self.thickness
class Beam(Element):
    def __init__(self, name, length, width, depth):
        super().__init__(name)         # runs super().__init__(name) does not return a weight.
        #It runs the parent’s setup, which stores name
        #  and density in the object. The weight is calculated later by weight()
        self.length = length
        self.width = width
        self.depth = depth

    def volume(self):
        return self.length * self.width * self.depth


class Column(Element):
    def __init__(self, name, length, width, height):
        super().__init__(name)
        self.length = length
        self.width = width
        self.height=height

    def volume(self):
        return self.length * self.width * self.height
def save_elements(elements):
    with open("elements.txt", "w") as f:
        for e in elements:
            if isinstance(e, Beam):
                f.write(f"Beam,{e.name},{e.length},{e.width},{e.depth}\n")
            elif isinstance(e, Column):
                f.write(f"Column,{e.name},{e.length},{e.width},{e.height}\n")
            elif isinstance(e, Slab):
                f.write(f"Slab,{e.name},{e.length},{e.width},{e.thickness}\n")


def load_elements():
    loaded = []
    try:
        with open("elements.txt", "r") as f:
            for line in f:
                kind, name, a, b, c = line.strip().split(",")
                a, b, c = float(a), float(b), float(c)
                if kind == "Beam":
                    loaded.append(Beam(name, a, b, c))
                elif kind == "Column":
                    loaded.append(Column(name, a, b, c))
                elif kind == "Slab":
                    loaded.append(Slab(name, a, b, c))
    except FileNotFoundError:
        pass                          # first run: no file yet, start empty
    return loaded
def show_summary(elements):
    print("\n===== Summary =====")
    if len(elements) == 0:
        print("No elements added yet.")
        return
    total_volume = 0
    total_weight = 0
    for e in elements:
        print(f"{e.name} ({type(e).__name__}): volume = {e.volume():.3f} m3, weight = {e.weight():.2f} kN")
        total_volume += e.volume()
        total_weight += e.weight()
    print(f"Total volume = {total_volume:.3f} m3")
    print(f"Total weight = {total_weight:.2f} kN")
elements = []

elements = load_elements()          # load saved data when the program starts

while True:
    choice = menu()
    if choice == 1:
        print("Enter the Beam details:")
        name = get_string("Beam name: ")
        length = get_number("Length (m): ")
        width = get_number("Width (m): ")
        depth = get_number("Depth (m): ")
        elements.append(Beam(name, length, width, depth))
    elif choice == 2:
        print("Enter the Column details:")
        name = get_string("Column name: ")
        length = get_number("Length (m): ")
        width = get_number("Width (m): ")
        height = get_number("Height (m): ")
        elements.append(Column(name, length, width, height))
    elif choice == 3:
        print("Enter the Slab details:")
        name = get_string("Slab name: ")
        length = get_number("Length (m): ")
        width = get_number("Width (m): ")
        thickness = get_number("Thickness (m): ")
        elements.append(Slab(name, length, width, thickness))
    elif choice == 4:
        show_summary(elements)
    elif choice == 5:
        save_elements(elements)
        print("Saved. Good bye!")
        break




