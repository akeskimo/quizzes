# compile tests (with Catch2)
Include(FetchContent)

FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG        v2.13.1)

FetchContent_MakeAvailable(Catch2)

add_executable(Tests tests_main.cpp tests_linkedlist.cpp)

target_link_libraries(Tests Catch2::Catch2)

add_test(test_all Tests)
