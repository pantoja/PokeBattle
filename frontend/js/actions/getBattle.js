import axios from 'axios';
import { normalize } from 'normalizr';

import { GET_BATTLE } from '../constants';
import * as schema from '../utils/schema';

function writeBattle(battle) {
  return { type: GET_BATTLE, payload: battle };
}

function getBattle(battle) {
  return (dispatch) =>
    axios.get(`/api/battle/${battle}`).then((response) => {
      const normalizedBattle = normalize(response.data, schema.battle);
      console.log('normalized response', normalizedBattle.entities.battles);
      return dispatch(writeBattle(normalizedBattle.entities.battles));
    });
}

function writeBattleList(list) {
  return { type: 'LIST_BATTLE', payload: list };
}

function listBattle() {
  return (dispatch) =>
    axios.get(`/api/battles/active`).then((response) => {
      const normalizedBattleList = normalize(response.data, schema.battleList);
      return dispatch(writeBattleList(normalizedBattleList.entities.battles));
    });
}

export { getBattle, listBattle };
