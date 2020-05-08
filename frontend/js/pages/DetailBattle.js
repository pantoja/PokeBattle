import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import party from '../../image/party-popper.png';
import { setBattle } from '../actions/setBattle';
import PokemonCard from '../components/PokemonCard';
import TrainersInBattle from '../components/TrainersInBattle';

const StyledTitle = styled.span`
  font-weight: 600;
`;

const StyledContainer = styled.div`
  margin-top: 30px;
`;

const StyledRoundContainer = styled.div`
  display: flex;
  justify-content: space-evenly;
  margin: 40px;
`;
const StyledVersus = styled.span`
  font-weight: 700;
  align-self: center;
`;
const StyledIcon = styled.img`
  width: 30px;
  padding-left: 5px;
`;

class DetailBattle extends Component {
  componentDidMount() {
    const { setBattle, match, battles } = this.props;
    const { id } = match.params;
    if (battles === undefined) {
      setBattle(id);
    }
  }

  render() {
    const { battle, session } = this.props;
    if (!battle) return <>Loading</>;

    const { id, creator, opponent, winner } = battle;
    return (
      <>
        <h1>Battle nº {id}</h1>
        <div>
          <p>
            <StyledTitle>Players: </StyledTitle>
            <TrainersInBattle creator={creator.trainer} opponent={opponent.trainer} />
          </p>

          <p>
            <StyledTitle>Winner: </StyledTitle>
            {winner || '?'}
            {winner === session.email && <StyledIcon alt="winner" src={party} />}
          </p>
          <StyledContainer>
            {creator.team.map((pokemon, index) => (
              <div key={pokemon}>
                <StyledTitle>Round {index + 1}</StyledTitle>
                <StyledRoundContainer>
                  <PokemonCard pokemon={pokemon} trainer={creator.trainer} />
                  <StyledVersus>VS</StyledVersus>
                  <PokemonCard
                    pokemon={opponent.team ? opponent.team[index] : undefined}
                    trainer={opponent.trainer}
                  />
                </StyledRoundContainer>
              </div>
            ))}
          </StyledContainer>
        </div>
      </>
    );
  }
}

DetailBattle.propTypes = {
  battles: PropTypes.object,
  battle: PropTypes.object,
  setBattle: PropTypes.func,
  match: PropTypes.object,
  session: PropTypes.object,
};

const mapStateToProps = (state, { match }) => {
  const { id } = match.params;
  if (state.battles.battles) {
    return {
      battle: state.battles.battles[id],
      session: state.session,
    };
  }
  return {
    session: state.session,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    setBattle: (battle) => dispatch(setBattle(battle)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(DetailBattle);
