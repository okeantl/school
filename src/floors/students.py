from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.floors.primary_school.first_floor.corridor import Corridor

class Students:
    def __init__(self, name: str):
        self.name = name
        
        
    def run(self, corridor: 'Corridor'):
        print(f"В {corridor.class_name()} пробежал ученик, {self.name}")
        