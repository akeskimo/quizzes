
# CMake 3.14 is to support fetching git content
# with more abbreviated syntax.
cmake_minimum_required (VERSION 3.14)

# set project name and version
project (Quizzes VERSION 0.0)

# enforce C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# add configuration file for project version
configure_file(QuizzesConfig.h.in QuizzesConfig.h)

enable_testing()

# add sub-projects
add_subdirectory(src)
add_subdirectory(tests)