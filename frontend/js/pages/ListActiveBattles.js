import React, { Component } from 'react';

import TableActiveRow from '../components/TableActiveRow';
import TableHeader from '../components/TableHeader';
import { getActiveBattlesAPI } from '../utils/services';

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
      battles: [],
    };
  }

  componentDidMount() {
    getActiveBattlesAPI().then((battlesData) => {
      return this.setState({ battles: battlesData });
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
