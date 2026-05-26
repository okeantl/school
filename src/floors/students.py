from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.floors.primary_school.first_floor.first_floor import Corridor, Vxod, Wardrobe
        
class Students:
    def __init__(self, name: str):
        self.name = name
        
        
    def run(self, corridor: 'Corridor'):
        print(f"В {corridor.log_info()} пробежал ученик, {self.name}")
        
    def vxod(self, vxod: 'Vxod'):
        print(f"В школу через главный {vxod.log_info()}, зашел ученик, {self.name}")
        
    def wardrobe(self, wardrobe: 'Wardrobe'):
        print(f"В {wardrobe.log_info()}, зашел ученик, {self.name}")