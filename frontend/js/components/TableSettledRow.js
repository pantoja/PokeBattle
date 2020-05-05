import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
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
  const { battles, user } = props;

  return (
    <div>
      {battles.map((battle) => {
        const { id, created, user_opponent, user_creator, winner } = battle;
        return (
          <StyledRow key={id} to={`/battle/${id}`}>
            <StyledImage alt="pokeball-icon" src={pokeball} />
            <span>Battle nº {id}</span>
            <span>{created}</span>
            <span>
              {user_creator.name} VS {user_opponent.name}
            </span>
            {winner === user.user.id ? <StyledImage src={tick} /> : <StyledImage src={cross} />}
          </StyledRow>
        );
      })}
    </div>
  );
};

TableSettledRow.propTypes = {
  battles: PropTypes.array,
  user: PropTypes.object,
};

const mapStateToProps = (state) => ({
  user: state.user,
});

export default connect(mapStateToProps, null)(TableSettledRow);
