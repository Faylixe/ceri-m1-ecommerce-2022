import {createAction, props} from '@ngrx/store';

export const initAction = createAction('Init app');

export const changeUsername = createAction('change username', props<{ username: string }>());

export const getUser = createAction('User info', props<{user : any}>());

export const disconnect = createAction('Log out', props<{user : any}>());

//export const disconnect = createAction('log out', props<{ isloged: boolean }>());

export const logOut = createAction('Log out user');