cmake_minimum_required(VERSION 3.5)
project(state)

set(CMAKE_C_STANDARD 99)
set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_C_FLAGS "-Wall -Werror")

FILE(GLOB MyCSources *.c)
FILE(GLOB MyCHeaders *.h)

set(SOURCE_FILES ${MyCSources} ${MyCHeaders})
add_executable(main ${SOURCE_FILES})
