//hoisting es el comportamiento de javascript de mover las declaraciones al inicio del scope
//Ejemplo:
console.log(miNombre);
var miNombre = "Juan";

undefined

//Ejemplo:
var miNombre = undefined;
console.log(miNombre);
miNombre = "Juan";

undefined
"Juan"

//Ejemplo:
var miNombre = undefined;
console.log(miNombre + " soy un hoisting");
miNombre = "Juan";

undefined soy un hoisting
"Juan"

//Ejemplo:

hey();
function hey(){
    console.log("Hola " + miNombre);
}
var miNombre = "Juan";

Hola undefined
undefined