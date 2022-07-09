#include "Customer.h"
#include "Order.h"
#include <stdlib.h>
#include <stdio.h>

struct Customer
{
    const char* name;
    Address address;
};

CustomerPtr createCustomer (const char* name, const Address* address)
{
    CustomerPtr customer = malloc (sizeof *customer);

    if (NULL != customer)
    {
        /* Initialize each field in the customer... */
        customer->name = name;
        customer->address = *address;
    }

    return customer;
}


void showCustomer (CustomerPtr customer)
{
    printf ("Name:\t%s\nCity:\t%s\nStreet:\t%s\n",
            customer->name,
            customer->address.street,
            customer->address.city)
    ;
}

void destroyCustomer (CustomerPtr customer)
{
    /* Perform clean-up of the customer internals, if necessary. */
    free (customer);
}
