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