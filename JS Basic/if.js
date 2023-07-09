// Condicional if es una sentencia que ejecuta un bloque de código si una condición es verdadera
if (true) {
    console.log('Hola mundo');
}
// Hola mundo

if (false) {
    console.log('Hola mundo');
}  
// No se ejecuta nada

// Condicional if con else
if (false) {
    console.log('Hola mundo');
} else {
    console.log('Adiós mundo');
}
// Adiós mundo

// Condicional if con else if
if (false) {
    console.log('Hola mundo');
} else if (true) {
    console.log('Adiós mundo');
} else {
    console.log('No se ejecuta nada');
}  
// Adiós mundo

var edad = 18;
if (edad === 18) {
    console.log('Puedes votar, será tu primera votación');
} else if (edad > 18) {
    console.log('Puedes votar de nuevo');
} else {
    console.log('Aún no puedes votar');
}
// Puedes votar, será tu primera votación

// Condicional if con operador ternario
condition ? true : false;
var numero = 1;
var resultado = numero === 1 ? 'Sí soy un uno' : 'No, no soy un uno';
console.log(resultado);
// Sí soy un uno

var numero = 2;
var resultado = numero === 1 ? 'Sí soy un uno' : 'No, no soy un uno';
console.log(resultado);
// No, no soy un uno