cmake_minimum_required(VERSION 3.5)
project(adt)

set(CMAKE_C_STANDARD 99)
SET(CMAKE_VERBOSE_MAKEFILE ON)
SET(CMAKE_C_FLAGS "-Wall -Werror")

set(SOURCE_FILES main.c MemoryPollAluno.c Aluno.h Order.h Address.h)
add_executable(main ${SOURCE_FILES})