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

