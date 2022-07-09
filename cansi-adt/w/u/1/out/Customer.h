#ifndef CUSTOMER_H
#define CUSTOMER_H

#include "Address.h"

#include <stdio.h>

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct Customer_t *CustomerPtr;

/*
Create a Customer and return a handle to it.
*/
CustomerPtr createCustomer(const char* name, const Address* address);

/*
Destroy the given Customer object.
All handles to it will be invalidated.
*/
void destroyCustomer(CustomerPtr customer);

/*
Print the given Customer object.
*/
void displayCustomer(CustomerPtr customer);
#endif
