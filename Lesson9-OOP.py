#1. car class
class Car:
    def __init__(self, brand, color, volume):
        self.car_brand = brand
        self.car_color = color
        self.car_volume = volume

    @staticmethod
    def go_forward():
        print("Goes forward")

    @staticmethod
    def go_backward():
        print("Goes backward")

class CarModern(Car):
    @staticmethod
    def go_right():
        print("Goes right")

    @staticmethod
    def go_left():
        print("Goes left")



car1 = Car('Audi', 'blue', 2.5)
car2 = CarModern('BMW', 'blue', 3)

print(car1.car_volume)
car1.go_forward()
car2.go_backward()
car2.go_right()

print()
#2.very long task description
class TextProcessor:
    def __init__(self):
        self.my_punctuation = ',.!?'
        self.__True_or_False = None

    def get_clean_string(self, txt):
        clean_txt = ''
        for char in txt:
            if char in self.my_punctuation:
                continue
            else:
                clean_txt += char
        return clean_txt


    def __is_punktiation(self):
        for simbol in self.my_punctuation:
            if simbol in self.my_punctuation:
                __True_or_False = True
                return __True_or_False
            else:
                __True_or_False = False
                return __True_or_False

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_text(self, txt):
        self.__clean_string = self.__text_processor.get_clean_string(txt)
        return self.__clean_string

    @property
    def clean_string(self):
        print("This is your cleaned text: ")
        return self.__clean_string

class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self):
        while True:
            print("Insert your text for cleaning or press Q if you already done ")
            txt = input()
            result = self._text_loader.set_clean_text(txt)
            output = self._text_loader.clean_string
            print(output)
            if txt == "Q":
                break

txt1 = DataInterface()
txt1.process_texts()

print()
#3.class Parallelogram
class Parallelogram:
    def __init__(self, width, length):
        self.fig_width = width
        self.fig_length = length

    def get_area(self):
        return self.fig_width*self.fig_length

class Square(Parallelogram):
    def get_area(self):
        return self.fig_width*self.fig_width


my_fig = Square(10,15)
print(my_fig.get_area())

