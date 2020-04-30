import { GET_USER } from '../constants';

function getUser(user) {
  return { type: GET_USER, payload: user };
}

export { getUser };
