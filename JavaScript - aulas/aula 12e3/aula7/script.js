const salario = document.querySelector("#salario") // INPUT
const analisar = document.querySelector("#analisar") // BUTTON
const meus_salarios = document.querySelector("#meus_salarios") // UL

analisar.addEventListener("click", () => {
    const novo_item = document.createElement('li')
    novo_item.textContent = `R$ ${salario.value}`
    if(Number(salario.value) > 1600){
        novo_item.style.color = 'green'
    }else{
        novo_item.style.color = 'red'
    }
    meus_salarios.appendChild(novo_item)
})

