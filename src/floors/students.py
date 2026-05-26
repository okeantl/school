from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.floors.primary_school.first_floor.first_floor import Corridor, Vxod, Wardrobe, SportZal
        
class Students:
    def __init__(self, name: str):
        self.name = name
        
        
    def run(self, corridor: 'Corridor'):
        print(f"В {corridor.log_info()} пробежал ученик, {self.name}")
        
    def vxod(self, vxod: 'Vxod'):
        print(f"В школу через главный {vxod.log_info()}, зашел ученик, {self.name}")
        
    def wardrobe(self, wardrobe: 'Wardrobe'):
        print(f"В {wardrobe.log_info()}, зашел ученик, {self.name}")
        
    def sportzal(self, wardrobe: 'Wardrobe', sportzal: 'SportZal'):
        print(f"{self.name} пошел в {wardrobe.log_info()}, переодеваться в {sportzal.log_info()}")
        
    def undress(self, wardrobe: 'Wardrobe'):
        print(f"{self.name} разделся, чтобы пойти на урок, когда зашел в {wardrobe.log_info()}")
        
    def changed_clothes(self, wardrobe: 'Wardrobe', sportzal: 'SportZal'):
        print(f"{self.name} зашел в {wardrobe.log_info()} переодеться, чтобы пойти в {sportzal.log_info()}")