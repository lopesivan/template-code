#ifndef POINT2D_H
#define POINT2D_H

#include "Real.h"

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct Point2d_t *Point2dPtr;

/*
Create a Point2d and return a handle to it.
*/
Point2dPtr createPoint2d(Real x, Real y);

/*
Destroy the given Point2d object.
All handles to it will be invalidated.
*/
void destroyPoint2d(Point2dPtr point2d);

/*
Print the given Point2d object.
*/
void displayPoint2d(Point2dPtr point2d);
#endif
