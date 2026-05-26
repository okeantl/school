from src.floors.primary_school.first_floor.first_floor import Corridor, Vxod, Wardrobe, SportZal
from src.floors.students import Students


def main():
    my_vxod = Vxod()
    my_corridor = Corridor()
    my_wardrobe = Wardrobe()
    my_sportzal = SportZal()
    Vase = Students("Вася")
    Vase.run(my_corridor)
    Vase.vxod(my_vxod)
    Vase.wardrobe(my_wardrobe)
    Vase.sportzal(my_wardrobe, my_sportzal)
    Vase.undress(my_wardrobe)
    Vase.changed_clothes(my_wardrobe, my_sportzal)
    
if __name__ == "__main__":
    main()