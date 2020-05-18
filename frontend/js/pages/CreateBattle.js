import { Formik, Form } from 'formik';
import PropTypes from 'prop-types';
import React from 'react';
import styled from 'styled-components';

import ChooseOpponent from '../components/ChooseOpponent';
import ChooseTeam from '../components/ChooseTeam';
import { postBattleAPI, postTeamAPI } from '../utils/services';

const Page = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
`;

const StyledForm = styled(Form)`
  display: flex;
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
        onSubmit={(fields) => {
          const battle_data = {
            user_opponent: fields.opponent,
          };
          const team_data = {
            first_pokemon: fields.pokemon_1,
            second_pokemon: fields.pokemon_2,
            third_pokemon: fields.pokemon_3,
            choice_1: 1,
            choice_2: 2,
            choice_3: 3,
          };
          postBattleAPI(battle_data).then((response) => {
            team_data.battle = response.data.id;
            return postTeamAPI(team_data);
          });
        }}
      >
        {(props) => (
          <StyledForm>
            <ChooseOpponent />
            <ChooseTeam setFieldValue={props.setFieldValue} />
            <input type="submit" value="Go!" />
          </StyledForm>
        )}
      </Formik>
    </Page>
  );
};

CreateBattle.propTypes = {
  setFieldValue: PropTypes.func,
};

export default CreateBattle;
