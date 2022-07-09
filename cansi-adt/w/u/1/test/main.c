
#include "Customer.h"

#include <stdlib.h>
#include <stdio.h>


/*****************************************************************************
 *                                                                           *
 *  --------------------------------- main --------------------------------- *
 *                                                                           *
 *****************************************************************************/

int
main (int argc, char *argv[])
{

    const char* name1 = "Ivan Lopes";
    const Address address1 =
    {
        .city = "Rio de Janeiro",
        .street = "Rua Maia Lacerda"
    };

    const char* name2 = "Adriana";
    const Address address2 =
    {
        .city = "Rio de Janeiro",
        .street = "Travessa dos Tamoios"
    };

    CustomerPtr customer1 = createCustomer (name1, &address1);
    CustomerPtr customer2 = createCustomer (name2, &address2);

    displayCustomer    (customer1);
    displayCustomer    (customer2);

    destroyCustomer (customer1);
    destroyCustomer (customer2);

    return EXIT_SUCCESS;
}

/* -*- vim: set ts=4 sw=4 tw=78 ft=c: -*- */


