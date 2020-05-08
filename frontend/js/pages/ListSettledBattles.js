import React, { Component } from 'react';

import TableHeader from '../components/TableHeader';
import TableSettledRow from '../components/TableSettledRow';

class ListSettledBattles extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tableHeader: [
        { id: 0, content: '' },
        { id: 1, content: 'Battle Number' },
        { id: 2, content: 'Created' },
        { id: 3, content: 'Trainers' },
        { id: 4, content: 'You Won' },
      ],
    };
  }

  render() {
    const { tableHeader } = this.state;
    return (
      <>
        <h1>List Settled Battles</h1>
        <TableHeader header={tableHeader} settled />
        <TableSettledRow />
      </>
    );
  }
}

export default ListSettledBattles;
