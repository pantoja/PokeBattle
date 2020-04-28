import PropTypes from 'prop-types';
import React from 'react';
import styled from 'styled-components';

import pokeball from '../../image/pokeball.svg';

const StyledRow = styled.div`
  background-color: #fff;
  padding: 1rem 2rem;
  border-radius: 30px;
  display: grid;
  grid-template-columns: 40px repeat(3, 1fr) 60px;
  box-shadow: 0px 0px 15px -12px rgba(0, 0, 0, 0.74902);
  text-align: center;
  font-weight: 500;
  font-size: 0.8rem;
`;

const StyledImage = styled.img`
  width: 20px;
`;

const TableRow = (props) => {
  const { battles } = props;
  return (
    <div>
      {battles.map((battle) => (
        <StyledRow key={battle.id}>
          <StyledImage alt="pokeball-icon" src={pokeball} />
          <span>Battle nº {battle.id}</span>
          <span>{battle.created}</span>
          <span>
            {battle.userCreator.name} VS {battle.userOpponent.name}
          </span>
          {/* TODO: Conditional if user is winner use icons to represent */}
          <span>{battle.winner}</span>
        </StyledRow>
      ))}
    </div>
  );
};

TableRow.propTypes = {
  battles: PropTypes.object,
};

export default TableRow;
