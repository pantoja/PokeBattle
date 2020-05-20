import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Typeahead, Menu, MenuItem } from 'react-bootstrap-typeahead';
import { connect } from 'react-redux';
import styled from 'styled-components';

import { fetchPokemonList } from '../actions/setBattle';
import { setTeamField } from '../actions/setForm';

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

class TypeaheadField extends Component {
  componentDidMount() {
    const { fetchPokemonList } = this.props;
    fetchPokemonList();
  }

  render() {
    const { pokemon, index, setTeamField } = this.props;
    if (!pokemon) return <>Loading</>;
    return (
      <Typeahead
        id={`pokemon_${index}`}
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
            const field = {
              index,
              pokemon: selected[0].id,
            };
            setTeamField(field);
          }
        }}
      />
    );
  }
}

TypeaheadField.propTypes = {
  pokemon: PropTypes.array,
  errors: PropTypes.object,
  field: PropTypes.object,
  fetchPokemonList: PropTypes.func,
  setTeamField: PropTypes.func,
  setFieldValue: PropTypes.func,
  value: PropTypes.number,
  index: PropTypes.number,
};

const mapStateToProps = (state) => ({
  pokemon: state.battles.pokemon,
});

const mapDispatchToProps = (dispatch) => {
  return {
    fetchPokemonList: () => dispatch(fetchPokemonList()),
    setTeamField: (field) => dispatch(setTeamField(field)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TypeaheadField);
