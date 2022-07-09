#include "TresState.h"
#include "EstadoStateInternal.h"

/* Possible transition to the following state: */
#include "QuatroState.h"

#include "message.h" // DEBUG

static void quatroEstado (EstadoStatePtr state)
{
    message ("** quatroEstado **");

    transitionToQuatro (state);
}

void transitionToTres (EstadoStatePtr state)
{
    message ("** transitionToTres **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    defaultImplementation (state);
    state->func = quatroEstado;
}

