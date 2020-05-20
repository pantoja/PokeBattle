import { SET_BATTLE, LIST_USER, LIST_POKEMON } from '../constants';

const initialState = {
  battles: {},
  users: {},
  pokemon: {},
  battlesResult: [],
};

const battleReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_BATTLE: {
      const { entities } = action.payload;
      return {
        battles: { ...state.battles, ...entities.battles },
        users: { ...state.users, ...entities.users },
        pokemon: { ...state.pokemon, ...entities.pokemon },
        battlesResult: action.payload.result,
      };
    }
    case LIST_USER: {
      return {
        ...state,
        users: action.payload,
      };
    }
    case LIST_POKEMON: {
      return {
        ...state,
        pokemon: action.payload,
      };
    }
    default:
      return state;
  }
};

export default battleReducer;
