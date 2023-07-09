// Operadores de Asignación
// // Asignación
var a = 1;
// // Asignación de adición
a += 3; // a = a + 3
// // Asignación de sustracción
a -= 2; // a = a - 2
// // Asignación de multiplicación
a *= 2; // a = a * 2
// // Asignación de división
a /= 2; // a = a / 2
// // Asignación de módulo
a %= 2; // a = a % 2
// // Asignación de exponenciación
a **= 2; // a = a ** 2

// Operadores de Comparación
// // Igualdad
3 == "3"; // true
// // Igualdad estricta
3 === "3"; // false
// // Desigualdad
3 != "3"; // false
// // Desigualdad estricta
3 !== "3"; // true
// // Mayor que
3 > 2; // true
// // Mayor o igual que
3 >= 2; // true
// // Menor que
3 < 2; // false
// // Menor o igual que
3 <= 2; // false
// // Operador ternario
var a = 3;
var b = 2;
var c = a > b ? "a es mayor que b" : "a no es mayor que b";

// Operadores Lógicos
// // AND
true && true; // true
true && false; // false
false && true; // false
false && false; // false
// // OR
true || true; // true
true || false; // true
false || true; // true
false || false; // false
// // NOT
!true; // false
!false; // true

// Operadores de Cadena
// // Concatenación
"Hello" + " " + "World"; // "Hello World"
// // Comparación
"z" > "a"; // true
"Hello" > "World"; // false (porque H es mayor que W)
// // Asignación de adición
var a = "Hello";
a += " World"; // "Hello World" (porque += es un operador de asignación)

// Operadores de Tipo
// // typeof
typeof 123; // "number"
typeof "123"; // "string"
typeof true; // "boolean"
typeof undefined; // "undefined"
typeof null; // "object"
typeof Symbol(); // "symbol"
typeof {}; // "object"
typeof []; // "object"
typeof function() {}; // "function"

// Operadores Bit a Bit
// // AND
3 & 2; // 2 (porque 3 = 11 en binario, y 2 = 10 en binario, y 11 & 10 = 10, y 10 en binario es 2 en decimal) 
// // OR
3 | 2; // 3 (porque 3 = 11 en binario, y 2 = 10 en binario, y 11 | 10 = 11, y 11 en binario es 3 en decimal)
// // XOR
3 ^ 2; // 1 (porque 3 | 2 = 3, y 3 & 2 = 2, y 3 ^ 2 = 3 ^ 2)
// // NOT
~3; // -4 (porque -(3 + 1) = -4)
// // Desplazamiento a la izquierda
3 << 2; // 12 (porque 3 = 11 en binario, y 11 << 2 = 1100, y 1100 en binario es 12 en decimal)
// // Desplazamiento a la derecha
3 >> 2; // 0 (porque 3 = 11 en binario, y 11 >> 2 = 0, y 0 en binario es 0 en decimal)
// // Desplazamiento a la derecha sin signo
3 >>> 2; // 0 (porque 3 = 11 en binario, y 11 >>> 2 = 0, y 0 en binario es 0 en decimal)

// Operadores de Igualdad
// // Igualdad
3 == "3"; // true

// Operadores Aritméticos
// // Suma
3 + 2; // 5
// // Resta
3 - 2; // 1
// // Multiplicación
3 * 2; // 6
// // División
3 / 2; // 1.5
// // Módulo
3 % 2; // 1 (porque 3 / 2 = 1.5, y 1.5 - 1 = 0.5, y 0.5 * 2 = 1)
// // Exponenciación
3 ** 2; // 9

// Operadores de Incremento y Decremento
// // Incremento
var a = 3;
a++; // 4
// // Decremento
var a = 3;
a--; // 2

var a = 3;
a += 1; // 4
a -= 1; // 3

// Operadores de Negación
// // Negación
var a = 3;
-a; // -3

// Operadores de Agrupación
// // Agrupación
(3 + 2) * 2; // 10
