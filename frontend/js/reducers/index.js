import { combineReducers } from 'redux';

import battleReducer from './battle-reducer';

const rootReducer = combineReducers({
  battles: battleReducer,
});

export default rootReducer;
