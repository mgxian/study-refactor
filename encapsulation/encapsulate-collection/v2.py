import copy


class Person:
    def __init__(self, name):
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return copy.deepcopy(self._courses)

    @property.setter
    def courses(self, aList):
        self._courses = aList

    def addCourse(self, course):
        self._courses.append(course)

    def removeCourse(self, course):
        for i, c in self._courses:
            if c.name == course.name:
                find = i
                break

        self._courses = self._courses[:find].extend(self._courses[find + 1:])


class Course:
    def __init__(self, name, isAdvanced):
        self._name = name
        self._isAdvanced = isAdvanced

    @property
    def name(self):
        return self._name

    @property
    def isAdvanced(self):
        return self._isAdvanced


aPerson = Person("will")
filter(lambda c: c.isAdvanced, aPerson.courses)
aPerson.addCourse(Course("hello", False))
