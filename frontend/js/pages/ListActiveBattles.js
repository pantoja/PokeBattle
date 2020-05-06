import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { setBattleList } from '../actions/setBattle';
import TableActiveRow from '../components/TableActiveRow';
import TableHeader from '../components/TableHeader';

class ListActiveBattles extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableHeader: [
        { id: 0, content: '' },
        { id: 1, content: 'Battle Number' },
        { id: 2, content: 'Created' },
        { id: 3, content: 'Trainers' },
        { id: 4, content: 'Pending Answer From' },
      ],
    };
  }

  componentDidMount() {
    const { setBattleList } = this.props;
    setBattleList();
  }

  render() {
    const { tableHeader } = this.state;
    const { battles } = this.props;
    if (!battles) return <>Loading</>;
    return (
      <>
        <h1>List Active Battles</h1>
        <TableHeader header={tableHeader} />
        <TableActiveRow battles={Object.values(battles)} />
      </>
    );
  }
}

ListActiveBattles.propTypes = {
  battles: PropTypes.object,
  setBattleList: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battles: state.battles,
  isLoading: state.battles.isLoading,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setBattleList: () => dispatch(setBattleList()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ListActiveBattles);
