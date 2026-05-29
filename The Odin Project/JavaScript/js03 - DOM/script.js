const container = document.querySelector("#container")

const content = document.createElement("div")
content.classList.add("content")
content.textContent = 'This is the glorious text-content!'

const paragrafo = document.createElement("p")
paragrafo.classList.add("paragrafo")
paragrafo.style.color = 'red'
paragrafo.textContent = 'Hey, I am red!'

const texto = document.createElement("h3")
texto.classList.add("texto")
texto.style.color = 'blue'
texto.textContent = 'I am a blue h3!'

const bloco = document.createElement("div")
bloco.classList.add("bloco")
bloco.style.border = '1px solid black'
bloco.style.backgroundColor = 'pink'
const textoBloco = document.createElement('h1')
textoBloco.textContent = 'I’m in a div'
const paragrafoBloco = document.createElement('p')
paragrafoBloco.textContent = 'Me too!'


container.append(content, paragrafo, texto, bloco)
bloco.append(textoBloco, paragrafoBloco)
