#ifndef ALUNO_H
#define ALUNO_H

#include "Address.h"

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct Aluno* AlunoPtr;

/*
Create a Aluno and return a handle to it.
*/
AlunoPtr createAluno (const char* name, const Address* address);

/*
Destroy the given Aluno object.
All handles to it will be invalidated.
*/
void destroyAluno (AlunoPtr aluno);

void showAluno (AlunoPtr aluno);
#endif
