#include    <iostream>
using namespace std;
int main(){
    int edad = 0;
    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Su edad es: " << edad << endl;
    if(edad < 18){
        cout << "Es menor de edad" << endl;
    }else if (edad >= 60){
        cout << "Es de la tercera edad" << endl;
    }else{
        cout << "Es mayor de edad" << endl;
    }
}