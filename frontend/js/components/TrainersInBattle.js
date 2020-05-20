import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

import { selectUserById } from '../utils/selectors';

const TrainersInBattle = (props) => {
  const { creator, opponent } = props;
  return (
    <span>
      {creator.name} VS {opponent.name}
    </span>
  );
};

TrainersInBattle.propTypes = {
  creator: PropTypes.object,
  opponent: PropTypes.object,
};

const mapStateToProps = (state, { creatorId, opponentId }) => {
  return {
    creator: selectUserById(state, creatorId),
    opponent: selectUserById(state, opponentId),
  };
};

export default connect(mapStateToProps)(TrainersInBattle);
