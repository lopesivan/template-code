#ifndef CONTEXTO_H
#define CONTEXTO_H

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct contexto* contextoPtr;

contextoPtr createEstado (void);
void destroyEstado (contextoPtr instance);
void statemachine (void);

#endif
