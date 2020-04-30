import PropTypes from 'prop-types';
import React from 'react';
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
      {battles.map((battle) => (
        <StyledRow key={battle.id} to={getLink(battle.userOpponent.id, user.id, battle.id)}>
          <StyledImage alt="pokeball-icon" src={pokeball} />
          <span>Battle nº {battle.id}</span>
          <span>{battle.created}</span>
          <span>
            {battle.userCreator.name} VS {battle.userOpponent.name}
          </span>
          {battle.userOpponent.id === user.id ? (
            <StyledCall>You</StyledCall>
          ) : (
            <span>{battle.userOpponent.name}</span>
          )}
        </StyledRow>
      ))}
    </div>
  );
};

TableActiveRow.propTypes = {
  battles: PropTypes.object,
  user: PropTypes.object,
};

export default TableActiveRow;
