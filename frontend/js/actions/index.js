const GET_BATTLE = 'GET_BATTLE';

function getBattle(battle) {
  return { type: GET_BATTLE, payload: battle };
}

export { getBattle };
