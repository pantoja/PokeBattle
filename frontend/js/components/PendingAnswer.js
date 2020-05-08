import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

const StyledCall = styled.span`
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
  const { session, opponent } = props;
  if (opponent.id === session) {
    return <StyledCall>You</StyledCall>;
  }
  return <span>{opponent.name}</span>;
};

PendingAnswer.propTypes = {
  opponent: PropTypes.object,
  session: PropTypes.number,
};

const mapStateToProps = (state, { opponent }) => {
  return {
    opponent: state.battles.users[opponent],
  };
};

export default connect(mapStateToProps)(PendingAnswer);
