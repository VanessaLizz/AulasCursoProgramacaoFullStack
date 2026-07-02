const resultados = document.querySelector("#resultados");

async function buscarFilmes() {
    try {
        const response = await fetch(
            "https://api.themoviedb.org/3/movie/popular?api_key=77c4e2b070a2e1396500d0b42ebf7cec&language=pt-BR"
        );

        const data = await response.json();
        const lista_de_filmes = data.results;

        resultados.innerHTML = "";

        lista_de_filmes.forEach((element) => {
            const novo_filme = document.createElement("div");

            const novo_titulo = document.createElement("h2");
            novo_titulo.textContent = element.title;

            const nova_imagem = document.createElement("img")
            nova_imagem.src = `https://image.tmdb.org/t/p/w500${element.poster_path}`

            const nova_nota = document.createElement("p");
            nova_nota.textContent = `⭐ Nota: ` + element.vote_average.toFixed(1);

            novo_filme.append(nova_imagem, novo_titulo, nova_nota);

            resultados.appendChild(novo_filme);
        });

    } catch (erro) {
        console.error(erro);
    }
}

buscarFilmes();