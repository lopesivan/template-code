#include "Aluno.h"
//#include "Address.h"
//#include "Order.h"
#include <stdlib.h>
#include <stdio.h>

struct Aluno
{
    const char* name;
    Address address;
};

AlunoPtr createAluno (const char* name, const Address* address)
{
    AlunoPtr aluno = malloc (sizeof *aluno);

    if (NULL != aluno)
    {
        /* Initialize each field in the aluno... */
        aluno->name = name;
        aluno->address = *address;
    }

    return aluno;
}


void showAluno (AlunoPtr aluno)
{
    printf ("Name:\t%s\nCity:\t%s\nStreet:\t%s\n",
            aluno->name,
            aluno->address.city,
            aluno->address.street)
    ;
}

void destroyAluno (AlunoPtr aluno)
{
    /* Perform clean-up of the aluno internals, if necessary. */
    free (aluno);
}
