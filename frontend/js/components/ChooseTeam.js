import { Field } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Typeahead, Menu, MenuItem } from 'react-bootstrap-typeahead';
import { connect } from 'react-redux';
import { sortableContainer, sortableElement, sortableHandle } from 'react-sortable-hoc';
import 'react-bootstrap-typeahead/css/Typeahead.css';
import styled from 'styled-components';

import { setPokemonList } from '../actions/setBattle';

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

const Container = styled.div`
  // display: grid;
  // grid-template-column: 1fr 1fr 1fr;
`;

const Error = styled.div`
  background-color: #f9ab2f;
  color: #fff;
  border-radius: 10px;
  border: 2px solid #f9ab2f;
  text-align: center;
  font-weight: 500;
  padding: 0.5rem;
`;

const DragHandle = sortableHandle(() => <span>::</span>);

const SortableItem = sortableElement(({ children }) => (
  <li>
    <DragHandle />
    {children}
  </li>
));

const SortableContainer = sortableContainer(({ children }) => {
  return <ul>{children}</ul>;
});

class ChooseTeam extends Component {
  componentDidMount() {
    const { setPokemonList } = this.props;
    setPokemonList();
  }

  render() {
    const { pokemon, setFieldValue, errors } = this.props;
    if (!pokemon) {
      return <div>Loading</div>;
    }
    const indexList = [1, 2, 3];
    return (
      <Container>
        {errors.team && <Error>{errors.team}</Error>}
        <SortableContainer useDragHandle>
          {indexList.map((value, index) => (
            <SortableItem key={`item-${value}`} index={index} value={value}>
              <Field name={`pokemon_${value}`}>
                {({ field }) => (
                  <>
                    {/* <label htmlFor={`pokemon_${index}`}>Opponent:</label> */}
                    <Typeahead
                      id={`pokemon-${value}-select`}
                      inputProps={{ required: true }}
                      labelKey="name"
                      maxHeight="150px"
                      options={pokemon}
                      placeholder="Choose a pokemon"
                      renderMenu={(results, menuProps) => (
                        <StyledMenu {...menuProps}>
                          {results.map((result, index) => (
                            <StyledItem key={result.id} option={result} position={index}>
                              {result.name}
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
            </SortableItem>
          ))}
        </SortableContainer>
      </Container>
    );
  }
}

ChooseTeam.propTypes = {
  setPokemonList: PropTypes.func,
  pokemon: PropTypes.array,
  setFieldValue: PropTypes.func,
  errors: PropTypes.object,
};

const mapStateToProps = (state) => ({
  pokemon: state.battles.pokemon,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setPokemonList: () => dispatch(setPokemonList()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ChooseTeam);
