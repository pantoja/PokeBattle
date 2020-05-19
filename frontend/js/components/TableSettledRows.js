import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { fetchSettledBattles } from '../actions/setBattle';
import { selectBattlesResult } from '../utils/selectors';

import SettledRow from './SettledRow';

class TableSettledRows extends Component {
  componentDidMount() {
    const { fetchSettledBattles } = this.props;
    fetchSettledBattles();
  }

  render() {
    const { battlesResult } = this.props;
    if (!battlesResult) return <>Loading</>;
    return battlesResult.map((id) => {
      return <SettledRow key={id} battleId={id} />;
    });
  }
}

TableSettledRows.propTypes = {
  battlesResult: PropTypes.array,
  fetchSettledBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: selectBattlesResult(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchSettledBattles: () => dispatch(fetchSettledBattles()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TableSettledRows);
