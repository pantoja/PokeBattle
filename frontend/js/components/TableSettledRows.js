import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { fetchSettledBattles } from '../actions/setBattle';
import { selectBattlesResult, selectBattles } from '../utils/selectors';

import SettledRow from './SettledRow';

class TableSettledRows extends Component {
  componentDidMount() {
    const { fetchSettledBattles } = this.props;
    fetchSettledBattles();
  }

  render() {
    const { battlesResult, battleList } = this.props;
    if (!battlesResult) return <>Loading</>;
    return battlesResult.map((id) => {
      const battle = battleList[id];
      return <SettledRow key={id} battle={battle} />;
    });
  }
}

TableSettledRows.propTypes = {
  battleList: PropTypes.object,
  battlesResult: PropTypes.array,
  fetchSettledBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: selectBattlesResult(state),
  battleList: selectBattles(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchSettledBattles: () => dispatch(fetchSettledBattles()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TableSettledRows);
