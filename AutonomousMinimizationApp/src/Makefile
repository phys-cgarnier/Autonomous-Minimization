TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = AutonomousMinimization
# AutonomousMinimization.dbd will be created and installed
DBD += AutonomousMinimization.dbd

# AutonomousMinimization.dbd will be made up from these files:
AutonomousMinimization_DBD += base.dbd

# Include dbd files from all support applications:
#AutonomousMinimization_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#AutonomousMinimization_LIBS += xxx

# AutonomousMinimization_registerRecordDeviceDriver.cpp derives from AutonomousMinimization.dbd
AutonomousMinimization_SRCS += AutonomousMinimization_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
AutonomousMinimization_SRCS_DEFAULT += AutonomousMinimizationMain.cpp
AutonomousMinimization_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#AutonomousMinimization_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
AutonomousMinimization_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

