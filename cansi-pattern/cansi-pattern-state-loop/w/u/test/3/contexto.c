#include "contexto.h"

/* We need to know about or initial state: */
#include "FimState.h"

/* We need to know about final state: */
//#include "CincoState.h"

#include "EstadoStateInternal.h"
#include <stdlib.h>

#include "message.h" // DEBUG

struct contexto
{
    struct EstadoState state;
};

/* Estatico */
/* USING:
    contextoPtr p = createEstado();
    umEstado(p);
*/
#define MAX_NO_OF_CONTEXTOS 2
static struct contexto objectPool[MAX_NO_OF_CONTEXTOS];
static size_t numberOfObjects = 0;

contextoPtr createEstado (void)
{
    message ("** createEstado **");

    contextoPtr instance = NULL;

    if (numberOfObjects < MAX_NO_OF_CONTEXTOS)
    {
        instance = &objectPool[numberOfObjects++];
        /* Initialize the object... */

        /* Specify the initial state. */
        transitionToFim (&instance->state);
        /* Initialize the other attributes here.*/
    }

    return instance;
}

void statemachine (void)
{
    message ("** statemachine **");

    contextoPtr instance = NULL;
    /* contextoPtr stop     = NULL; */

    if (numberOfObjects < MAX_NO_OF_CONTEXTOS)
    {
        instance = &objectPool[numberOfObjects++];
        /* stop     = &objectPool[numberOfObjects++]; */

        /* transitionToCinco (&stop->state); */
        transitionToFim (&instance->state);

        /* while (stop->state.func != instance->state.func) */
        while (1)
        {
            instance->state.func (&instance->state);
        }
    }
}

void destroyEstado (contextoPtr instance)
{
    message ("** destroyEstado **");

    //free (instance);
}
