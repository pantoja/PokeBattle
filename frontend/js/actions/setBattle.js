import { normalize } from 'normalizr';

import { SET_BATTLE } from '../constants';
import * as schema from '../utils/schema';
import { getBattleAPI, getActiveBattlesAPI, getSettledBattlesAPI } from '../utils/services';

function writeBattle(list) {
  return { type: SET_BATTLE, payload: list };
}

function setBattle(battle) {
  return (dispatch) =>
    getBattleAPI(battle).then((battleData) => {
      const normalizedBattle = normalize(battleData, schema.battle);
      return dispatch(writeBattle(normalizedBattle));
    });
}

function setActiveBattles() {
  return (dispatch) =>
    getActiveBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattle(normalizedBattleList));
    });
}

function setSettledBattles() {
  return (dispatch) =>
    getSettledBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattle(normalizedBattleList));
    });
}

export { setBattle, setActiveBattles, setSettledBattles };
