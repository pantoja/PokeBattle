import axios from 'axios';
import PropTypes from 'prop-types';
import React, { Component } from 'react';

import TableActiveRow from '../components/TableActiveRow';
import TableHeader from '../components/TableHeader';

class ListActiveBattles extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableHeader: ['', 'Battle Number', 'Created', 'Trainers', 'Pending Answer From'],
      battles: [],
    };
  }

  async componentDidMount() {
    axios.get(`/api/battles/active`).then((response) => {
      this.setState({ battles: response.data });
      return response.data;
    });
  }

  render() {
    const { battles, tableHeader } = this.state;
    const { user } = this.props;
    return (
      <>
        <h1>List Active Battles</h1>
        <TableHeader header={tableHeader} />
        <TableActiveRow battles={battles} user={user} />
      </>
    );
  }
}

ListActiveBattles.propTypes = {
  user: PropTypes.object,
};

export default ListActiveBattles;
