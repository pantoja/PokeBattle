import axios from 'axios';

const getAPI = (url) => {
  return axios.get(url).then((response) => {
    return response.data;
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

export { getBattleAPI, getActiveBattlesAPI, getSettledBattlesAPI, getUserAPI, getUserListAPI };
