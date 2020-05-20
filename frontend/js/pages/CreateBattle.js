import { Formik, Form } from 'formik';
import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import ChooseOpponent from '../components/ChooseOpponent';
import ChooseTeam from '../components/ChooseTeam';
import { postBattleAPI, postTeamAPI } from '../utils/services';
import 'react-bootstrap-typeahead/css/Typeahead.css';

const StyledForm = styled(Form)`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 90vw;
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

const CreateBattle = (props) => {
  return (
    <Page>
      <h2>Create a Battle</h2>
      <Formik
        initialValues={{
          opponent: '',
          pokemon_1: '',
          pokemon_2: '',
          pokemon_3: '',
        }}
        onSubmit={(fields, { setFieldError }) => {
          const battle_data = {
            user_opponent: fields.opponent,
          };

          const { order } = fields;
          const { pokemonFields } = props;

          const team_data = {
            pokemon_1: pokemonFields[order[0]],
            pokemon_2: pokemonFields[order[1]],
            pokemon_3: pokemonFields[order[2]],
          };
          postBattleAPI(battle_data)
            .then((response) => {
              team_data.battle = response.data.id;
              return postTeamAPI(team_data);
            })
            .catch((err) => {
              if (err.response.status === 400) {
                setFieldError('team', err.response.data.non_field_errors[0]);
              }
            });
        }}
      >
        {({ setFieldValue, errors }) => (
          <StyledForm>
            <ChooseOpponent setFieldValue={setFieldValue} />
            <ChooseTeam errors={errors} setFieldValue={setFieldValue} />
            <Submit type="submit" value="Go!" />
          </StyledForm>
        )}
      </Formik>
    </Page>
  );
};

CreateBattle.propTypes = {
  pokemonFields: PropTypes.object,
};

const mapStateToProps = (state) => ({
  pokemonFields: state.form.pokemonFields,
});

export default connect(mapStateToProps)(CreateBattle);
