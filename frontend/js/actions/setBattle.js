import { normalize } from 'normalizr';

import { SET_BATTLE, LIST_USER, LIST_POKEMON } from '../constants';
import * as schema from '../utils/schema';
import {
  getBattleAPI,
  getActiveBattlesAPI,
  getSettledBattlesAPI,
  getUserListAPI,
  getPokemonAPI,
} from '../utils/services';

function writeBattle(list) {
  return { type: SET_BATTLE, payload: list };
}

function writeUserList(user) {
  return { type: LIST_USER, payload: user };
}

function writePokemonList(pokemon) {
  return { type: LIST_POKEMON, payload: pokemon };
}

function fetchBattle(battle) {
  return (dispatch) =>
    getBattleAPI(battle).then((battleData) => {
      const normalizedBattle = normalize(battleData, schema.battle);
      return dispatch(writeBattle(normalizedBattle));
    });
}

function fetchActiveBattles() {
  return (dispatch) =>
    getActiveBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattle(normalizedBattleList));
    });
}

function fetchSettledBattles() {
  return (dispatch) =>
    getSettledBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattle(normalizedBattleList));
    });
}

function fetchUserList() {
  return (dispatch) =>
    getUserListAPI().then((userList) => {
      return dispatch(writeUserList(userList));
    });
}

function fetchPokemonList() {
  return (dispatch) =>
    getPokemonAPI().then((pokemonList) => {
      return dispatch(writePokemonList(pokemonList));
    });
}

export { fetchBattle, fetchActiveBattles, fetchSettledBattles, fetchUserList, fetchPokemonList };
