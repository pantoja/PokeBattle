import PropTypes from 'prop-types';
import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

import cross from '../../image/cross.svg';
import pokeball from '../../image/pokeball.svg';
import tick from '../../image/tick.svg';

const StyledRow = styled(Link)`
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

const StyledImage = styled.img`
  width: 20px;
  justify-self: center;
`;

const TableSettledRow = (props) => {
  const { battles } = props;
  // TODO: Replace this constant with user in session from redux
  const user = 'admin@admin.com';
  return (
    <div>
      {battles.map((battle) => (
        <StyledRow key={battle.id} to={`/battle/${battle.id}`}>
          <StyledImage alt="pokeball-icon" src={pokeball} />
          <span>Battle nº {battle.id}</span>
          <span>{battle.created}</span>
          <span>
            {battle.userCreator.name} VS {battle.userOpponent.name}
          </span>
          {battle.winner === user ? <StyledImage src={tick} /> : <StyledImage src={cross} />}
        </StyledRow>
      ))}
    </div>
  );
};

TableSettledRow.propTypes = {
  battles: PropTypes.object,
};

export default TableSettledRow;
