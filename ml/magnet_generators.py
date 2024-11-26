from device_and_db_gen import Generator
from typing import List, Dict, Any

class MagnetGenerator(Generator):
    magnet_types: List = ['XCOR', 'YCOR', 'QUAD', 'KICK']
    def __init__(self):
