import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import party from '../../image/party-popper.png';
import { setBattle } from '../actions/setBattle';
import PokemonCard from '../components/PokemonCard';
import { getBattleAPI } from '../utils/services';

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
    const { setBattle, match } = this.props;
    const { id } = match.params;
    getBattleAPI(id).then((battleData) => {
      return setBattle(battleData);
    });
  }

  render() {
    const { battle, isLoading, user } = this.props;
    const { id, creator_team, opponent_team, winner } = battle;
    if (isLoading) return <>Loading</>;
    return (
      <>
        <h1>Battle nº {id}</h1>
        <div>
          <p>
            <StyledTitle>Players: </StyledTitle>
            {creator_team.trainer} <span>VS</span> {opponent_team.trainer}
          </p>

          <p>
            <StyledTitle>Winner: </StyledTitle>
            {winner || '?'}
            {winner === user.email && <StyledIcon alt="winner" src={party} />}
          </p>
          <StyledContainer>
            {creator_team.team.map((pokemon, index) => (
              <div key={pokemon.id}>
                <StyledTitle>Round {index + 1}</StyledTitle>
                <StyledRoundContainer>
                  <PokemonCard pokemon={pokemon} trainer={creator_team.trainer} />
                  <StyledVersus>VS</StyledVersus>
                  <PokemonCard
                    pokemon={winner ? opponent_team.team[index] : undefined}
                    trainer={opponent_team.trainer}
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
  battle: PropTypes.object,
  setBattle: PropTypes.func,
  isLoading: PropTypes.bool,
  match: PropTypes.object,
  user: PropTypes.object,
};

const mapStateToProps = (state) => ({
  battle: state.battles.battle,
  isLoading: state.battles.isLoading,
  user: state.user,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setBattle: (battle) => dispatch(setBattle(battle)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(DetailBattle);
