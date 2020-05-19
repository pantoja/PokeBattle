const selectPokemonById = (state, id) => {
  return state.battles.pokemon[id];
};

const selectUserById = (state, id) => {
  return state.battles.users[id];
};

const selectUserInSession = (state) => {
  return state.session;
};

const selectBattlesResult = (state) => {
  return state.battles.battlesResult;
};

const selectBattleById = (state, id) => {
  return state.battles.battles[id];
};

export {
  selectUserInSession,
  selectPokemonById,
  selectUserById,
  selectBattlesResult,
  selectBattleById,
};
