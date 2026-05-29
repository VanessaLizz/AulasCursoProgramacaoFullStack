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

// EXEMPLO DE FOREACH
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


const salarios_do_banco = [1598.75, 2500, 6799.99, 800, 600, 1000]

salarios_do_banco.forEach((element)=>{ // for que vai dar 6 voltas.
    const novo_item = document.createElement('li')
    novo_item.textContent = `R$ ${element}`
    if(element > 1600){
        novo_item.style.color = 'green'
    }else{
        novo_item.style.color = 'red'
    }
    meus_salarios.appendChild(novo_item)
})

// KEYDOWN
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
    salario.value = ""
    salario.focus()
})


salario.addEventListener("keydown", (event)=>{
    if(event.key === 'Enter'){
        const novo_item = document.createElement('li')
        novo_item.textContent = `R$ ${salario.value}`
        if(Number(salario.value) > 1600){
            novo_item.style.color = 'green'
        }else{
            novo_item.style.color = 'red'
        }
        meus_salarios.appendChild(novo_item)
        salario.value = ""
        salario.focus()
    }
})