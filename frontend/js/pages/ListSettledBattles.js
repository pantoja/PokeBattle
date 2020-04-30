import axios from 'axios';
import PropTypes from 'prop-types';
import React, { Component } from 'react';

import TableHeader from '../components/TableHeader';
import TableSettledRow from '../components/TableSettledRow';

class ListSettledBattles extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableHeader: ['', 'Battle Number', 'Created', 'Trainers', 'You Won'],
      battles: [],
    };
  }

  async componentDidMount() {
    axios.get(`/api/battles/settled`).then((response) => {
      this.setState({ battles: response.data });
      return response.data;
    });
  }

  render() {
    const { battles, tableHeader } = this.state;
    const { user } = this.props;
    return (
      <>
        <h1>List Settled Battles</h1>
        <TableHeader header={tableHeader} settled />
        <TableSettledRow battles={battles} user={user} />
      </>
    );
  }
}

ListSettledBattles.propTypes = {
  user: PropTypes.object,
};

export default ListSettledBattles;
