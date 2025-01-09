TOP=../..

include $(TOP)/configure/CONFIG
include $(PYDEVSUP)/configure/CONFIG_PY
# Build the IOC application
PROD_IOC = AutonomousMinimization
DBD += AutonomousMinimization.dbd
AutonomousMinimization_DBD += base.dbd
AutonomousMinimization_DBD += elaunchSupport.dbd

# maybe have to comment out
AutonomousMinimization_DBD += pyDevSup.dbd
AutonomousMinimization_LIBS += pyDevSup$(PY_LD_VER)

# AutonomousMinimization_registerRecordDeviceDriver.cpp derives from AutonomousMinimization.dbd
AutonomousMinimization_SRCS += AutonomousMinimization_registerRecordDeviceDriver.cpp
# Build the main IOC entry point on workstation OSs.
AutonomousMinimization_SRCS_DEFAULT += AutonomousMinimizationMain.cpp
AutonomousMinimization_SRCS_vxWorks += -nil-

AutonomousMinimization_SRCS += launcher.c
AutonomousMinimization_SRCS += program_readiness_checks.c

# AutonomousMinimization.dbd will be created and installed


# AutonomousMinimization.dbd will be made up from these files:


# Include dbd files from all support applications:
#AutonomousMinimization_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#AutonomousMinimization_LIBS += xxx

# Add support from base/src/vxWorks if needed
#AutonomousMinimization_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
AutonomousMinimization_LIBS += $(EPICS_BASE_IOC_LIBS)
AutonomousMinimization_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
#AutonomousMinimization_LIBS += $(PYDEVSUP)/lib/$(EPICS_HOST_ARCH)/libPyDevSup

#how can I see what rfal app is using as PY_LD_VER
#rfal also has
SYS_PROD_LIBS_DEFAULT += python$(PY_LD_VER)
#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

