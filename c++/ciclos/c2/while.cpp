#include    <iostream>
using namespace std;
int main(){
    do {
         char respuesta;
         cout << "¿Desea continuar? (s/n): ";
         cin >> respuesta;
         if (respuesta == 'n'){
            cout << "Adios" << endl;
             break;
         }
    } while (true);
}