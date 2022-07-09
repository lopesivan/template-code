#include "array.h"
#include "data.h"
#include <stdlib.h>

struct Array
{
    unsigned int size;
    Data data;
};

Array_ptr createArray
    (unsigned int size)
{
    Array_ptr array = malloc (sizeof *array);

    if (array)
    {
        /* Initialize each field in the array... */
    }

    return array;
}

void destroyArray
    (Array_ptr array)
{
    /* Perform clean-up of the array internals, if necessary. */
    free (array);
}
