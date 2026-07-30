import styled from "styled-components";
// REGRA DE OUTRO DO REACT TODOOOOOOOOOOOOOOOOOOOOOOOOOOOS OS COMPONENTS COMEÇAM COM LETRA MAIUSCULA.
export const CardStyle = styled.div`
  border: 1px solid #1f1f1f;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: ${({ $fundo }) => $fundo};
  gap: 10px;
  border-radius: 8px;
  padding: 10px;
  h2{
    font-weight: bold;
    font-size: 24px;
    letter-spacing: 4px;
  }
  p{
    font-size: 16px;
    font-style: italic;
  }
  img{
    max-width: 250px;
  }
`;