import { SET_BATTLE } from '../constants';
import { getBattleAPI } from '../utils/services';

function writeBattle(battle) {
  return { type: SET_BATTLE, payload: battle };
}

function setBattle(battle) {
  return (dispatch) =>
    getBattleAPI(battle).then((battleData) => {
      return dispatch(writeBattle(battleData));
    });
}

export { setBattle };
