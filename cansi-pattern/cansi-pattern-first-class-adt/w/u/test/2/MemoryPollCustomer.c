#include "Aluno.h"
#include "Address.h"

struct Aluno
{
    const char* name;
    Address address;
};

#define MAX_NO_OF_ALUNOS 42

static struct Aluno objectPool[MAX_NO_OF_ALUNOS];
static size_t numberOfObjects = 0;

AlunoPtr createAluno
(
    const char* name,
    const Address* address
)
{
    AlunoPtr aluno = NULL;

    if (numberOfObjects < MAX_NO_OF_ALUNOS)
    {
        aluno = &objectPool[numberOfObjects++];
        /* Initialize the object... */
    }
    return aluno;
}

void destroyAluno
(AlunoPtr aluno)
{
    /*
      In case de-allocation is needed, an array will still do, but a more
      sophisticated method for keeping track of "allocated" objects will be
      needed.  However, such an algorithm is outside the scope of this book.
    */
}

