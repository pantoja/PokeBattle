import { Field } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Typeahead, Menu, MenuItem } from 'react-bootstrap-typeahead';
import { connect } from 'react-redux';
import styled from 'styled-components';

import { fetchUserList } from '../actions/setBattle';

const Container = styled.div`
  margin-top: 5vh;
  margin-bottom: 8vh;
`;

const StyledMenu = styled(Menu)`
  z-index: 1000;
  float: left;
  min-width: 10rem;
  padding: 0.5rem 0;
  margin: 0.125rem 0 0;
  font-size: 1rem;
  color: #212529;
  text-align: left;
  list-style: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 0.25rem;
  .active {
    background-color: #e2e2e2;
  }
`;

const StyledItem = styled(MenuItem)`
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  padding: 0.25rem 1.5rem;
  clear: both;
  font-weight: 400;
  color: #212529;
  text-align: inherit;
  white-space: nowrap;
  background-color: transparent;
  border: 0;
`;

class ChooseOpponent extends Component {
  componentDidMount() {
    const { fetchUserList } = this.props;
    fetchUserList();
  }

  render() {
    const { users, setFieldValue } = this.props;
    if (!users) {
      return <>Loading</>;
    }

    return (
      <Container>
        <Field name="opponent">
          {({ field }) => (
            <>
              {/* <label htmlFor="opponent">Opponent:</label> */}
              <Typeahead
                id="opponent"
                inputProps={{ required: true }}
                labelKey="email"
                maxHeight="150px"
                options={users}
                placeholder="Choose your opponent"
                renderMenu={(results, menuProps) => (
                  <StyledMenu {...menuProps}>
                    {results.map((result, index) => (
                      <StyledItem key={result.id} option={result} position={index}>
                        {result.email}
                      </StyledItem>
                    ))}
                  </StyledMenu>
                )}
                onChange={(selected) => {
                  if (selected[0]) {
                    setFieldValue(field.name, selected[0].id);
                  }
                }}
              />
            </>
          )}
        </Field>
      </Container>
    );
  }
}

ChooseOpponent.propTypes = {
  fetchUserList: PropTypes.func,
  users: PropTypes.array,
  setFieldValue: PropTypes.func,
};

const mapStateToProps = (state) => ({
  users: state.battles.users,
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchUserList: () => dispatch(fetchUserList()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ChooseOpponent);
