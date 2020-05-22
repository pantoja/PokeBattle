import React, { Component } from 'react';

import TableActiveRows from '../components/TableActiveRows';
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

  render() {
    const { tableHeader } = this.state;
    return (
      <>
        <h1>List Active Battles</h1>
        <TableHeader header={tableHeader} />
        <TableActiveRows />
      </>
    );
  }
}

export default ListActiveBattles;
