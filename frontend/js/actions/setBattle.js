import { SET_BATTLE } from '../constants';

function setBattle(battle) {
  return { type: SET_BATTLE, payload: battle };
}

export { setBattle };
