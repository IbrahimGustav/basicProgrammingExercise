# create
def getAboutMe(name, class_name):
    return("My name is " + name + " and i'm a part of " + class_name)


def getCourses(class_name):
    if(class_name == "TI23T"):
        return "Basic Programming"
    else:
        return "Object Oriented Programming"

about_ibrahim = getAboutMe("Ibrahim", "TI23T")
ibrahim_course = getCourses("TI23T")

print(about_ibrahim)
print(ibrahim_course)