#include "CincoState.h"
#include "EstadoStateInternal.h"

/* Possible transition to the following state: */
#include "FimState.h"

#include "message.h" // DEBUG

static void fimEstado (EstadoStatePtr state)
{
    message ("** fimEstado **");

    transitionToFim (state);
}

void transitionToCinco (EstadoStatePtr state)
{

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    defaultImplementation (state);
    state->func = fimEstado;
}

