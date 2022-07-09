#include "DoisState.h"
#include "EstadoStateInternal.h"

/* Possible transition to the following state: */
#include "TresState.h"

#include "message.h" // DEBUG

static void tresEstado (EstadoStatePtr state)
{
    message ("** tresEstado **");

    transitionToTres (state);
}

void transitionToDois (EstadoStatePtr state)
{

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    defaultImplementation (state);
    state->func = tresEstado;
}

