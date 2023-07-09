#include <iostream>

using namespace std;

int main(){
    int a = 9;
    int b = 3;
    cout << a + b << endl;
    cout << a - b << endl;
    cout << a * b << endl;
    cout << a / b << endl;
    cout << (a + b) * 0.5 << endl;
    bool c = a > b;
    cout << c << endl;
    bool d = a < b;
    cout << d << endl;
    cout << sizeof(a) << endl;
    int edades[] = {24, 40, 7};
    cout << sizeof(edades) << endl;
    cout << sizeof(edades) / sizeof(a) << endl;
    cout << sizeof(edades) / sizeof(edades[0]) << endl;
}