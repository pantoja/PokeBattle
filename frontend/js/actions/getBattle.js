import axios from 'axios';

import { GET_BATTLE } from '../constants';

function writeBattle(battle) {
  return { type: GET_BATTLE, payload: battle };
}

function getBattle(battle) {
  return (dispatch) =>
    axios.get(`/api/battle/${battle}`).then((response) => {
      return dispatch(writeBattle(response.data));
    });
}

export { getBattle };
