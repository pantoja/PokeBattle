import { SET_USER, LIST_USER } from '../constants';
import { getUserAPI, getUserListAPI } from '../utils/services';

function writeUser(user) {
  return { type: SET_USER, payload: user };
}

function writeUserList(user) {
  return { type: LIST_USER, payload: user };
}

function setUser() {
  return (dispatch) =>
    getUserAPI().then((userData) => {
      return dispatch(writeUser(userData));
    });
}

function setUserList() {
  return (dispatch) =>
    getUserListAPI().then((userList) => {
      return dispatch(writeUserList(userList));
    });
}

export { setUser, setUserList };
