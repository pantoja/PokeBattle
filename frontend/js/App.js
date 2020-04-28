import React from 'react';
import { hot } from 'react-hot-loader/root';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import DetailBattle from './pages/DetailBattle';
import ListSettledBattles from './pages/ListSettledBattles';

const App = () => (
  <Router>
    <Switch>
      <Route component={DetailBattle} path="/battle/:id" />
      <Route component={ListSettledBattles} path="/settled-battles" />
    </Switch>
  </Router>
);

export default hot(App);
