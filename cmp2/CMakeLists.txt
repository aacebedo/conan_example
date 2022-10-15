cmake_minimum_required(VERSION 3.23)
project(cmp2 LANGUAGES C)

find_package(cmp1 REQUIRED)

add_executable(cmp2 src/cmp2.c)
target_include_directories(cmp2 PRIVATE include)

target_link_libraries(cmp2 cmp1)

install(TARGETS cmp2)
