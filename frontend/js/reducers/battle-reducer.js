const initialState = {
  battle: {},
  isLoading: true,
};

const battleReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'GET_BATTLE':
      return {
        ...state,
        battle: action.payload,
        isLoading: false,
      };
    default:
      return state;
  }
};

export default battleReducer;
