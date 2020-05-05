import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { listBattle } from '../actions/getBattle';
import TableActiveRow from '../components/TableActiveRow';
import TableHeader from '../components/TableHeader';

class ListActiveBattles extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableHeader: ['', 'Battle Number', 'Created', 'Trainers', 'Pending Answer From'],
    };
  }

  componentDidMount() {
    const { listBattle } = this.props;
    listBattle();
  }

  render() {
    const { tableHeader } = this.state;
    const { battles } = this.props;
    if (!battles) return <>Loading</>;
    return (
      <>
        <h1>List Active Battles</h1>
        <TableHeader header={tableHeader} />
        <TableActiveRow battles={Object.values(battles).reverse()} />
      </>
    );
  }
}

ListActiveBattles.propTypes = {
  battles: PropTypes.object,
  listBattle: PropTypes.func,
};

const mapStateToProps = (state) => ({
  battles: state.battles,
  isLoading: state.battles.isLoading,
});

const mapDispatchToProps = (dispatch) => {
  return {
    listBattle: () => dispatch(listBattle()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ListActiveBattles);
