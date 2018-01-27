# dictionary that maps a class name to a list of students who have taken the class.
class_to_students = dict()

# takes in a name of a Student and a list of classes he/she has taken and adds to the dictionary
def add_student(name, classes):
    for c in classes:
        class_to_students.setdefault(c, list()).append(name)

# Adding some data to dictionary
add_student("Kyle Qian", ["CSCI 0190", "CSCI 0180", "CSCI 0220", "ECON 1110", "ECON 1620", "NEUR 0010", "HIAA 0860",
                          "CLPS 0500", "MUSC 0610"])
add_student("Wenhuang Zeng", ["VISA 0140", "CLPS 0220", "APMA 1650", "CSCI 0150", "CSCI 0160", "CSCI 0220", "MATH 520",
                              "ECON 0110", "HIST 1101"])
add_student("Dylan Sam", ["CSCI 0170", "APMA 1650", "MATH 0520", "CHEM 0330", "PHYS 0100", "CHEM 0350", "CSCI 0180",
                          "CSCI 0220", "HIST 0276-B"])
add_student("Kevin Du", ["CSCI 0170", "MATH 0520", "CLPS 0220", "CSCI 0180", "CSCI 0220"])
add_student("Lawrence Huang", ["MATH 0520", "CSCI 0190", "CHEM 0330", "CSCI 0020", "CSCI 0220", "CHEM 0350",
                                            "MATH 0180"])
add_student("Ryan Choi", ["MATH 0520", "MATH 0180", "CSCI 0150", "MUSC 0610", "CSCI 0160", "CSCI 0220",
                                       "APMA 1650", "HIAA 0860"])

