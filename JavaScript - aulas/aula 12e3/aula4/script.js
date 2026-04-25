const senha = prompt("Digite sua senha: ")
let qtde_requisitos_cumpridos = 0
const minusculas = "abcdefghijklmnopqrstuvxwyzçâãàáèéêóôõíú"
const maisculas = minusculas.toUpperCase()
const numeros = '0123456789'
let tem_8_caracteres = 0
let tem_letras_minusculas = 0
let tem_letras_maiusculas = 0
let tem_numero = 0
let tem_caracter_especial = 0

if(senha.length >= 8){
    tem_8_caracteres = 1
}

for(let element of senha){
    if(minusculas.includes(element)){
        tem_letras_minusculas = 1
    }else if (maisculas.includes(element)){
        tem_letras_maiusculas = 1
    }else if(numeros.includes(element)){
        tem_numero = 1
    }else{
        tem_caracter_especial = 1
    }
}

qtde_requisitos_cumpridos = tem_8_caracteres + tem_caracter_especial + tem_letras_maiusculas + tem_letras_minusculas + tem_numero

if(qtde_requisitos_cumpridos <= 2){
    console.log("SENHA FRACA")
}else if(qtde_requisitos_cumpridos <= 4){
    console.log("SENHA MÉDIA")
}else{
    console.log("SENHA FORTE")
}