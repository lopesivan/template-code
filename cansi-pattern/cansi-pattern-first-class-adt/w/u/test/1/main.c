/*
 *                     __ __       ___
 *                    /\ \\ \    /'___`\
 *                    \ \ \\ \  /\_\ /\ \
 *                     \ \ \\ \_\/_/// /__
 *                      \ \__ ,__\ // /_\ \
 *                       \/_/\_\_//\______/
 *                          \/_/  \/_____/
 *                                        Algoritmos
 *
 *
 *      Author: Ivan Lopes
 *        Mail: ivan@42algoritmos.com.br
 *        Site: http://www.42algoritmos.com.br
 *     License: gpl
 *    Language: C ansi
 *        File: main.c
 *        Date: Ter 21 Nov 2017 13:03:05 -02
 * Description:
 */

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

    const char* name = "Ivan Lopes";
    const Address address =
    {
        .city = "Rio de Janeiro",
        .street = "Rua Maia Lacerda"
    };

    CustomerPtr  customer = createCustomer (name, &address);
    showCustomer (customer);
    destroyCustomer (customer);

    return EXIT_SUCCESS;
}

/* -*- vim: set ts=4 sw=4 tw=78 ft=c: -*- */

