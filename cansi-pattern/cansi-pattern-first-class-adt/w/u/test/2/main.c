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

#include "Aluno.h"

#include <stdlib.h>
#include "main.h"

// in .c
const char* Names[]  = { "first",
                         "second",
                         "third"
                       };

const char* Cities[] = { "Rio de Janeiro",
                         "Brasília",
                         "Ceará"
                       };

const char* Streets[] = { "Praça Quinze",
                          "Avenida Francisco Bicalho",
                          "Republica do Líbano"
                        };


void f (const char **name, int index);
void h (Address *adress,   int index);
void g (Address *adress,  int index);

/*****************************************************************************
 *                                                                           *
 *  --------------------------------- main --------------------------------- *
 *                                                                           *
 *****************************************************************************/


int
main (int argc, char *argv[])
{
    const char *name;
    Address address;

    /*{
        .city   = "Rio de Janeiro",
        .street = "Rua Maia Lacerda"
    };*/

    for (int i = 0; i < 2; ++i)
    {
        f (&name, i);
        g (&address,i);
        h (&address,i);

        AlunoPtr  aluno = createAluno (name, &address);
        showAluno (aluno);
        destroyAluno (aluno);
    }

    return EXIT_SUCCESS;
}

void f (const char **name, int index)
{
    (*name) = Names[index];
}

void h (Address *address, int index)
{
    address->street = Streets[index];
}

void g (Address *address, int index)
{
    address->city = Cities[index];
}

/* -*- vim: set ts=4 sw=4 tw=78 ft=c: -*- */