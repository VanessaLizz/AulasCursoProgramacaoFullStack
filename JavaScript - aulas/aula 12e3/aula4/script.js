// ATIVIDADE 1 
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SUA IDADE
// E MOSTRE NA TELA O DIREITO DE VOTO DELE
// OPÇOES:
// 1 - NÃO PODE VOTAR ( SE A IDADE FOR MENOR QUE 16)
// 2 - FACULTATIVO (SE A IDADE TIVER ENTRE 16 E 17 OU ACIMA DE 70)
// 3 - OBRIGATÓRIO (SE A IDADE ESTIVER ENTRE 18 E 69)

const idade = Number(prompt("Digite a sua idade: "))

if (idade < 16){
  console.log("Você não possui idade mínima para votar")
} else if(idade <=17 || idade > 70){
  console.log("Seu voto é facultativo")
} else{
  console.log("Seu voto é obrigatório")
}

// ATIVIDADE 2
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 5 IDADES (USANDO UM FOR)
// E ENTÃO NO FINAL DO FOR, MOSTRE NO CONSOLE A MÉDIA DAS IDADES.

let soma = 0

for (let i = 1; i<=5; i++){
  const idade = Number(prompt("Digite uma idade: "))
  soma += idade
}

const media = soma / 5
console.log(media)

// ARRAYS - LISTAS

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas[1])
console.log(frutas)
frutas[0] = 'Laranja'
console.log(frutas)
console.log(frutas.length)

// ADICIONA NO FINAL (PUSH É O APPEND DO JS)

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas)
frutas.push('Melancia')
console.log(frutas)

// REMOVE O ÚLTIMO

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas)
frutas.pop()
console.log(frutas)

// ADICIONA NO COMEÇO (É MERMO QUE BOSTA)

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas)
frutas.unshift('Melancia')
console.log(frutas)

// REMOVE O PRIMEIRO (MAIS BOSTA QUE ESSE DE CIMA)

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas)
frutas.shift()
console.log(frutas)

// ADICIONANDO EM UM LUGAR ESPECÍFICO (NINGUEM USA ISSO PRA NADA)

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas)
frutas.splice(1, 0, 'Laranja') // EQUIVALENTE AO INSERT DO PY
console.log(frutas)

// REMOVENDO O ITEM PELO NOME (INFELIZMENTE USAMOS MTO KKKK )
// ISSO EQUIVALE O REMOVE DO Py

const frutas = ['Uva', 'Morango', 'Acerola']
console.log(frutas)
const posicao_fruta = frutas.indexOf('Morango') // ISSO AQUI VAI BUSCAR A POSIÇÃO DO ITEM
frutas.splice(posicao_fruta, 1) // AI REMOVE O ITEM PELA POSIÇÃO ENCONTRADA.
console.log(frutas)
