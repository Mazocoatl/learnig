#include    <iostream>
using namespace std;
int main(){
    int lista[] = {1,2,3};
    int limite = sizeof(lista)/sizeof(lista[0]);
   for (int i= 0; i<limite; i+=1)
      cout << lista[i] << endl;
}