import { Field } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
// import { SortableContainer, SortableElement } from 'react-sortable-hoc';

import { setPokemonList } from '../actions/setBattle';

class ChooseTeam extends Component {
  componentDidMount() {
    const { setPokemonList } = this.props;
    setPokemonList();
  }

  render() {
    const { pokemon } = this.props;
    if (!pokemon) {
      return <div>Loading</div>;
    }
    return (
      <>
        <Field as="select" name="pokemon_1" required>
          {pokemon.map((pokemon) => (
            <option key={pokemon.id} value={pokemon.id}>
              {pokemon.name}
            </option>
          ))}
        </Field>
        <Field as="select" name="pokemon_2" required>
          {pokemon.map((pokemon) => (
            <option key={pokemon.id} value={pokemon.id}>
              {pokemon.name}
            </option>
          ))}
        </Field>
        <Field as="select" name="pokemon_3" required>
          {pokemon.map((pokemon) => (
            <option key={pokemon.id} value={pokemon.id}>
              {pokemon.name}
            </option>
          ))}
        </Field>
      </>
    );
  }
}

ChooseTeam.propTypes = {
  setPokemonList: PropTypes.func,
  pokemon: PropTypes.array,
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
