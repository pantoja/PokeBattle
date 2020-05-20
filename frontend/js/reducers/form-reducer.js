import { SET_TEAM } from '../constants';

const formReducer = (state = { pokemonFields: {} }, action) => {
  switch (action.type) {
    case SET_TEAM: {
      return {
        pokemonFields: { ...state.pokemonFields, [action.payload.index]: action.payload.pokemon },
      };
    }
    default:
      return state;
  }
};

export default formReducer;
