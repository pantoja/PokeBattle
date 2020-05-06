import axios from 'axios';

const getBattleAPI = (id) => {
  return axios.get(`/api/battle/${id}`).then((response) => {
    return response.data;
  });
};

const getActiveBattlesAPI = () => {
  return axios.get(`/api/battles/active`).then((response) => {
    return response.data;
  });
};

const getSettledBattlesAPI = () => {
  return axios.get(`/api/battles/settled`).then((response) => {
    return response.data;
  });
};

const getUserAPI = () => {
  return axios.get(`/api/user/`).then((response) => {
    return response.data;
  });
};

export { getBattleAPI, getActiveBattlesAPI, getSettledBattlesAPI, getUserAPI };
