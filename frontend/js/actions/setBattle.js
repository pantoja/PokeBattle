import { normalize } from 'normalizr';

import { SET_BATTLE, LIST_BATTLE } from '../constants';
import * as schema from '../utils/schema';
import { getBattleAPI, getActiveBattlesAPI } from '../utils/services';

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
      return dispatch(writeBattleDetail(normalizedBattle.entities.battles));
      // return dispatch(writeBattleDetail(battleData));
    });
}

function listBattle() {
  return (dispatch) =>
    getActiveBattlesAPI().then((battleList) => {
      // const normalizedBattleList = normalize(battleList, schema.battleList);
      // return dispatch(writeBattleList(normalizedBattleList.entities.battles));
      return dispatch(writeBattleList(battleList));
    });
}

export { setBattle, listBattle };
