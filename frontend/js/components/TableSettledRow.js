import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import cross from '../../image/cross.svg';
import pokeball from '../../image/pokeball.svg';
import tick from '../../image/tick.svg';
import { fetchSettledBattles } from '../actions/setBattle';
import { selectUserInSession, selectBattlesResult, selectBattles } from '../utils/selectors';

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

class TableSettledRow extends Component {
  componentDidMount() {
    const { fetchSettledBattles } = this.props;
    fetchSettledBattles();
  }

  render() {
    const { battlesResult, battleList, session } = this.props;
    if (!battlesResult) return <>Loading</>;
    return (
      <div>
        {battlesResult.map((id) => {
          const battle = battleList[id];
          const { created, opponent, creator, winner } = battle;
          return (
            <Row key={id} to={`/battle/${id}`}>
              <Image alt="pokeball-icon" src={pokeball} />
              <span>Battle nº {id}</span>
              <span>{created}</span>
              <TrainersInBattle creatorId={creator.trainer} opponentId={opponent.trainer} />
              {winner === session.email ? <Image src={tick} /> : <Image src={cross} />}
            </Row>
          );
        })}
      </div>
    );
  }
}

TableSettledRow.propTypes = {
  battleList: PropTypes.object,
  battlesResult: PropTypes.array,
  session: PropTypes.object,
  fetchSettledBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: selectBattlesResult(state),
  battleList: selectBattles(state),
  session: selectUserInSession(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchSettledBattles: () => dispatch(fetchSettledBattles()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TableSettledRow);
