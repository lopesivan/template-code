#include "Point2d.h"
/*
#include "Real.h"
#include "Integer.h"
*/
#include <stdlib.h>

struct Point2d_t
{
    Real x;
    Real y;
};

Point2dPtr createPoint2d(Real x, Real y)
{
    Point2dPtr point2d = malloc (sizeof *point2d);

    if (NULL != point2d)
    {
        /* Initialize each field in the point2d... */
        point2d->x = x;
        point2d->y = y;
    }

    return point2d;
}


void showPoint2d(Point2dPtr point2d)
{
    printf ("%s\n", "Not implemented yet");
}

void destroyPoint2d(Point2dPtr point2d)
{
    /* Perform clean-up of the point2d internals, if necessary. */
    free (point2d);
}
