import { SET_USER } from '../constants';
import { getUserAPI } from '../utils/services';

function writeUser(user) {
  return { type: SET_USER, payload: user };
}

function setUser() {
  return (dispatch) =>
    getUserAPI().then((userData) => {
      return dispatch(writeUser(userData));
    });
}

export { setUser };
