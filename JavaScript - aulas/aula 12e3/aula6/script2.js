const nome = document.querySelector("#nome")
const cadastrar = document.querySelector("#cadastrar")
const lista_alunos = document.querySelector("#lista_alunos")

cadastrar.addEventListener("click", ()=>{
    const novo_item = document.createElement("li")
    novo_item.textContent = nome.value
    lista_alunos.append(novo_item)
    nome.value = ""
    nome.focus()
})


const lista_infinity = ['Thais', 'Bia', 'Lazaro', 'Luis']
const banco_de_vdd = document.querySelector("#banco_de_vdd")

banco_de_vdd.addEventListener("click", ()=>{
    for(let element of lista_infinity){
        const novo_li = document.createElement("li")
        novo_li.textContent = element
        lista_alunos.append(novo_li)
    }
})

// ATIVIDADE FINAL
// FAÇA UM SITE QUE PEDE PARA O USUÁRIO CADASTRAR SEU SALÁRIO
// ADICIONE ESSES SALÁRIO EM UMA LISTA (UL) DO HTML
// SE FOR ACIMA DO SALÁRIO MINIMO, O SALARIO APARECE DA COR VERDE
// SE NÃO, DA COR VERMELHO.