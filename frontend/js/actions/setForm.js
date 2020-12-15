import { SET_TEAM } from '../constants';

function writeTeamField(field) {
  return { type: SET_TEAM, payload: field };
}

function setTeamField(field) {
  return (dispatch) => dispatch(writeTeamField(field));
}

export { setTeamField };
