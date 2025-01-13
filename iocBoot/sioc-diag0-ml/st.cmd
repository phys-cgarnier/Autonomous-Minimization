#!../../bin/rhel7-x86_64/AutonomousMinimization

#- You may have to change AutonomousMinimization to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"
#epicsEnvSet(PYTHONPATH, "$(PYTHONPATH):$(EPICS_SITE_TOP)/R7.0.3.1-1.0/modules/pyDevSup/R1.2-0.0.2PY3.10/python3.10/rhel7-x86_64")
epicsEnvSet(BEAMLINE, "DIAG0")
## Register all support components
dbLoadDatabase("dbd/AutonomousMinimization.dbd")
AutonomousMinimization_registerRecordDeviceDriver(pdbbase)

## Load record instances


#py("from magnet_generators import MagnetGenerator;")
#py("print(MagnetGenerator(beamline='DIAG0').device_list)")

#dbLoadRecords("db/test.db","user=cgarnier")
#dbLoadRecords("db/test_pydevsup.db")
dbLoadRecords("db/launch_ml_jobs.db")
#scanOnceSetQueueSize(8000)


# Load common Access Configuration File
#< ${ACF_INIT}

cd("${TOP}/iocBoot/${IOC}")
iocInit()

## Start any sequence programs
#seq sncxxx,"user=cgarnier"
