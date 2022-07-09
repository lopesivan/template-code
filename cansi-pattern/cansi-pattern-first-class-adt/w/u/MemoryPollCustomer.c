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

#define MAX_NO_OF_CUSTOMERS 42

static struct Customer objectPool[MAX_NO_OF_CUSTOMERS];
static size_t numberOfObjects = 0;

Customer_ptr createCustomer
(
    const char* name,
    const Address* address
)
{
    Customer_ptr customer = NULL;

    if (numberOfObjects < MAX_NO_OF_CUSTOMERS)
    {
        customer = &objectPool[numberOfObjects++];
        /* Initialize the object... */
    }
    return customer;
}

void destroyCustomer
    (Customer_ptr customer)
{
    /*
      In case de-allocation is needed, an array will still do, but a more
      sophisticated method for keeping track of "allocated" objects will be
      needed.  However, such an algorithm is outside the scope of this book.
    */
}

