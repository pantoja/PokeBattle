import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import pokeball from '../../image/pokeball.svg';

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

const getLink = (opponent, user, id) => {
  if (user === opponent) {
    return `/create-team/${id}`;
  }
  return `/battle/${id}`;
};

const TableActiveRow = (props) => {
  const { battles, user } = props;
  return (
    <div>
      {battles.map((battle) => {
        const { id, created, user_opponent, user_creator } = battle;
        return (
          <StyledRow key={id} to={getLink(user_opponent.id, user.user.id, id)}>
            <StyledImage alt="pokeball-icon" src={pokeball} />
            <span>Battle nº {id}</span>
            <span>{created}</span>
            <span>
              {user_creator.name} VS {user_opponent.name}
            </span>
            {user_opponent.id === user.user.id ? (
              <StyledCall>You</StyledCall>
            ) : (
              <span>{user_opponent.name}</span>
            )}
          </StyledRow>
        );
      })}
    </div>
  );
};

TableActiveRow.propTypes = {
  battles: PropTypes.array,
  user: PropTypes.object,
};

const mapStateToProps = (state) => ({
  user: state.user,
});

export default connect(mapStateToProps, null)(TableActiveRow);
