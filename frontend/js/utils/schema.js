import { schema } from 'normalizr';

export const user = new schema.Entity('users');

export const pokemon = new schema.Entity('pokemon');

export const battle = new schema.Entity('battles', {
  creator: {
    trainer: user,
    team: [pokemon],
  },
  opponent: {
    trainer: user,
  },
});

export const battleList = new schema.Array(battle);
