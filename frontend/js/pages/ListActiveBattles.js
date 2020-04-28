import axios from 'axios';
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
    axios
      .get(`/api/battles/active`)
      .then((response) => {
        this.setState({ battles: response.data });
        return response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    const { battles, tableHeader } = this.state;
    return (
      <>
        <h1>List Active Battles</h1>
        <TableHeader header={tableHeader} />
        <TableActiveRow battles={battles} />
      </>
    );
  }
}

export default ListActiveBattles;
