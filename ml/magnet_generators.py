from ml.device_generator import Generator
from typing import List, Dict, Any

class MagnetGenerator(Generator):
    magnet_types: List = ['XCOR', 'YCOR', 'QUAD', 'KICK']

    def config_contents(self):
        return None