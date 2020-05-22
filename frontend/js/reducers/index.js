import { combineReducers } from 'redux';

import battleReducer from './battle-reducer';
import userReducer from './user-reducer';

const rootReducer = combineReducers({
  battles: battleReducer,
  session: userReducer,
});

export default rootReducer;
