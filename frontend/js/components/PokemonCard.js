import PropTypes from 'prop-types';
import React from 'react';
import styled from 'styled-components';

const StyledCard = styled.div`
  width: 300px;
  text-align: center;
  border-radius: 10px;
  background-color: #ffffff;
  padding-bottom: 10px;
  box-shadow: 0px 0px 15px -13px $shadow-black;
`;

const StyledTrainer = styled.p`
  border-radius: 10px 10px 0 0;
  background-color: #8370cc;
  color: #ffffff;
  font-weight: 500;
  padding: 10px;
`;

const StyledName = styled.p`
  text-transform: capitalize;
`;

const StyledStats = styled.p`
  font-weight: 500;
`;

const StyledQuestionMark = styled.p`
  font-weight: 700;
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
`;

const PokemonCard = (props) => {
  const { pokemon, trainer } = props;
  return (
    <StyledCard>
      <StyledTrainer>{trainer} played:</StyledTrainer>
      {pokemon ? (
        <>
          <img alt={pokemon.name} src={pokemon.sprite} />
          <StyledName>{pokemon.name}</StyledName>
          <StyledStats>
            ATT: {pokemon.attack} DEF: {pokemon.defense} HP: {pokemon.hp}
          </StyledStats>
        </>
      ) : (
        <StyledQuestionMark>?</StyledQuestionMark>
      )}
    </StyledCard>
  );
};

PokemonCard.propTypes = {
  pokemon: PropTypes.object,
  trainer: PropTypes.string,
};

export default PokemonCard;
