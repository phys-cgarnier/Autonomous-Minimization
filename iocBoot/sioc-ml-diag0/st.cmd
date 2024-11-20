#!../../bin/rhel7-x86_64/AutonomousMinimization

#- You may have to change AutonomousMinimization to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/AutonomousMinimization.dbd")
AutonomousMinimization_registerRecordDeviceDriver(pdbbase)

## Load record instances

py("import test_support;")
py("test_support.hello_world()")
dbLoadRecords("db/test.db","user=cgarnier")
cd("${TOP}/iocBoot/${IOC}")
iocInit()

## Start any sequence programs
#seq sncxxx,"user=cgarnier"
