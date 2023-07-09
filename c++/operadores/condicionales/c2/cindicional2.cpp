#include    <iostream>
using namespace std;
int main(){
    int edad = 0;
    cout << "Ingrese su edad: ";
    cin >> edad;
    if (edad < 18 || edad > 60){
        cout << "No puedes votar" << endl;
    }else{
        cout << "Puedes Votar" << endl;
    }
}
