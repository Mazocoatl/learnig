//El scope es el alcance que tiene una variable dentro de un bloque de codigo
// Ejemplo:
var nombre = 'Juan';
function imprimirNombreEnMayusculas(nombre) {
     nombre = nombre.toUpperCase();
     console.log(nombre);
}
imprimirNombreEnMayusculas(nombre);
JUAN

// Ejemplo:
var mNombre = 'Jair';
var nick = "Mazocoatl";
function nombre(){
    var lNombre = "Varela";
    console.log(mNombre + " " + nick + " " + lNombre);
}

nombre();
Jair Mazocoatl Varela