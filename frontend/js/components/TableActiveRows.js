import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { fetchActiveBattles } from '../actions/setBattle';
import { selectBattlesResult } from '../utils/selectors';

import ActiveRow from './ActiveRow';

class TableActiveRows extends Component {
  componentDidMount() {
    const { fetchActiveBattles } = this.props;
    fetchActiveBattles();
  }

  render() {
    const { battlesResult } = this.props;
    if (!battlesResult) return <>Loading</>;
    return battlesResult.map((id) => {
      // return <div>{id}</div>;
      return <ActiveRow key={id} battleId={id} />;
    });
  }
}

TableActiveRows.propTypes = {
  battlesResult: PropTypes.array,
  fetchActiveBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: selectBattlesResult(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchActiveBattles: () => dispatch(fetchActiveBattles()),
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(TableActiveRows);
