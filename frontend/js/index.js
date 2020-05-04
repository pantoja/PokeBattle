// import pages
import React from 'react';
import ReactDOM from 'react-dom';
import './bootstrap-includes';
import '../sass/style.scss';
import { Provider } from 'react-redux';

import App from './App';
import store from './store';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('react-app')
);
