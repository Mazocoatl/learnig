// Que es coerción?
// Es el proceso de convertir un valor de un tipo a otro

// Coerción implícita
// Es cuando el lenguaje nos ayuda a convertir un valor de un tipo a otro

// Ejemplo:
var a = 4 + "7";
console.log(a);
console.log(typeof a);

47
string

// Ejemplo:
var a = 4 * "7";
console.log(a);
console.log(typeof a);

28
number

// Coerción explícita
// Es cuando nosotros obligamos a un valor a convertirse a otro tipo

// Ejemplo:
var a = 20;
var b = a + "";
console.log(b);
console.log(typeof b);
var c = String(a);
console.log(c);
console.log(typeof c);
var d = Number(c);
console.log(d);
console.log(typeof d);

20
string
20
string
20
number
