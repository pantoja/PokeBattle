import { GET_BATTLE } from '../constants';

const initialState = {
  battle: {},
  battles: [],
  isLoading: true,
};

const battleReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_BATTLE: {
      const key = Object.keys(action.payload);
      const value = action.payload[key];
      return {
        ...state,
        [key]: {
          creator_team: value.creator_team,
          opponent_team: value.opponent_team,
        },
        isLoading: false,
      };
    }
    case 'LIST_BATTLE': {
      return action.payload;
    }
    default:
      return state;
  }
};

export default battleReducer;
