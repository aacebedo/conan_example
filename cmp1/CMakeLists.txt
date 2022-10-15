cmake_minimum_required(VERSION 3.23)
project(cmp1 LANGUAGES C)

add_library(cmp1 SHARED src/cmp1.c)
target_include_directories(cmp1 PUBLIC include)
set_target_properties(cmp1 PROPERTIES PUBLIC_HEADER "include/cmp1.h")

install(TARGETS cmp1)
