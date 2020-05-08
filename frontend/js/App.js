import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { hot } from 'react-hot-loader/root';
import { connect } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import { setUser } from './actions/setUser';
import DetailBattle from './pages/DetailBattle';
import ListActiveBattles from './pages/ListActiveBattles';
import ListSettledBattles from './pages/ListSettledBattles';
import { getUserAPI } from './utils/services';

class App extends Component {
  componentDidMount() {
    const { setUser } = this.props;
    getUserAPI().then((userData) => {
      return setUser(userData);
    });
  }

  render() {
    const { user } = this.props;
    if (Object.keys(user).length === 0) {
      return <div>Loading</div>;
    }
    return (
      <Router>
        <Switch>
          <Route component={DetailBattle} path="/battle/:id" />
          <Route component={ListActiveBattles} path="/active-battles" />
          <Route component={ListSettledBattles} path="/settled-battles" />
        </Switch>
      </Router>
    );
  }
}

App.propTypes = {
  setUser: PropTypes.func,
  user: PropTypes.object,
};

const mapStateToProps = (state) => ({
  user: state.user,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setUser: (user) => dispatch(setUser(user)),
  };
};

export default hot(connect(mapStateToProps, mapDispatchToProps)(App));
