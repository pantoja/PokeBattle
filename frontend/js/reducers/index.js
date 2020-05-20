import { combineReducers } from 'redux';

import battleReducer from './battle-reducer';
import formReducer from './form-reducer';
import userReducer from './user-reducer';

const rootReducer = combineReducers({
  battles: battleReducer,
  form: formReducer,
  session: userReducer,
});

export default rootReducer;
