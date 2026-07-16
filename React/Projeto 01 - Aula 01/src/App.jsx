import './App.css'
import { pokemons } from './mocks/poke'


function App() {
  const agora = new Date()
  const hora_atual = agora.getHours()
    return (
      <>  
        <h1>Lista de Pokemons</h1>
        {pokemons.map(e =>(
            <div>
              <h2>{e.nome}</h2>
              <img src={e.imagem} alt={`Foto do pokemon ${e.nome}`} />
              <p>Tipo: {e.tipo}</p>
            </div>
          )
        )}
      </>
        
    )
}

export default App
