#include <stdio.h>
#include <dbCommon.h>
#include <subRecord.h>
#include <registryFunction.h>
#include <epicsExport.h>

// Custom subroutine function
long checks(subRecord *precord) {
    // Access inputs
    double inpa = precord->a;
    double inpb = precord->b;

    // Print the values to the IOC console
    printf("subRecord '%s' called with INPA=%.2f and INPB=%.2f\n", precord->name, inpa, inpb);

    // Perform optional computation (here, we'll set the VAL field to INPA + INPB)
    int result = 1
    precord->val = result;

    // Return 0 for success
    return 0;
}

// Register the function with EPICS
epicsRegisterFunction(checks);