import PropTypes from 'prop-types';
import React from 'react';
import styled from 'styled-components';

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

const TableHeader = (props) => {
  const { header } = props;
  return (
    <StyledRow>
      {header.map((item) => (
        <span key={item.id}>{item}</span>
      ))}
    </StyledRow>
  );
};

TableHeader.propTypes = {
  header: PropTypes.object,
};

export default TableHeader;
