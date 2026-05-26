from src.floors.primary_school.first_floor.corridor import Corridor
from src.floors.students import Students

def main():
    my_corridor = Corridor("Главный коридор")
    Vase = Students("Вася")
    Vase.run(my_corridor)
    
if __name__ == "__main__":
    main()