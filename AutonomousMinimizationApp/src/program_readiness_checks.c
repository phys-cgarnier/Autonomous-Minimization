#include <stdio.h>
#include <dbCommon.h>
#include <subRecord.h>
#include <registryFunction.h>
#include <epicsExport.h>

// Custom subroutine function
static long subChecksInit(struct subRecord *psub){
    printf("subInit was called\n");
    return 0;
}

static long subChecksProcess(struct subRecord *psub){
    // Access inputs
    int inpa = psub->a;
    // Print the values to the IOC console
    //printf("subRecord '%s' called with INPA=%.2f\n", psub->name, inpa);
    print('called subChecksProcess')
    // Perform optional computation (here, we'll set the VAL field to INPA + INPB)

    psub->val = inpa;

    // Return 0 for success
    return 0;
}

// Register the function with EPICS
epicsRegisterFunction(subChecksInit);
epicsRegisterFunction(subChecksProcess);