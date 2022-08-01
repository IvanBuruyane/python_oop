from typing import Any


class LessonItem:

    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value) -> None:
        keys = {
            "title": "str",
            "practices": "int > 0",
            "duration": "int > 0"
        }
        if key in keys:
            if not self.is_attr_valid(value, keys[key]):
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item) -> bool:
        return False

    def __delattr__(self, item) -> None:
        if item in ["title", "practices", "duration"]:
            pass

    @classmethod
    def is_attr_valid(cls, value: Any, rules: str) -> bool:
        types = {
            "int": int,
            "str": str,
            "list": list,
            "dict": dict,
            "float": float,
            "bool": bool
        }
        rule_list = rules.split(" ")
        _type = rule_list[0]
        if type(value) != types[_type]:
            print(type(value))
            return False
        if len(rule_list) > 1:
            sign = rule_list[1]
            boundary = float(rule_list[2])
            if sign == ">":
                return value > boundary
            elif sign == "<":
                return value < boundary
            elif sign == "==":
                return value == boundary
            elif sign == "!=":
                return value != boundary
            elif sign == ">=":
                return value >= boundary
            elif sign == "<=":
                return value <= boundary
        return True


class Module:

    def __init__(self, name: str) -> None:
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:

    def __init__(self, name: str) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
for module in course.modules:
    print(f"module: {module.name}")
    for lesson in module.lessons:
        print(f"    lesson: {lesson.title}")


# less = LessonItem("Lesson", 343, 434)
# less.__delattr__("title")
# print(less.__dict__)
