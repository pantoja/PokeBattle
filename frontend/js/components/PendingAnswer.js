import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import { selectUserById } from '../utils/selectors';

const AnswerTag = styled.span`
  position: relative;
  &&:after {
    content: 'Answer';
    color: #fff;
    background-color: #f9ab2f;
    padding: 5px;
    position: absolute;
    right: -40px;
    bottom: -5px;
    font-weight: 500;
    outline: dashed #29344c;
  }
`;

const PendingAnswer = (props) => {
  const { sessionId, opponent } = props;
  if (opponent.id === sessionId) {
    return <AnswerTag>You</AnswerTag>;
  }
  return <span>{opponent.name}</span>;
};

PendingAnswer.propTypes = {
  opponent: PropTypes.object,
  sessionId: PropTypes.number,
};

const mapStateToProps = (state, { opponentId }) => {
  return {
    opponent: selectUserById(state, opponentId),
  };
};

export default connect(mapStateToProps)(PendingAnswer);
