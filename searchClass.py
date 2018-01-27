import addStudent

# takes in a name of a class and looks it up in the dictionary
def search_class(class_name):
    if class_name in addStudent.class_to_students:
        return addStudent.class_to_students[class_name]
    else:
        print("No data for that class.")

