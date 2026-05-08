// FUNÇÕES

function cumprimentar(nome){
    return `Olá ${nome}`
}

console.log(cumprimentar('abel'))
console.log(cumprimentar('maria'))
console.log(cumprimentar('joao'))

// VARIOS PARÂMETROS E CONDICIONAIS

function cumprimentar(hora, nome){
    if(hora >= 5 && hora <= 12){
        return `Bom dia ${nome}`
    }else if(hora >=13 && hora <= 18){
        return `Boa tarde ${nome}`
    }else{
        return `Boa noite ${nome}`
    }
}

console.log(cumprimentar(16, 'abel'))
console.log(cumprimentar(9, 'maria'))
console.log(cumprimentar(21, 'joao'))

// ATIVIDADE 1
// FAÇA UMA FUNÇÃO QUE RECEBE NO PARÂMETRO A IDADE E O NOME DE UMA PESSOA
// E ENTÃO RETORNE O DIREITO DE VOTO DESSA PESSOA
// CONSIDERANDO:
// - ABAIXO DE 16 NÃO PODE VOTAR
// - ENTRE 16 E 17 E ACIMA DE 70 O VOTO É FACULTATIVO
// - ENTRE 18 E 69 O VOTO É OBRIGATÓRIO
// TESTE NO CONSOLE PELO MENOS 2 VEZES.

function verificar_idade(idade, nome){
  if (idade < 16){
    return `${nome}, você não pode votar`
  } else if (idade <= 17 || idade > 70){
    return `${nome}, seu voto é facultativo`
  } else {
    return `${nome}, seu voto é obrigatório`
  }
}

console.log(verificar_idade(14, 'Ana'))
console.log(verificar_idade(75, 'Maria'))
console.log(verificar_idade(47, 'João'))

// ARROW FUNCTION - utilizar apenas se não for usar a função depois

function cumprimentar(nome){
    return `Olá ${nome}`
}

// 1º PASSO - É TIRAR O NOME DA FUNÇÃO
function(nome){
    return `Olá ${nome}`
}

// 2º PASSO - É COLOCAR A SETA (A FLECHA) DEPOIS DO PARÂMENTO
function (nome) => {
    return `Olá ${nome}`
}

// 3º PASSO - TIRAR A PALAVRA 'FUNCTION'
(nome) => {
    return `Olá ${nome}`
}

// REGRAS OPCIONAIS

// 4º PASSO - SE SÓ TIVER UMA LINHA NÃO PRECISA DA PALAVRA 'RETURN'
(nome) => {
    `Olá ${nome}`
}

// 5º PASSO - SE NÃO TIVER ESCRITO O RETURN NÃO PRECISA DAS CHAVES
(nome) => `Olá ${nome}`


// 6º PASSO - SE SÓ TIVER 1 PARÂMETRO NÃO PRECISA DOS PARÊNTESES
nome => `Olá ${nome}`
FILTER
// for (let element of idades){
    //     if(element >= 18){
        //         maiores_idade.push(element)
        //     }
        // }
        // console.log(idades)
        // console.log(maiores_idade)
        
        
// MÉTODOS AVANÇADOS DE ARRAYS
// const maiores_idade = []
// function filtrarIdades(lista_idades){
//     const maiores_de_idade = []
//     for(let element of lista_idades){
//         if (element >= 18){
//             maiores_de_idade.push(element)
//         }
//     }
//     return maiores_de_idade
// }

const idades = [30, 58, 16, 21, 14, 8, 60, 18]
const maiores = idades.filter(e => e >= 18)
console.log(idades)
console.log(maiores)