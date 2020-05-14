import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import pokeball from '../../image/pokeball.svg';
import { fetchActiveBattles } from '../actions/setBattle';
import { sessionSelector, battleResultsSelector, battlesListSelector } from '../utils/selectors';

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

class TableActiveRow extends Component {
  componentDidMount() {
    const { fetchActiveBattles } = this.props;
    fetchActiveBattles();
  }

  render() {
    const { battlesResult, battleList, session } = this.props;
    if (!battlesResult) return <>Loading</>;
    return (
      <div>
        {battlesResult.map((id) => {
          const battle = battleList[id];
          const { created, opponent, creator } = battle;
          return (
            <Row key={id} {...getLinkAttributes(opponent.trainer, session.id, id)}>
              <Image alt="pokeball-icon" src={pokeball} />
              <span>Battle nº {id}</span>
              <span>{created}</span>
              <TrainersInBattle creatorId={creator.trainer} opponentId={opponent.trainer} />
              <PendingAnswer opponent={opponent.trainer} session={session.id} />
            </Row>
          );
        })}
      </div>
    );
  }
}

TableActiveRow.propTypes = {
  battleList: PropTypes.object,
  battlesResult: PropTypes.array,
  session: PropTypes.object,
  fetchActiveBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: battleResultsSelector(state),
  battleList: battlesListSelector(state),
  session: sessionSelector(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchActiveBattles: () => dispatch(fetchActiveBattles()),
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(TableActiveRow);
