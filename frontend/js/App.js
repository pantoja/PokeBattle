import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { hot } from 'react-hot-loader/root';
import { connect } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import { setUser } from './actions/setUser';
import CreateBattle from './pages/CreateBattle';
import DetailBattle from './pages/DetailBattle';
import ListActiveBattles from './pages/ListActiveBattles';
import ListSettledBattles from './pages/ListSettledBattles';

class App extends Component {
  componentDidMount() {
    const { setUser } = this.props;
    setUser();
  }

  render() {
    const { session } = this.props;
    if (!session) return <div>Loading</div>;
    return (
      <Router>
        <Switch>
          <Route component={DetailBattle} path="/battle/:id" />
          <Route component={ListActiveBattles} path="/active-battles" />
          <Route component={ListSettledBattles} path="/settled-battles" />
          <Route component={CreateBattle} path="/create-battle" />
        </Switch>
      </Router>
    );
  }
}

App.propTypes = {
  setUser: PropTypes.func,
  session: PropTypes.object,
};

const mapStateToProps = (state) => ({
  session: state.session,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setUser: () => dispatch(setUser()),
  };
};

export default hot(connect(mapStateToProps, mapDispatchToProps)(App));
