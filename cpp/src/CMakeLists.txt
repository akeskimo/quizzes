# embeds required source files in the built binary
add_executable(Quizzes linkedlist/linkedlist.cpp main.cpp)

# links binaries, i.e. configure_file, in the executable
target_include_directories(Quizzes PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )
