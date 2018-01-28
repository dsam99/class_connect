import addStudent, operator

# Finds the most frequent classes taken in conjunction with input class name and returns a list of similar classes
def find_similar_classes(class_name):
    students = addStudent.class_to_students[class_name]
    similar_classes = dict()
    for student in students:
        for key, value in addStudent.class_to_students.items():
            if student in value and key not in similar_classes:
                similar_classes[key] = similar_classes.setdefault(key, 0) + 1
    sorted_freq = sorted(similar_classes.items(), key=operator.itemgetter(1))
    if len(sorted_freq) < 5:
        return [i[0] for i in sorted_freq]
    else:
        return [i[0] for i in sorted_freq[:5]]

