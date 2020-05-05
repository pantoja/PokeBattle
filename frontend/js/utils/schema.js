import { schema } from 'normalizr';

export const battle = new schema.Entity('battles');

export const battleList = new schema.Array(battle);
