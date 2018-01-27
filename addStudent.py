# dictionary that maps a class name to a list of students who have taken the class.
class_to_students = dict()


# turns a string of classes into a list of classes
def classes_str_to_list(classes):
    classes_list = classes.split(",")
    for c in classes_list:
        c.replace(" ", "")
    return classes_list

# takes in a name of a Student and a string of classes he/she has taken and adds to the dictionary
def add_student(name, classes):
    for c in classes_str_to_list(classes):
        class_to_students.setdefault(c, list()).append(name)

# Adding some data to dictionary
add_student("Kyle Qian", "CSCI0190, CSCI0180, CSCI0220, ECON1110, ECON1620, NEUR0010, HIAA0860, CLPS0500, MUSC0610")
add_student("Wenhuang Zeng", "VISA0140, CLPS0220, APMA1650, CSCI0150, CSCI0160, CSCI0220, MATH0520, ECON0110, HIST1101")
add_student("Dylan Sam", "CSCI0170, APMA1650, MATH0520, CHEM0330, PHYS0100, CHEM0350, CSCI0180, CSCI0220, HIST0276-B")
add_student("Kevin Du", "CSCI0170, MATH0520, CLPS0220, CSCI0180, CSCI0220")
add_student("Lawrence Huang", "MATH0520, CSCI0190, CHEM0330, CSCI0020, CSCI0220, CHEM0350, MATH0180")
add_student("Ryan Choi", "MATH0520, MATH0180, CSCI0150, MUSC0610, CSCI0160, CSCI0220, APMA1650, HIAA0860")



