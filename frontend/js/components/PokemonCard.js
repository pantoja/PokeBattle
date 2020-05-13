import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import { pokemonSelector, userSelector } from '../utils/selectors';

const Card = styled.div`
  width: 300px;
  text-align: center;
  border-radius: 10px;
  background-color: #ffffff;
  padding-bottom: 10px;
  box-shadow: 0px 0px 15px -13px $shadow-black;
`;

const Trainer = styled.p`
  border-radius: 10px 10px 0 0;
  background-color: #8370cc;
  color: #ffffff;
  font-weight: 500;
  padding: 10px;
`;

const Name = styled.p`
  text-transform: capitalize;
`;

const Stats = styled.p`
  font-weight: 500;
`;

const QuestionMark = styled.p`
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
    <Card>
      <Trainer>{trainer.email} played:</Trainer>
      {pokemon ? (
        <>
          <img alt={pokemon.name} src={pokemon.sprite} />
          <Name>{pokemon.name}</Name>
          <Stats>
            ATT: {pokemon.attack} DEF: {pokemon.defense} HP: {pokemon.hp}
          </Stats>
        </>
      ) : (
        <QuestionMark>?</QuestionMark>
      )}
    </Card>
  );
};

PokemonCard.propTypes = {
  pokemon: PropTypes.object,
  trainer: PropTypes.object,
};

const mapStateToProps = (state, { trainer, pokemon }) => ({
  pokemon: pokemonSelector(state, pokemon),
  trainer: userSelector(state, trainer),
});

export default connect(mapStateToProps)(PokemonCard);
