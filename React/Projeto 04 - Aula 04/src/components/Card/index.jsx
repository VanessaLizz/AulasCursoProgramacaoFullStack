import { CardStyle } from "./style";

export const Card = ({pokemon}) => {
  return (
    <>
      <CardStyle $fundo={pokemon.cor}>
        <h2>{pokemon.nome}</h2>
        <img src={pokemon.foto} />
        <p>Tipo: {pokemon.tipo}</p>
      </CardStyle>
    </>
  );
};