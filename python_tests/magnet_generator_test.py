from  ml.magnet_generators import MagnetGenerator


magnet_db_generator = MagnetGenerator(beamline = 'DIAG0')
print('here')
#print(magnet_db_generator.__dict__)
print(magnet_db_generator.device_list)