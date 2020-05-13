import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const getAPI = (url) => {
  return axios.get(url).then((response) => {
    return response.data;
  });
};

const postAPI = (url, data) => {
  return axios.post(url, data).then((response) => {
    return response;
  });
};

const getBattleAPI = (id) => {
  return getAPI(`/api/battle/${id}`);
};

const getActiveBattlesAPI = () => {
  return getAPI('/api/battles/active');
};

const getSettledBattlesAPI = () => {
  return getAPI('/api/battles/settled');
};

const getUserAPI = () => {
  return getAPI('/api/user/');
};

const getUserListAPI = () => {
  return getAPI('/api/users/');
};

const getPokemonAPI = () => {
  return getAPI('/api/pokemon/');
};

const postBattleAPI = (data) => {
  return postAPI('/api/battle/', data);
};

const postTeamAPI = (data) => {
  return postAPI('/api/team/', data);
};

export {
  getBattleAPI,
  getActiveBattlesAPI,
  getSettledBattlesAPI,
  getUserAPI,
  getUserListAPI,
  getPokemonAPI,
  postBattleAPI,
  postTeamAPI,
};
