import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { fetchActiveBattles } from '../actions/setBattle';
import { selectBattlesResult, selectBattles } from '../utils/selectors';

import ActiveRow from './ActiveRow';

class TableActiveRows extends Component {
  componentDidMount() {
    const { fetchActiveBattles } = this.props;
    fetchActiveBattles();
  }

  render() {
    const { battlesResult, battleList } = this.props;
    if (!battlesResult) return <>Loading</>;
    return battlesResult.map((id) => {
      const battle = battleList[id];
      return <ActiveRow key={id} battle={battle} />;
    });
  }
}

TableActiveRows.propTypes = {
  battleList: PropTypes.object,
  battlesResult: PropTypes.array,
  fetchActiveBattles: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battlesResult: selectBattlesResult(state),
  battleList: selectBattles(state),
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchActiveBattles: () => dispatch(fetchActiveBattles()),
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(TableActiveRows);
