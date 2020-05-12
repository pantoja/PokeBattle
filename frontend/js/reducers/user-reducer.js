import { SET_USER, LIST_USER } from '../constants';

const userReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_USER:
      return { ...state, session: action.payload };
    case LIST_USER: {
      return {
        ...state,
        users: action.payload,
      };
    }
    default:
      return state;
  }
};

export default userReducer;
