from src.floors.primary_school.first_floor.first_floor import Corridor, Vxod, Wardrobe
from src.floors.students import Students


def main():
    my_vxod = Vxod()
    my_corridor = Corridor()
    my_wardrobe = Wardrobe()
    Vase = Students("Вася")
    Vase.run(my_corridor)
    Vase.vxod(my_vxod)
    Vase.wardrobe(my_wardrobe)
    
if __name__ == "__main__":
    main()