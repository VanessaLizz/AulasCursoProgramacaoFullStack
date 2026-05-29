// ATIVIDADE 1 - CONDICIONAIS
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR O SEU PESO E SUA ALTURA, CALCULE O SEU IMC E ENTÃO MOSTRE NO CONSOLE.LOG() SEU RESULTADO, SENDO:
// ABAIXO DE 18.5 -> ABAIXO DO PESO
// ENTRE 18.5 E 24.9 -> PESO NORMAL
// ENTRE 25 E 29.9 -> ACIMA DO PESO
// ENTRE 30 E 34.9 -> OBESIDADE I
// ENTRE 35 E 39.9 -> OBESIDADE II
// DE 40 PRA CIMA -> OBESIDADE III

function calcularIMC(){
  const peso = Number(prompt("Digite o seu peso: "))
  const altura = Number(prompt("Digite a sua altura: "))
  const imc = peso / altura**2
  if (imc < 18.5){
    console.log(`Seu IMC é: 18.5. Você está abaixo do peso.`)
  } else if (imc <= 24.9){
    console.log(`Seu IMC é: ${imc.toFixed(2)}. Seu peso está normal!`)
  }else if (imc <= 29.9){
    console.log(`Seu IMC é: ${imc.toFixed(2)}. Você está acima do peso.`)
  }else if (imc <= 34.9){
    console.log(`Seu IMC é: ${imc.toFixed(2)}. Você está com obesidade I.`)
  }else if (imc <= 39.9){
    console.log(`Seu IMC é: ${imc.toFixed(2)}. Você está com obesidade II.`)
  } else{
    console.log(`Seu IMC é: ${imc.toFixed(2)}. Você está com obesidade III.`)
  }
}
calcularIMC()

// CORREÇÃO OTIMIZADA
const peso = Number(prompt("Digite seu peso: "))
const altura = Number(prompt("Digite sua altura: "))
const imc = peso / altura ** 2
let condicao = ""

if (imc < 18.5){
    condicao = 'Abaixo do peso'
}else if(imc <= 24.9){
    condicao = 'Peso Normal'
}else if(imc <= 29.9){
    condicao = 'Acima do peso'
}else if(imc <= 34.9){
    condicao = 'Obesidade I'
}else if(imc <= 39.9){
    condicao = 'Obesidade II'
}else{
    condicao = 'Obesidade III'
}

console.log(`Você está ${condicao} e seu imc é ${imc.toFixed(2)}`)


// ATIVIDADE 2 - LOOP DE REPETIÇÃO
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR A IDADE DE 6 PESSOAS
// CALCULE A MÉDIA DAS IDADES
// E MOSTRE NA TELA SE A MÉDIA DAS IDADES É:
// - INFANTIL (SE A MÉDIA FOR MENOR QUE 12)
// - JOVEM (SE A MÉDIA FOR ENTRE 13 E 19)
// - ADULTO (SE A MÉDIA FOR ENTRE 20 E 50)
// - VEI (SE A MÉDIA FOR ENTRE 51 E 69)
// - CAINDO OS PEDAÇO ( SE FOR DE 70 PRA CIMA)

let soma = 0
for(let i = 1; i<=6; i++){
    const idade = Number(prompt("Digite uma idade: "))
    soma += idade
}
const media = soma / 6
let condicao = ""
if(media < 12){
    condicao = 'Infantil'
}else if(media <= 19){
    condicao = 'Jovem'
}else if(media <= 50){
    condicao = 'Adulto'
}else if(media <= 69){
    condicao = 'Vei'
}else{
    condicao = 'Caindo os Pedaço'
}

console.log(`A média das idades é ${media.toFixed(2)} o publico é ${condicao}`)


// INTRO DE DOM
const meu_p = document.getElementById("teste")
const agora = new Date()
const hora_atual = agora.getHours()

if(hora_atual >= 8 && hora_atual <= 17){
    meu_p.textContent = "A loja está aberta"
    meu_p.className = 'open'
}else{
    meu_p.textContent = "A loja está fechada"
    meu_p.className = 'close'
}
