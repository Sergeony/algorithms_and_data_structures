/* Lab_4
   1) Individual task: 20 % 18 = 2
        2. Освіта {вища / середня, технічна, є працевлаштування}

   2) Results:
        - Getting a field from a structure and from an array takes
        approximately the same time.
*/
#include <iostream>
#include <bitset>
#include <string>
#include <ctime>

using namespace std;

template <class T> void print_data_in_machine_representation(T &x);


struct Education{
    string educationType;
    bool is_tech;
    bool is_employed;
};

int main()
{
    Education student_1 = {"higher", true, true};
    Education students[] = {{"higher", false, true},
                            {"secondary", false, false}};

    cout << "struct_1: ";
    print_data_in_machine_representation(student_1);

    int start = clock();
    student_1.is_tech;
    int end = clock();
    int runtime = end - start;
    cout << "struct_1 runtime: " << runtime << endl << endl;

    cout << "struct array: ";
    print_data_in_machine_representation(students);

    start = clock();
    students[1].is_tech;
    end = clock();
    runtime = end - start;
    cout << "struct array runtime: " << runtime << endl;

    return 0;
}

template <class T> void print_data_in_machine_representation(T &x){
    for (size_t i = 0; i < sizeof x; i++)
        cout << ' ' << bitset<8>(reinterpret_cast<unsigned char *>(&x)[i]);

    cout << ";" << endl;
}
