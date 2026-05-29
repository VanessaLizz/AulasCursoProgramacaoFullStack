const salario = document.querySelector("#salario") // INPUT
const formulario = document.querySelector("#formulario") // FORM
const meus_salarios = document.querySelector("#meus_salarios") // UL

formulario.addEventListener("submit", (event) => {
    event.preventDefault()
    const novo_item = document.createElement('li')
    novo_item.textContent = `R$ ${salario.value}`
    if(Number(salario.value) > 1600){
        novo_item.style.color = 'green'
    }else{
        novo_item.style.color = 'red'
    }
    meus_salarios.appendChild(novo_item)
    formulario.reset()
})