import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

import { userSelector } from '../utils/selectors';

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

const mapStateToProps = (state, { creator, opponent }) => {
  return {
    creator: userSelector(state, creator),
    opponent: userSelector(state, opponent),
  };
};

export default connect(mapStateToProps)(TrainersInBattle);
