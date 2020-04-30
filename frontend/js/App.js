import axios from 'axios';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { hot } from 'react-hot-loader/root';
import { connect } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import { getUser } from './actions/getUser';
import DetailBattle from './pages/DetailBattle';
import ListActiveBattles from './pages/ListActiveBattles';
import ListSettledBattles from './pages/ListSettledBattles';

class App extends Component {
  componentDidMount() {
    const { getUser } = this.props;
    axios.get(`/api/user/`).then((response) => {
      return getUser(response.data);
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
  getUser: PropTypes.func,
  user: PropTypes.object,
};

const mapStateToProps = (state) => ({
  user: state.user,
});

const mapDispatchToProps = (dispatch) => {
  return {
    getUser: (user) => dispatch(getUser(user)),
  };
};

export default hot(connect(mapStateToProps, mapDispatchToProps)(App));
