// AULA 08: OBJETOS LITERAIS

const pessoa = {
    nome: 'João',
    idade: 30,
    altura: 1.60,
    habilitado: false,
}
console.log(pessoa.nome)
console.log(pessoa)

// LISTA DE OBJETOS COM MÉDIA FILTRADA

const alunos = [
    { nome: 'João', nota: 8.5, serie: '1° ano' },
    { nome: 'Maria', nota: 9.2, serie: '1° ano' },
    { nome: 'Pedro', nota: 7.8, serie: '2° ano' },
    { nome: 'Ana', nota: 8.9, serie: '2° ano' },
    { nome: 'Lucas', nota: 6.5, serie: '3° ano' },
    { nome: 'Juliana', nota: 9.5, serie: '3° ano' },
    { nome: 'Carlos', nota: 7.0, serie: '1° ano' },
    { nome: 'Fernanda', nota: 8.3, serie: '2° ano' },
    { nome: 'Rafael', nota: 6.8, serie: '3° ano' },
    { nome: 'Beatriz', nota: 9.0, serie: '1° ano' }
];

const lista_1_ano = []
for(let element of alunos){
    if(element.serie === '1° ano'){
        lista_1_ano.push(element)
    }
}
let soma_1_ano = 0
for(let element of lista_1_ano){
    soma_1_ano += element.nota
}

const media_do_1_ano = soma_1_ano / lista_1_ano.length

// ---
// VERSÃO REDUZIDA

const alunos = [
    { nome: 'João', nota: 8.5, serie: '1° ano' },
    { nome: 'Maria', nota: 9.2, serie: '1° ano' },
    { nome: 'Pedro', nota: 7.8, serie: '2° ano' },
    { nome: 'Ana', nota: 8.9, serie: '2° ano' },
    { nome: 'Lucas', nota: 6.5, serie: '3° ano' },
    { nome: 'Juliana', nota: 9.5, serie: '3° ano' },
    { nome: 'Carlos', nota: 7.0, serie: '1° ano' },
    { nome: 'Fernanda', nota: 8.3, serie: '2° ano' },
    { nome: 'Rafael', nota: 6.8, serie: '3° ano' },
    { nome: 'Beatriz', nota: 9.0, serie: '1° ano' }
];

const lista_1_ano = []
let soma_1_ano = 0
for(let element of alunos){
    if(element.serie === '1° ano'){
        soma_1_ano += element.nota
        lista_1_ano.push(element)
    }
}
const media_do_1_ano = soma_1_ano / lista_1_ano.length

// ---

// ATIVIDADE DE OBJETOS
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO CADASTRAR 4 PRODUTOS for(let i=1; i<=4; i++)
// CADA PRODUTO DEVE TER: NOME, PREÇO, QTDE_ESTOQUE
// ADICIONE TUDO EM UM OBJETO
// ADICIONE O OBJETO NA LISTA

// PERCORRA A LISTA E CALCULE A MÉDIA DE PREÇO DOS PRODUTOS.
// meu código:

const produtos = []

for (let i = 1; i <= 4; i++){
  const produtos_nome = prompt("Digite o nome: ")
  const produtos_preco = Number(prompt("Digite o preço: "))
  const produtos_qtde = Number(prompt("Digite a quantidade: "))
  const produto_final = {
    nome: produtos_nome,
    preco: produtos_preco,
    quantidade: produtos_qtde
  }
  produtos.push(produto_final)
}

let soma = 0
for (let element of produto_final){
  soma += element.produtos_preco
}

const media = soma / produto_final.length
console.log(media)
const lista_produtos = []

for(let i=1; i<=4; i++){
    const nome_produto = prompt("Digite o nome do produto: ")
    const preco_produto = Number(prompt("Digite o preço do produto: "))
    const qtde_produto = Number(prompt("Digite a quantidade de estoque do produto: "))

    const novo_produto = {
        nome: nome_produto,
        preco: preco_produto,
        qtde: qtde_produto
    }
    lista_produtos.push(novo_produto)
    console.log("Produto cadastrado com sucesso.")
}

let soma_precos = 0
for (let element of lista_produtos){
    soma_precos += element.preco
}

const media = soma_precos / lista_produtos.length

console.log(`A média do preço dos produtos é: ${media.toFixed(2)}`)

// ---

// DESAFIO FINAL
// FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO CADASTRAR 6 FILMES
// CADA FILME CONTENDO: TÍTULO, GENERO, DURAÇÃO, PRECO_ALUGUEL

