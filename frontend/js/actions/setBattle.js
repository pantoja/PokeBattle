import { normalize } from 'normalizr';

import { SET_BATTLE, LIST_BATTLE, LIST_USER, LIST_POKEMON } from '../constants';
import * as schema from '../utils/schema';
import {
  getBattleAPI,
  getActiveBattlesAPI,
  getSettledBattlesAPI,
  getUserListAPI,
  getPokemonAPI,
} from '../utils/services';

function writeBattleDetail(battle) {
  return { type: SET_BATTLE, payload: battle };
}

function writeBattleList(list) {
  return { type: LIST_BATTLE, payload: list };
}

function writeUserList(user) {
  return { type: LIST_USER, payload: user };
}

function writePokemonList(pokemon) {
  return { type: LIST_POKEMON, payload: pokemon };
}

function setBattle(battle) {
  return (dispatch) =>
    getBattleAPI(battle).then((battleData) => {
      const normalizedBattle = normalize(battleData, schema.battle);
      return dispatch(writeBattleDetail(normalizedBattle.entities));
    });
}

function setActiveBattles() {
  return (dispatch) =>
    getActiveBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattleList(normalizedBattleList.entities));
    });
}

function setSettledBattles() {
  return (dispatch) =>
    getSettledBattlesAPI().then((battleList) => {
      const normalizedBattleList = normalize(battleList, schema.battleList);
      return dispatch(writeBattleList(normalizedBattleList.entities));
    });
}

function setUserList() {
  return (dispatch) =>
    getUserListAPI().then((userList) => {
      return dispatch(writeUserList(userList));
    });
}

function setPokemonList() {
  return (dispatch) =>
    getPokemonAPI().then((pokemonList) => {
      return dispatch(writePokemonList(pokemonList));
    });
}

export { setBattle, setActiveBattles, setSettledBattles, setUserList, setPokemonList };
