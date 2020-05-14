const pokemonSelector = (state, id) => {
  return state.battles.pokemon[id];
};

const userSelector = (state, id) => {
  return state.battles.users[id];
};

const sessionSelector = (state) => {
  return state.session;
};

const battleResultsSelector = (state) => {
  return state.battles.battlesResult;
};

const battlesListSelector = (state) => {
  return state.battles.battles;
};

export {
  sessionSelector,
  pokemonSelector,
  userSelector,
  battlesListSelector,
  battleResultsSelector,
};
