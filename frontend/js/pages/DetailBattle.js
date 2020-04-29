import axios from 'axios';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import { getBattle } from '../actions';
import PokemonCard from '../components/PokemonCard';

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

class DetailBattle extends Component {
  componentDidMount() {
    const { getBattle } = this.props;
    // TODO: Will use pathname from props when I implement react-router-dom
    const { pathname } = window.location;
    const id = pathname.slice(pathname.lastIndexOf('/') + 1);
    axios.get(`/api/battle/${id}`).then((response) => {
      return getBattle(response.data);
    });
  }

  render() {
    const { battle, isLoading } = this.props;
    if (isLoading) {
      return <>Loading</>;
    }
    return (
      <>
        <h1>Battle nº {battle.id}</h1>
        <div>
          <p>
            <StyledTitle>Players: </StyledTitle>
            {battle.creatorTeam.trainer} <span>VS</span> {battle.opponentTeam.trainer}
          </p>

          <p>
            <StyledTitle>Winner: </StyledTitle>
            {battle.winner ? battle.winner : '?'}
          </p>
          <StyledContainer>
            {battle.creatorTeam.team.map((pokemon, index) => (
              <div key={pokemon.id}>
                <StyledTitle>Round {index + 1}</StyledTitle>
                <StyledRoundContainer>
                  <PokemonCard pokemon={pokemon} trainer={battle.creatorTeam.trainer} />
                  <StyledVersus>VS</StyledVersus>
                  <PokemonCard
                    pokemon={battle.winner ? battle.opponentTeam.team[index] : undefined}
                    trainer={battle.opponentTeam.trainer}
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
  isLoading: PropTypes.bool,
  getBattle: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battle: state.battles.battle,
  isLoading: state.battles.isLoading,
});

const mapDispatchToProps = (dispatch) => {
  return {
    getBattle: (battle) => dispatch(getBattle(battle)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(DetailBattle);
