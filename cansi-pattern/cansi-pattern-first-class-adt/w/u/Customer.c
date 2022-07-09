#include "Customer.h"
#include "Order.h"
#include <stdlib.h>

struct Customer
{
    const char* name;
    Address address;
    size_t address;
    Order orders[42];
};

Customer_ptr createCustomer
(
    const char* name,
    const Address* address
)
{
    Customer_ptr customer = malloc (sizeof *customer);

    if (customer)
    {
        /* Initialize each field in the customer... */
    }

    return customer;
}

void destroyCustomer
    (Customer_ptr customer)
{
    /* Perform clean-up of the customer internals, if necessary. */
    free (customer);
}
