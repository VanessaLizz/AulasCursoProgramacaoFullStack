import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios';

function App() {
  const [endereco, setEndereco] = useState();
  const [cep, setCEP] = useState("");
  const [error, setError] = useState("")
  
  async function buscarCEP() {
    try{
      const {data} = await axios.get(`https://viacep.com.br/ws/${cep}/json/`);
      if(data.erro){
        setError("CEP inexistente")
        setEndereco(undefined)
      }else {
        setEndereco(data);
        setError("")
      }
    } catch(err){
      console.log(err);
      setError("Digite o CEP corretamente!")
      setEndereco(undefined)
    }
  }

  return (
    <>
      <h1>Consulte seu CEP</h1>
      <form onSubmit={(e) => {
        e.preventDefault();
        buscarCEP();
      }}>

        <label htmlFor="cep">CEP</label>
        <input type="text" id="cep" name="cep" placeholder="xxxxx-xxx" maxLength={8} minLength={8} 
        required onChange={e => setCEP(e.target.value)} />
        <button>Pesquisar</button>

      </form>
      {endereco && ( //verificador de existencia - evolução do if - se tiver algum tipo de erro, a div ñ será criada
        <div>
        <h2>{endereco.logradouro}</h2>
        <p>Bairro: {endereco.bairro}</p>
        <p>Cidade: {endereco.localidade}</p>
        <p>Estado: {endereco.estado}</p>
      </div>
      )}

      {error && <p>{error}</p>}
    </>
  )
}

export default App
