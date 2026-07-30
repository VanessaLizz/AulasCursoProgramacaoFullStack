import { Card } from "./components/Card";
import { pokemons } from "./mooks/pokemons";
import { Container, GlobalStyles } from "./utils/globalStyles";

function App() {
  return (
    <>
      <GlobalStyles />
      <h1>Projeto Pokemon</h1>
      <Container>
        {pokemons && pokemons.map((e) => <Card pokemon={e} />)}
      </Container>
    </>
  );
}

export default App;