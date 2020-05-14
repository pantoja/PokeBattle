import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import cross from '../../image/cross.svg';
import pokeball from '../../image/pokeball.svg';
import tick from '../../image/tick.svg';
import { setSettledBattles } from '../actions/setBattle';
import { sessionSelector, battleResultsSelector, battlesListSelector } from '../utils/selectors';

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
    const { setSettledBattles } = this.props;
    setSettledBattles();
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
              <TrainersInBattle creator={creator.trainer} opponent={opponent.trainer} />
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
  setSettledBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: battleResultsSelector(state),
  battleList: battlesListSelector(state),
  session: sessionSelector(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    setSettledBattles: () => dispatch(setSettledBattles()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TableSettledRow);
