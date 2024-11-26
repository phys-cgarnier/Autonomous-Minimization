#!../../bin/rhel7-x86_64/AutonomousMinimization

#- You may have to change AutonomousMinimization to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"
#epicsEnvSet(PYTHONPATH, "$(PYTHONPATH):$(EPICS_SITE_TOP)/R7.0.3.1-1.0/modules/pyDevSup/R1.2-0.0.2/python3.8/rhel7-x86_64")
epicsEnvSet(BEAMLINE, "DIAG0")
## Register all support components
dbLoadDatabase("dbd/AutonomousMinimization.dbd")
AutonomousMinimization_registerRecordDeviceDriver(pdbbase)

## Load record instances

py("import test_support;")
py("test_support.hello_world()")
#py("import device_and_db_gen;")
#py("device_and_db_gen.meme_service()")
py("from magnet_generators import MagnetGenerator;")
py("print(MagnetGenerator(beamline='DIAG0').device_list)")
py
dbLoadRecords("db/test.db","user=cgarnier")
cd("${TOP}/iocBoot/${IOC}")
iocInit()

## Start any sequence programs
#seq sncxxx,"user=cgarnier"
