import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import pokeball from '../../image/pokeball.svg';
import { setBattleList } from '../actions/setBattle';

import PendingAnswer from './PendingAnswer';
import TrainersInBattle from './TrainersInBattle';

const StyledRow = styled(Link)`
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

const StyledImage = styled.img`
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
    const { setBattleList } = this.props;
    setBattleList();
  }

  render() {
    const { battles, session } = this.props;
    if (!battles) return <>Loading</>;

    const battleList = Object.values(battles);
    return (
      <div>
        {battleList.map((battle) => {
          const { id, created, opponent, creator } = battle;
          return (
            <StyledRow key={id} {...getLinkAttributes(opponent.trainer, session.id, id)}>
              <StyledImage alt="pokeball-icon" src={pokeball} />
              <span>Battle nº {id}</span>
              <span>{created}</span>
              <TrainersInBattle creator={creator.trainer} opponent={opponent.trainer} />
              <PendingAnswer opponent={opponent.trainer} session={session.id} />
            </StyledRow>
          );
        })}
      </div>
    );
  }
}

TableActiveRow.propTypes = {
  battles: PropTypes.object,
  session: PropTypes.object,
  setBattleList: PropTypes.func,
};

const mapStateToProps = (state) => ({
  session: state.session,
  battles: state.battles.battles,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setBattleList: () => dispatch(setBattleList()),
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(TableActiveRow);
