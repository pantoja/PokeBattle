import { Formik, Form } from 'formik';
import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import TeamFormContainer from '../components/TeamFormContainer';
import { postBattleAPI, postTeamAPI } from '../utils/services';
import 'react-bootstrap-typeahead/css/Typeahead.css';

const StyledForm = styled(Form)`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
`;

const Page = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
`;

const Submit = styled.input`
  width: 200px;
  border-radius: 5px;
  margin-top: 20px;
`;

const Message = styled.div`
  background-color: ${(props) => (props.success ? '#45a751' : '#f9ab2f')};
  color: #fff;
  border-radius: 10px;
  text-align: center;
  font-weight: 500;
  padding: 0.5rem;
  margin-bottom: 20px;
`;

const CreateBattle = (props) => {
  const onSubmit = (fields, { setStatus, setFieldError }) => {
    setStatus(false);
    const battle_data = {
      user_opponent: fields.opponent,
    };

    const { order } = fields;
    const { pokemonFields } = props;
    const team_data = orderPokemonInTeam(order, pokemonFields);

    postBattleAPI(battle_data)
      .then((response) => {
        team_data.battle = response.data.id;
        return postTeamAPI(team_data);
      })
      .then(() => {
        return setStatus(true);
      })
      .catch((err) => {
        if (err.response.status === 400) {
          setFieldError('team', err.response.data.non_field_errors[0]);
        }
      });
  };

  return (
    <Page>
      <h1>Create a Battle</h1>
      <Formik
        initialValues={{
          opponent: '',
          pokemon_1: '',
          pokemon_2: '',
          pokemon_3: '',
        }}
        onSubmit={(fields, actions) => onSubmit(fields, actions)}
      >
        {({ setFieldValue, errors, status }) => (
          <StyledForm>
            {status && <Message success>You have successfully created a battle!</Message>}
            {errors.team && <Message>{errors.team}</Message>}
            <TeamFormContainer setFieldValue={setFieldValue} />
            <Submit type="submit" value="Go!" />
          </StyledForm>
        )}
      </Formik>
    </Page>
  );
};

const orderPokemonInTeam = (order, pokemonFields) => {
  return {
    pokemon_1: pokemonFields[order[0]],
    pokemon_2: pokemonFields[order[1]],
    pokemon_3: pokemonFields[order[2]],
  };
};

CreateBattle.propTypes = {
  pokemonFields: PropTypes.object,
};

const mapStateToProps = (state) => ({
  pokemonFields: state.form.pokemonFields,
});

export default connect(mapStateToProps)(CreateBattle);
