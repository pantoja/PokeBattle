import { SET_BATTLE, LIST_BATTLE } from '../constants';

const battleReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_BATTLE: {
      const key = Object.keys(action.payload);
      return {
        ...state,
        [key]: action.payload[key],
      };
    }
    case LIST_BATTLE: {
      return action.payload;
    }
    default:
      return state;
  }
};

export default battleReducer;
