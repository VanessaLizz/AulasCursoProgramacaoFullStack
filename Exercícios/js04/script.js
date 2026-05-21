// MANIPULAÇÃO DE DOM

// GETELEMENTSBYTAGNAME( )
const todos_h1 = document.getElementsByTagName("h1")
const todos_h2 = document.getElementsByTagName("h2")
const todos_p = document.getElementsByTagName("p")
console.log(todos_h1)
console.log(todos_h2)
console.log(todos_p)

// GETELEMENTSBYCLASSNAME( )
const todos_eventos = document.getElementsByClassName("eventos")
console.log(todos_eventos)

// GETELEMENTBYID( ) 
const elemento = document.getElementById("elemento")
console.log(elemento)

// QUERYSELECTOR( )
const todos_h2 = document.querySelectorAll("h2")
const todos_eventos = document.querySelectorAll(".eventos") // utiliza . para class
const elemento = document.querySelector("#elemento")  // utiliza # para id

console.log(todos_h2)
console.log(todos_eventos)
console.log(elemento) 

// MANIPULANDO 1 ELEMENTO
const especial = document.querySelector("#especial")

console.log(especial)
console.log(especial.textContent)
console.log(especial.id)
especial.textContent = 'outra coisa'
console.log(especial.textContent)


// EVENTO DE CLICK

const diminuir = document.querySelector("#diminuir")
const numero = document.querySelector("#numero")
const aumentar = document.querySelector("#aumentar")
const resposta = document.querySelector("#resposta")

aumentar.addEventListener("click", ()=>{
    resposta.textContent = ""
    if(Number(numero.textContent) === 10){
        resposta.textContent = "Não é possível passar de 10"
    }else{
        numero.textContent = Number(numero.textContent) + 1
    }

})

diminuir.addEventListener("click", ()=>{
    if(Number(numero.textContent) === 0){
        resposta.textContent = 'Não é permitido números negativos'
    }else{
        numero.textContent = Number(numero.textContent) - 1
        resposta.textContent = ""
    }
})