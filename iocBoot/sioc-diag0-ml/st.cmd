#!../../bin/rhel9-x86_64/AutonomousMinimization

#- You may have to change AutonomousMinimization to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"
#epicsEnvSet(PYTHONPATH, "$(PYTHONPATH):$(EPICS_SITE_TOP)/R7.0.3.1-1.0/modules/pyDevSup/R1.2-0.0.2PY3.10/python3.10/rhel7-x86_64:../../../../lcls-tools")
epicsEnvSet(PYTHONPATH, "$(PYTHONPATH):/sdf/home/c/cgarnier/autonomous_diag0/lcls-tools")
epicsEnvSet(BEAMLINE, "DIAG0")


#epicsEnvSet("EPICS_CA_ENABLE_PREEMPTIVE_CALLBACK", "YES")
#export EPICS_CA_AUTO_ADDR_LIST=NO
#export EPICS_CA_ADDR_LIST="lcls-prod01:5068 lcls-prod01:5063 mcc-dmz 134.79.219.255"
#export EPICS_CA_REPEATER_PORT="5069"
#export EPICS_CA_SERVER_PORT="5068"


epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST","NO")
#epicsEnvSet("EPICS_CA_ADDR_LIST", "lcls-prod01:5068 lcls-prod01:5063 mcc-dmz")
#epicsEnvSet("EPICS_CA_REPEATER_PORT","5069")
epicsEnvSet("EPICS_CA_ADDR_LIST", "127.0.0.1")
epicsEnvSet("EPICS_CA_SERVER_PORT", "10514")


## Register all support components
dbLoadDatabase("dbd/AutonomousMinimization.dbd")
AutonomousMinimization_registerRecordDeviceDriver(pdbbase)

## Load record instances


py("import epics; print(epics.ca.initialize_libca())")

#dbLoadRecords("db/test.db","user=cgarnier")
#dbLoadRecords("db/test_pydevsup.db")
#dbLoadRecords("db/launch_ml_jobs.db")
dbLoadRecords("db/program.db")
#scanOnceSetQueueSize(8000)

#callbackSetQueueSize(5000)
#scanOnceSetQueueSize(5000)

# Load common Access Configuration File
#< ${ACF_INIT}

cd("${TOP}/iocBoot/${IOC}")
iocInit()

## Start any sequence programs
#seq sncxxx,"user=cgarnier"
