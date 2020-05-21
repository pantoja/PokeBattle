import arrayMove from 'array-move';
import { Field } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { sortableContainer, sortableElement, sortableHandle } from 'react-sortable-hoc';
import 'react-bootstrap-typeahead/css/Typeahead.css';
import styled from 'styled-components';

import TeamTypeaheadField from './TeamTypeaheadField';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  border-top: 1px solid #e0e0e0;
`;

const Handle = styled.span`
  font-weight: 700;
  padding-right: 20px;
  color: #909090;
`;

const List = styled.ul`
  background-color: #f3f3f3;
  border-radius: 3px;
  outline: none;
  list-style: none;
  padding: 0;
  width: 100%;
`;

const Item = styled.li`
  display: flex;
  align-items: center;
  height: 60px;
  padding: 0 20px;
  background-color: #fff;
  border-bottom: 1px solid #efefef;
  box-sizing: border-box;
  color: #333;
  font-weight: 500;
  border-radius: 5px;
`;

const Label = styled.span`
  align-self: start;
  font-size: 0.8rem;
  padding-left: 20px;
  margin-top: 10px;
`;

const DragHandle = sortableHandle(() => <Handle>☰</Handle>);

const SortableItem = sortableElement(({ children }) => (
  <Item>
    <DragHandle />
    {children}
  </Item>
));

const SortableContainer = sortableContainer(({ children }) => {
  return <List>{children}</List>;
});

class ChooseTeam extends Component {
  constructor(props) {
    super(props);
    this.state = {
      indexList: [1, 2, 3],
    };
    this.onSortEnd = this.onSortEnd.bind(this);
  }

  componentDidMount() {
    const { setFieldValue } = this.props;
    const { indexList } = this.state;
    setFieldValue('order', indexList);
  }

  onSortEnd({ oldIndex, newIndex }) {
    const { setFieldValue } = this.props;
    const { indexList } = this.state;
    const order = arrayMove(indexList, oldIndex, newIndex);
    setFieldValue('order', order);
    this.setState(() => ({
      indexList: order,
    }));
  }

  render() {
    const { indexList } = this.state;

    return (
      <Container>
        <Label>Team:</Label>
        <SortableContainer onSortEnd={this.onSortEnd}>
          {indexList.map((value, index) => (
            <SortableItem key={`item-${value}`} index={index} value={value}>
              <Field name={`pokemon_${value}`}>
                {() => <TeamTypeaheadField {...this.props} index={index + 1} />}
              </Field>
            </SortableItem>
          ))}
        </SortableContainer>
      </Container>
    );
  }
}

ChooseTeam.propTypes = {
  setFieldValue: PropTypes.func,
  errors: PropTypes.object,
};

export default ChooseTeam;
