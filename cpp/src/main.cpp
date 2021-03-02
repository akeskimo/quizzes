#include <iostream>
#include "QuizzesConfig.h"


int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cout << "Version " << Quizzes_VERSION_MAJOR << "." << Quizzes_VERSION_MINOR << std::endl;
        return 0;
    }

    return 0;
}
