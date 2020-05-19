import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import pokeball from '../../image/pokeball.svg';
import { selectUserInSession, selectBattleById } from '../utils/selectors';

import PendingAnswer from './PendingAnswer';
import TrainersInBattle from './TrainersInBattle';

const Row = styled(Link)`
  background-color: #fff;
  padding: 1rem 2rem;
  border-radius: 30px;
  display: grid;
  grid-template-columns: 40px repeat(4, 1fr);
  box-shadow: 0px 0px 15px -12px rgba(0, 0, 0, 0.74902);
  text-align: center;
  font-size: 0.8rem;
  margin-bottom: 1rem;
`;

const Image = styled.img`
  width: 20px;
`;

const getLinkAttributes = (opponent, session, id) => {
  if (session === opponent) {
    return { as: 'a', href: `/create-team/${id}` };
  }
  return { to: `/battle/${id}` };
};

const ActiveRow = (props) => {
  const { battle, session } = props;
  const { id, created, opponent, creator } = battle;
  return (
    <Row {...getLinkAttributes(opponent.trainer, session.id, id)}>
      <Image alt="pokeball-icon" src={pokeball} />
      <span>Battle nº {id}</span>
      <span>{created}</span>
      <TrainersInBattle creatorId={creator.trainer} opponentId={opponent.trainer} />
      <PendingAnswer opponent={opponent.trainer} session={session.id} />
    </Row>
  );
};

ActiveRow.propTypes = {
  battle: PropTypes.object,
  session: PropTypes.object,
};

const mapStateToProps = (state, { battleId }) => {
  return {
    session: selectUserInSession(state),
    battle: selectBattleById(state, battleId),
  };
};

export default connect(mapStateToProps)(ActiveRow);
