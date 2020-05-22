import { normalize } from 'normalizr';

import { SET_BATTLE } from '../constants';
import * as schema from '../utils/schema';
import { getBattleAPI, getActiveBattlesAPI, getSettledBattlesAPI } from '../utils/services';

function writeBattle(list) {
  return { type: SET_BATTLE, payload: list };
}

function fetchBattle(battle) {
  return (dispatch) =>
    getBattleAPI(battle).then((battleData) => {
      const normalizedBattle = normalize(battleData, schema.battle);
      return dispatch(writeBattle(normalizedBattle));
    });
}

function fetchActiveBattles() {
  return (dispatch) =>
    getActiveBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattle(normalizedBattleList));
    });
}

function fetchSettledBattles() {
  return (dispatch) =>
    getSettledBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattle(normalizedBattleList));
    });
}

export { fetchBattle, fetchActiveBattles, fetchSettledBattles };
