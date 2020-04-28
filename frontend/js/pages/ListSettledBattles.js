import axios from 'axios';
import React, { Component } from 'react';

import TableHeader from '../components/TableHeader';
import TableRow from '../components/TableRow';
// import Table from '../components/Table';

class ListSettledBattles extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableHeader: ['', 'Battle Number', 'Created', 'Trainers', 'You Won'],
      battles: [],
    };
  }

  async componentDidMount() {
    axios
      .get(`/api/battles/settled`)
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
        <h1>List Settled Battles</h1>
        <TableHeader header={tableHeader} />
        <TableRow battles={battles} />
      </>
    );
  }
}

export default ListSettledBattles;
