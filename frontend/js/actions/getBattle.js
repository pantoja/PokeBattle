import { GET_BATTLE } from '../constants';

function getBattle(battle) {
  return { type: GET_BATTLE, payload: battle };
}

export { getBattle };
