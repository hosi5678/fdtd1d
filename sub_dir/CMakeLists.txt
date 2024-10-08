# cmakeのversion指定
cmake_minimum_required(VERSION 3.5)
cmake_policy(SET CMP0148 NEW)

find_package(Python REQUIRED COMPONENTS Interpreter Development)

# compilerの指定
set(CMAKE_CXX_COMPILER "/usr/bin/g++-11")
set(CMAKE_SUPPRESS_DEVELOPER_WARNINGS 1)

# python include directory
find_package(Python3 COMPONENTS Development REQUIRED)

include_directories(${Python3_INCLUDE_DIRS} /usr/include/python3.11)
include_directories(${Python3_NumPy_INCLUDE_DIRS})

# project名の設定
project(cpp_lib)

# file名 .cppを収集する
file(GLOB_RECURSE SOURCES "./src/*.cpp")

# cppが増えてきたら外す。
# projectに.cpp filesをつける
add_library(cpp_lib STATIC ${SOURCES})

# projectに.hppをつける
target_include_directories(cpp_lib INTERFACE ./include)

target_link_libraries(cpp_lib ${Python_LIBRARIES})

# math.hが使えるようにする
target_link_libraries(cpp_lib m)
