import { SET_BATTLE, LIST_BATTLE } from '../constants';

const initialState = {
  battle: {},
  battles: [],
  isLoading: true,
};

const battleReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_BATTLE: {
      const key = Object.keys(action.payload);
      return {
        ...state,
        [key]: action.payload[key],
        isLoading: false,
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
