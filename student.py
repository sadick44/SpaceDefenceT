class Student:

    """
        We use classes to represent real worls entities such as Student, Teacher, 
        Animal and so on.
    """
    
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f'{self.name} from {self.house}'
    
    @property # syntax for getter
    def house(self):
        return self._house
    
    @property
    def name(self):
        return self._name
    
    
    @house.setter # syntax for setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw']:
            raise ValueError('Invalid house')
        self._house = house


    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')
        self._name = name
    

def main():
    print(get_student())


def get_student():
    name = input('Name: ')
    house = input('House: ')

    return Student(name, house)


if __name__ == "__main__":
    main()