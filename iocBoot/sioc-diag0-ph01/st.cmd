#!../../bin/rhel7-x86_64/AutonomousMinimization

#- You may have to change AutonomousMinimization to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"
epicsEnvSet(PYTHONPATH, "$(PYTHONPATH):$(EPICS_SITE_TOP)/R7.0.3.1-1.0/modules/pyDevSup/R1.2-0.0.2PY3.10/python3.10/rhel7-x86_64")
# for setup on dev-srv09 comment out line about and uncomment these

#epicsEnvSet("EPICS_CA_ADDR_LIST", "127.0.0.1")
#epicsEnvSet("EPICS_CA_SERVER_PORT", "10514")


## Register all support components
dbLoadDatabase("dbd/AutonomousMinimization.dbd")
AutonomousMinimization_registerRecordDeviceDriver(pdbbase)

py("import epics; print(epics.ca.initialize_libca())")

## Load record instances
dbLoadRecords("db/program.db")

# Load common Access Configuration File
#< ${ACF_INIT}

cd("${TOP}/iocBoot/${IOC}")
iocInit()

## Start any sequence programs
#seq sncxxx,"user=cgarnier"
