#ifndef ARRAY_H
#define ARRAY_H

#include "data.h"

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct Array* Array_ptr;

/*
Create a Array and return a handle to it.
*/
Array_ptr createArray
    (unsigned int size);

/*
Destroy the given Array object.
All handles to it will be invalidated.
*/
void destroyArray
    (Array_ptr array);

#endif
