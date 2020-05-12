import { SET_BATTLE, LIST_BATTLE, LIST_USER, LIST_POKEMON } from '../constants';

const battleReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_BATTLE: {
      return action.payload;
    }
    case LIST_BATTLE: {
      return action.payload;
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
