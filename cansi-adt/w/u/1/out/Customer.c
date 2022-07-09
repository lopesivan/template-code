#include "Customer.h"
/*
#include "Address.h"
*/
#include "Order.h"

#include <stdlib.h>

struct Customer_t
{
    const char* name;
    Address address;
    size_t noOfOrders;
    Order orders[42];
};

#ifdef NOMEMMORY
#define MAX_NO_OF_CUSTOMERS 42

static struct Customer objectPool[MAX_NO_OF_CUSTOMERS];
static size_t numberOfObjects = 0;


CustomerPtr createCustomer(const char* name, const Address* address)
{
    CustomerPtr customer = NULL;

    if (numberOfObjects < MAX_NO_OF_CUSTOMERS)
    {
        customer = &objectPool[numberOfObjects++];
        /* Initialize the object... */
        /* Initialize each field in the customer... */
        customer->name = name;
        customer->address = address;
    }

    return customer;
}


void destroyCustomer(CustomerPtr customer)
{
    /* Perform clean-up of the customer internals, if necessary.
    free (customer);
    */
}

#else

CustomerPtr createCustomer(const char* name, const Address* address)
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


void destroyCustomer(CustomerPtr customer)
{
    /* Perform clean-up of the customer internals, if necessary. */
    free (customer);
}
#endif

void displayCustomer(CustomerPtr customer)
{
    printf ("Name:\t%s\nCity:\t%s\nStreet:\t%s\n",
            customer->name,
            customer->address.street,
            customer->address.city)
    ;
}

