import axios from 'axios';

import { GET_USER } from '../constants';

function writeUser(user) {
  return { type: GET_USER, payload: user };
}

function getUser() {
  return (dispatch) =>
    axios.get('/api/user/').then((response) => {
      return dispatch(writeUser(response.data));
    });
}

export { getUser };
