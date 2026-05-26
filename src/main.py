from src.floors.primary_school.first_floor.corridor import Corridor
from src.floors.primary_school.first_floor.vxod import Vxod
from src.floors.students import Students


def main():
    my_vxod = Vxod()
    my_corridor = Corridor()
    Vase = Students("Вася")
    Vase.run(my_corridor)
    Vase.vxod(my_vxod)
    
if __name__ == "__main__":
    main()