import { Formik, Form } from 'formik';
import React from 'react';
import styled from 'styled-components';

import ChooseOpponent from '../components/ChooseOpponent';
import ChooseTeam from '../components/ChooseTeam';
import { postBattleAPI, postTeamAPI } from '../utils/services';
import 'react-bootstrap-typeahead/css/Typeahead.css';

const StyledForm = styled(Form)`
  width: 50vw;
`;

const Page = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
`;

const CreateBattle = () => {
  return (
    <Page>
      <h2>Create a battle</h2>
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
          const team_data = {
            first_pokemon: fields.pokemon_1,
            second_pokemon: fields.pokemon_2,
            third_pokemon: fields.pokemon_3,
          };
          postBattleAPI(battle_data)
            .then((response) => {
              team_data.battle = response.data.id;
              console.log(team_data);
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
            <input type="submit" value="Go!" />
          </StyledForm>
        )}
      </Formik>
    </Page>
  );
};

export default CreateBattle;
