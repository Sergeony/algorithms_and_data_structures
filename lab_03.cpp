/* Lab_3
   1) Individual task: N=20
        20. int, long double, char, int 3D array

   2) Results:
        - Int type contains 4*8 bits and starts from the left.
        - Long double type contains 16*8 bits.
        - The char type contains 8 bits because it uses the ASCII encoding with values 128=2^7,
            the most significant bit is used for pseudo graphics and national fonts.
        - Int 3D array type contains int_length * number_count sequential bits like a linear array.
*/
#include <iostream>
#include <bitset>

using namespace std;

template <class T> void print_data_in_machine_representation(T &x);

int main()
{
    int data_1 = 255;
    long double data_2 = 5.5;
    char data_3 = '~';
    int data_4[2][2][2] = {{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}};

    cout << "INT: ";
    print_data_in_machine_representation(data_1);

    cout << "LONG DOUBLE: ";
    print_data_in_machine_representation(data_2);

    cout << "CHAR: ";
    print_data_in_machine_representation(data_3);

    cout << "INT 3D ARRAY: ";
    print_data_in_machine_representation(data_4);

    return 0;
}

template <class T> void print_data_in_machine_representation(T &x){
    for (size_t i = 0; i < sizeof x; i++)
        cout << ' ' << bitset<8>(reinterpret_cast<unsigned char *>(&x)[i]);

    cout << ";" << endl;
}
