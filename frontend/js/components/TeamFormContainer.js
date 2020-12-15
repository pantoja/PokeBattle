import PropTypes from 'prop-types';
import React from 'react';
import styled from 'styled-components';

import ChooseOpponent from './ChooseOpponent';
import ChooseTeam from './ChooseTeam';

const FormContainer = styled.div`
  background-color: white;
  border-radius: 5px;
`;

const TeamFormContainer = (props) => {
  const { setFieldValue } = props;
  return (
    <FormContainer>
      <ChooseOpponent setFieldValue={setFieldValue} />
      <ChooseTeam setFieldValue={setFieldValue} />
    </FormContainer>
  );
};

TeamFormContainer.propTypes = {
  setFieldValue: PropTypes.func,
};

export default TeamFormContainer;
