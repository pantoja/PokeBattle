import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import cross from '../../image/cross.svg';
import pokeball from '../../image/pokeball.svg';
import tick from '../../image/tick.svg';
import { selectUserInSession, selectBattleById } from '../utils/selectors';

import TrainersInBattle from './TrainersInBattle';

const Row = styled(Link)`
  background-color: #fff;
  padding: 1rem 2rem;
  border-radius: 30px;
  display: grid;
  grid-template-columns: 40px repeat(3, 1fr) 60px;
  box-shadow: 0px 0px 15px -12px rgba(0, 0, 0, 0.74902);
  text-align: center;
  font-weight: 500;
  font-size: 0.8rem;
  margin-bottom: 1rem;
`;

const Image = styled.img`
  width: 20px;
  justify-self: center;
`;

const SettledRow = (props) => {
  const { battle, session } = props;
  const { id, created, opponent, creator, winner } = battle;
  return (
    <Row to={`/battle/${id}`}>
      <Image alt="pokeball-icon" src={pokeball} />
      <span>Battle nº {id}</span>
      <span>{created}</span>
      <TrainersInBattle creatorId={creator.trainer} opponentId={opponent.trainer} />
      {winner === session.email ? <Image src={tick} /> : <Image src={cross} />}
    </Row>
  );
};

SettledRow.propTypes = {
  battle: PropTypes.object,
  session: PropTypes.object,
};

const mapStateToProps = (state, { battleId }) => ({
  session: selectUserInSession(state),
  battle: selectBattleById(state, battleId),
});

export default connect(mapStateToProps)(SettledRow);
