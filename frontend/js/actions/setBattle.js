import { normalize } from 'normalizr';

import { SET_BATTLE, LIST_BATTLE } from '../constants';
import * as schema from '../utils/schema';
import { getBattleAPI, getActiveBattlesAPI, getSettledBattlesAPI } from '../utils/services';

function writeBattleDetail(battle) {
  return { type: SET_BATTLE, payload: battle };
}

function writeBattleList(list) {
  return { type: LIST_BATTLE, payload: list };
}

function setBattle(battle) {
  return (dispatch) =>
    getBattleAPI(battle).then((battleData) => {
      const normalizedBattle = normalize(battleData, schema.battle);
      return dispatch(writeBattleDetail(normalizedBattle.entities));
    });
}

function setActiveBattles() {
  return (dispatch) =>
    getActiveBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattleList(normalizedBattleList.entities));
    });
}

function setSettledBattles() {
  return (dispatch) =>
    getSettledBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattleList(normalizedBattleList.entities));
    });
}

export { setBattle, setActiveBattles, setSettledBattles };
