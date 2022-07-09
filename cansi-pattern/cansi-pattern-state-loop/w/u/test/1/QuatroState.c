#include "QuatroState.h"
#include "EstadoStateInternal.h"

/* Possible transition to the following state: */
#include "CincoState.h"

#include "message.h" // DEBUG

static void cincoEstado (EstadoStatePtr state)
{
    message ("** cincoEstado **");

    transitionToCinco (state);
}

void transitionToQuatro (EstadoStatePtr state)
{
    message ("** transitionToQuatro **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    defaultImplementation (state);
    state->func = cincoEstado;
}

