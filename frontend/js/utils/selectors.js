const pokemonSelector = (state, id) => {
  return state.battles.pokemon[id];
};

const userSelector = (state, id) => {
  return state.battles.users[id];
};

const sessionSelector = (state) => {
  return state.session;
};

const battleSelector = (state, id) => {
  return state.battles.battles[id];
};

const battleResultsSelector = (state) => {
  return state.battles.battles;
};

export { sessionSelector, pokemonSelector, userSelector, battleResultsSelector, battleSelector };
