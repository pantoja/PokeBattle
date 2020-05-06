import React, { Component } from 'react';

import TableHeader from '../components/TableHeader';
import TableSettledRow from '../components/TableSettledRow';
import { getSettledBattlesAPI } from '../utils/services';

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
      battles: [],
    };
  }

  async componentDidMount() {
    getSettledBattlesAPI().then((battlesData) => {
      return this.setState({ battles: battlesData });
    });
  }

  render() {
    const { battles, tableHeader } = this.state;
    return (
      <>
        <h1>List Settled Battles</h1>
        <TableHeader header={tableHeader} settled />
        <TableSettledRow battles={battles} />
      </>
    );
  }
}

export default ListSettledBattles;
