import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import party from '../../image/party-popper.png';
import { fetchBattle } from '../actions/setBattle';
import PokemonCard from '../components/PokemonCard';
import TrainersInBattle from '../components/TrainersInBattle';
import { selectUserInSession, selectBattleById } from '../utils/selectors';

const Title = styled.span`
  font-weight: 600;
`;

const Container = styled.div`
  margin-top: 30px;
`;

const RoundContainer = styled.div`
  display: flex;
  justify-content: space-evenly;
  margin: 40px;
`;
const VSTag = styled.span`
  font-weight: 700;
  align-self: center;
`;
const Icon = styled.img`
  width: 30px;
  padding-left: 5px;
`;

class DetailBattle extends Component {
  componentDidMount() {
    const { fetchBattle, match, battle } = this.props;
    const { id } = match.params;
    if (!battle) {
      return fetchBattle(id);
    }
    return null;
  }

  render() {
    const { session, battle } = this.props;
    const { match } = this.props;
    const { id } = match.params;

    if (!battle) return <>Loading</>;

    const { creator, opponent, winner } = battle;
    return (
      <>
        <h1>Battle nº {id}</h1>
        <div>
          <p>
            <Title>Players: </Title>
            <TrainersInBattle creatorId={creator.trainer} opponentId={opponent.trainer} />
          </p>

          <p>
            <Title>Winner: </Title>
            {winner || '?'}
            {winner === session.email && <Icon alt="winner" src={party} />}
          </p>
          <Container>
            {creator.team.map((pokemon, index) => (
              <div key={pokemon}>
                <Title>Round {index + 1}</Title>
                <RoundContainer>
                  <PokemonCard pokemonId={pokemon} trainerId={creator.trainer} />
                  <VSTag>VS</VSTag>
                  <PokemonCard
                    pokemonId={opponent.team ? opponent.team[index] : undefined}
                    trainerId={opponent.trainer}
                  />
                </RoundContainer>
              </div>
            ))}
          </Container>
        </div>
      </>
    );
  }
}

DetailBattle.propTypes = {
  battle: PropTypes.object,
  fetchBattle: PropTypes.func,
  match: PropTypes.object,
  session: PropTypes.object,
};

const mapStateToProps = (state, { match }) => {
  const { id } = match.params;
  return {
    session: selectUserInSession(state),
    battle: selectBattleById(state, id),
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBattle: (battle) => dispatch(fetchBattle(battle)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(DetailBattle);
