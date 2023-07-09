#include    <iostream>
using namespace std;
int suma (int a, int b){
    return a + b;
}
int multiplicacion (int a, int b){
    return a * b;
}
int main(){
    cout << "Que numeros quiere operar?" << endl;
    int a, b;
    cin >> a >> b;
    cout << suma (a, b) << endl;
    cout << multiplicacion (a, b) << endl;
}