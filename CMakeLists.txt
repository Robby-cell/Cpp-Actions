cmake_minimum_required(VERSION 3.15)
project(cpp-actions CXX)

add_executable(cpp-actions src/main.cpp)

install(TARGETS cpp-actions DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