// PERCORRA A LISTA DE FILMES E:
// [ ] O FILME MAIS CARO
// [ ] O FILME MAIS CURTO
// [ ] A MÉDIA DE DURAÇÃO DOS FILMES
// [ ] A MÉDIA DO PREÇO DOS FILMES
// [ ] QUAL É O FILME MAIS BARATO DO GÊNERO TERROR
// [ ] QUAL É O FILME MAIS LONGO DO GÊNERO AÇÃO


const lista_filmes = [
  {
    titulo: "Interestelar",
    genero: "Ficção Científica",
    duracao: 169,
    preco: 12.9
  },
  {
    titulo: "O Poderoso Chefão",
    genero: "Drama",
    duracao: 175,
    preco: 9.9
  },
  {
    titulo: "Vingadores: Ultimato",
    genero: "Ação",
    duracao: 181,
    preco: 14.5
  },
  {
    titulo: "Toy Story",
    genero: "Animação",
    duracao: 81,
    preco: 7.5
  },
  {
    titulo: "Parasita",
    genero: "Suspense",
    duracao: 132,
    preco: 11.0
  },
    {
    titulo: "Invocação do Mal",
    genero: "Terror",
    duracao: 112,
    preco: 10.5
  },
  {
    titulo: "Hereditário",
    genero: "Terror",
    duracao: 127,
    preco: 13.0
  },
  {
    titulo: "La La Land",
    genero: "Musical",
    duracao: 128,
    preco: 8.9
  },
  {
    titulo: "Mad Max: Estrada da Fúria",
    genero: "Ação",
    duracao: 120,
    preco: 11.9
  },
  {
    titulo: "Clube da Luta",
    genero: "Drama",
    duracao: 139,
    preco: 9.5
  }
];

for(let i = 1; i<=6 ; i++){
    const titulo = prompt("Digite o título do filme: ")
    const genero = prompt("Digite o gênero do filme: ")
    const duracao = Number(prompt("Digite o duração (minutos) do filme: "))
    const preco = Number(prompt("Digite o preço do aluguel do filme: "))
    
    const novo_filme = {
        titulo: titulo,
        genero: genero,
        duracao: duracao,
        preco: preco
    }
    lista_filmes.push(novo_filme)
    alert('Filme cadastrado com sucesso.')
}

//------------------------------------------------------------------------------//
let mais_caro = lista_filmes[0]
for (let element of lista_filmes){
    if(element.preco > mais_caro.preco){
        mais_caro = element
    }
}
console.log(`O filme mais caro é ${mais_caro.titulo} custando R$ ${mais_caro.preco}`)
//------------------------------------------------------------------------------//



//------------------------------------------------------------------------------//
let mais_curto = lista_filmes[0]
for (let element of lista_filmes){
    if(element.duracao < mais_curto.duracao){
        mais_curto = element
    }
}
console.log(`O filme mais curto é ${mais_curto.titulo} durando ${mais_curto.duracao} minutos`)
//------------------------------------------------------------------------------//



//------------------------------------------------------------------------------//
let soma_duracao = 0
for(let element of lista_filmes){
    soma_duracao += element.duracao
}
const media_duracao = soma_duracao / lista_filmes.length

console.log(`A média de duração dos filmes é de ${media_duracao.toFixed(2)}`)
//------------------------------------------------------------------------------//



//------------------------------------------------------------------------------//
let soma_preco = 0
for(let element of lista_filmes){
    soma_preco += element.preco
}
const media_preco = soma_preco / lista_filmes.length

console.log(`A média de preço do aluguel dos filmes é de ${media_preco.toFixed(2)}`)
//------------------------------------------------------------------------------//




//------------------------------------------------------------------------------//
const filmes_terror = []
for(let element of lista_filmes){
    if(element.genero === 'Terror'){
        filmes_terror.push(element)
    }
}
let mais_barato_terror = filmes_terror[0]
for(let element of filmes_terror){
    if (element.preco < mais_barato_terror.preco){
        mais_barato_terror = element
    }
}
console.log(`O filme mais barato de terror é ${mais_barato_terror.titulo} custando R$ ${mais_barato_terror.preco}`)
//------------------------------------------------------------------------------//



//------------------------------------------------------------------------------//
const filmes_acao = []
for(let element of lista_filmes){
    if(element.genero === 'Ação'){
        filmes_acao.push(element)
    }
}
let mais_longo_acao = filmes_acao[0]
for(let element of filmes_acao){
    if (element.duracao > mais_longo_acao.duracao){
        mais_longo_acao = element
    }
}
console.log(`O filme mais longo de ação é ${mais_longo_acao.titulo} durando ${mais_longo_acao.duracao} minutos`)
//------------------------------------------------------------------------------//