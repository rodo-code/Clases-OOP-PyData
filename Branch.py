class Branch:
    number_of_branches = 0
    """
    This class will be abstract a branch of some enterprise
    """

    def __init__(self, name, location, employees):
        Branch.number_of_branches += 1  # Update the number of branch's instances
        self.name = name  # The name of the branch
        self.location = location  # Specific geographical location of a branch in tex
        self.employees = employees  # Initially this attribute stores a list of Employee's names

    def __str__(self):
        return "Branch's name: {}\nLocation: {}".format(self.name, self.location)

    def number_of_employees(self):
        return len(self.employees)

    def names_of_employees(self):
        list_names = ""
        for employee in self.employees:
            list_names += (employee + "\n")
        return list_names

    def add_employee(self, employee_name):
        self.employees.append(employee_name)


branch1 = Branch("Montes", "Avenida Montes No 254 Casi Esquina Pando", ["Maria Apaza", "Jorge Ticona"])
branch2 = Branch("Prado", "Al frente de la fuente del Prado", ["Rodolfo Catunta", "Pedro Picapiedra", "Aracely Ramos"])
print(Branch.number_of_branches)  # Print 2 because there are 2 Branch's instances
print(branch1)
print("Branch 1 have {} employees".format(branch1.number_of_employees()))
print("The employees in branch 1 are:\n{}".format(branch1.names_of_employees()))
branch1.add_employee("Juan Pablo Rojas")
branch1.add_employee("Gabriela Fernandez")
print(branch2)
print("Branch 2 have {} employees".format(branch2.number_of_employees()))
print("The employees in branch 1 are:\n{}".format(branch2.names_of_employees()))
branch2.add_employee("Aldair Flores")