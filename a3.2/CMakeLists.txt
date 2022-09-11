CMAKE_MINIMUM_REQUIRED(VERSION 3.23)
project(sudokucheck)

set(CXX_FLAGS "-Wall -std=c++20 -O2 -march=native")

FILE(GLOB SOURCE_FILES cpp/*.cpp )

add_executable(sudokucheck ${SOURCE_FILES})

target_include_directories(sudokucheck PRIVATE include)
