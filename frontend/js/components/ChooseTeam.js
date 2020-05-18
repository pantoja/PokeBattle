import { Field } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Typeahead } from 'react-bootstrap-typeahead';
import { connect } from 'react-redux';
// import { SortableContainer, SortableElement } from 'react-sortable-hoc';
import 'react-bootstrap-typeahead/css/Typeahead.css';

import { setPokemonList } from '../actions/setBattle';

class ChooseTeam extends Component {
  componentDidMount() {
    const { setPokemonList } = this.props;
    setPokemonList();
  }

  render() {
    const { pokemon, setFieldValue } = this.props;
    if (!pokemon) {
      return <div>Loading</div>;
    }
    const indexList = [1, 2, 3];

    return indexList.map((index) => (
      <Field key={index} name={`pokemon_${index}`}>
        {({ field }) => (
          <Typeahead
            id={`pokemon-${index}-select`}
            labelKey="name"
            maxHeight="150px"
            options={pokemon}
            placeholder="Choose a pokemon"
            onChange={(selected) => {
              if (selected[0]) {
                setFieldValue(field.name, selected[0].id);
              }
            }}
          />
        )}
      </Field>
    ));
  }
}

ChooseTeam.propTypes = {
  setPokemonList: PropTypes.func,
  pokemon: PropTypes.array,
  setFieldValue: PropTypes.func,
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
