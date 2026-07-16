import { useState } from "react";
import "./App.css";
import { url_desligada, url_ligada } from "./assets/mocks/lampadas";

function App() {
  const [lampada, setLampada] = useState(url_desligada)
  return (
    <>
        <h1>Programinha da Lâmpada</h1>
        <img src={lampada}/>
        <br />
        <button onClick={()=>setLampada(url_ligada)}>Ligar</button>
        <button onClick={()=>setLampada(url_desligada)}>Desligar</button>
    </>
  );
}

export default App;