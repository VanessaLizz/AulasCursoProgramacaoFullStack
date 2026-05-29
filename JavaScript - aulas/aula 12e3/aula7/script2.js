const botao = document.querySelector("#botao")

botao.addEventListener("click", ()=>{
    console.log("Clicaram em mim")
})

botao.addEventListener("dblclick", ()=>{
    console.log("Duplo clique aconteceu")
})

botao.addEventListener("mouseover", ()=>{
    console.log("O mouse ENTROU")
})

botao.addEventListener("mouseout", ()=>{
    console.log("O mouse saiu")
})

// EVENTOS DE TECLADO
const caixinha = document.querySelector("#caixinha")

// caixinha.addEventListener("keydown", (event)=>{
//     console.log(event.key)
// })

// caixinha.addEventListener("keyup", (event)=>{
//     console.log(event.key)
// })

caixinha.addEventListener("change", (event)=>{
    console.log(event.target.value)
})


caixinha.addEventListener("input", (event)=>{
    console.log(event.target.value)
})