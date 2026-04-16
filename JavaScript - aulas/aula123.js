//PRIMEIRO ENCONTRO DE JAVASCRIPT 

//AULA 01: VARIÁVEIS, OPERADORES E INCREMENTADOR

alert("Vamos começar a brincadeira!!!")

//LET é usado apenas para contadores (apenas para criar o primeiro), para os outros é usado CONST(não altera). Não usar VAR.

// VARIÁVEIS
String
Number
Boolean

const nome = 'joao'
const idade = 20
const altura = 1.60
const habilitado = true


// OPERADORES MATEMÁTICOS
const n1 = 5
const n2 = 8
alert(n1 + n2) // 13
alert(n1 - n2) // -3
alert(n1 * n2) // 40
alert(n1 / n2) // 0.625


// INCREMENTADORES
let contador = 1
contador += 1 // 2
contador += 4 // 6
contador -= 3 // 3
contador *= 5 // 15
contador /= 3 // 5

// ISSO AQUI AGORA, NAO TEM NO PY:
// CASO QUEIRA INCREMENTAR OU DECREMENTAR ESTRITAMENTE 1

contador++ // ADICIONA 1
contador-- // DIMINUI 1
alert(contador)



//AULA 02: CONDICIONAIS
//IF E ELSE | OPERADORES DE COMPARAÇÃO
const idade = 25

if (idade >= 18){
    alert(`Maior de idade: ${idade}`)
}else{
    alert(`Menor de idade: ${idade}`)
}

// OPERADORES DE COMPARAÇÃO
const n1 = 5
const n2 = 8
alert(n1 > n2) // false
alert(n1 >= n2) // false
alert(n1 < n2) // true
alert(n1 <= n2) // true
alert(n1 === n2) // false
alert(n1 !== n2) // true

//OPERADORES LÓGICOS | ELSE IF
const numero = 5

if(numero > 0){
    alert("Positivo")
}else if(numero < 0){
    alert("Negativo")
}else{
    alert("Neutro")
}


// OPERADORES LÓGICOS

const idade = 25

if (idade >= 18 && idade <= 70){
    alert("Voto obrigatório")
}else if (idade <18 || idade > 70){
    alert("Voto facultativo")
}


const habilitado = true

if(!habilitado){
    alert("Multado")
}


// && -> equivalente ao "and"
// || -> equivalente ao "or"
// ! -> equivalente ao "not"


//ENTRADA E SAÍDA

const nome = prompt("Digite seu nome: ")
// const idade = Number(prompt("Digite sua idade: "))

// alert(`Olá ${nome}`) ISSO AQUI PARECE VIRUS
console.log(`Olá ${nome}`) 

// document.writeln(`Olá ${nome}`) EVITE ESSE MERDA


//ESTUDA ISSO NAO BTL, SERVE PRA NADA - SWITCH CASE
const cor = prompt("Digite uma cor do semáforo: ")

switch (cor){
    case "vermelho":
        console.log("Pare")
        break
    case "amarelo":
        console.log("Atenção")
        break
    case "verde":
        console.log("Continue")
        break
    default:
        console.log("DIGITA DIREITO BTL")
        break
}

//IF TERNÁRIO
const idade = 25
idade >= 18 ? alert("maior") : alert("menor")

//  ? -> SUBSTITUI O 'IF'
//  : -> SUBSTITUI O 'ELSE'

//AULA 03: LOOPS DE REPETIÇÃO

//WHILE (INÚTIL)
let cont = 1
while (cont <= 10){
    console.log(cont)
    cont++
}

//FOR - TRADICIONAL
for (let i = 2 ; i<= 20 ; i++){
    console.log(i)
}

//FOR...OF
const nome = 'abel'

for (let element of nome){
    console.log(element)
}

//LENGTH
const nome = 'abel'

console.log(nome.length)

//INCLUDES
const nome = 'abel'
const vogais = 'aeiou'
let qtde_vogais = 0

for (let element of nome){
    if(vogais.includes(element)){
        qtde_vogais++
    }
}