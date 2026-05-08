// DESAFIO FINAL
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA SENHA
// E ENTÃO MOSTRE NA TELA(CONSOLE.LOG) SE ESSA SENHA É:
// FRACA - 1 OU 2 REQUISITOS
// MEDIO - 3 OU 4 REQUISITOS
// FORTE - 5 REQUISITOS

// REQUISITOS:
// [ ] PELO MENOS 8 CARACTERES
// [ ] PELO MENOS 1 LETRA MAISCULA
// [ ] PELO MENOS 1 LETRA MINUSCULA
// [ ] PELO MENOS 1 NÚMERO
// [ ] PELO MENOS 1 CARACTER ESPECIAL

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

// RESOLUÇÃO COM BOAS PRÁTICAS
// let forca = ""

// if(qtde_requisitos_cumpridos <= 2){
//     forca = "FRACA"
// }else if(qtde_requisitos_cumpridos <= 4){
//     forca = "MÉDIA"
// }else{
//     forca = "FORTE"
// }

// console.log(`
//         Senha: ${senha}
//         Força: ${forca}
//         Quantidade de Requisitos Cumpridos: ${qtde_requisitos_cumpridos}
//         `)