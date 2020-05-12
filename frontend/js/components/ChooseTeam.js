import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { setPokemonList } from '../actions/setBattle';

class ChooseTeam extends Component {
  componentDidMount() {
    const { setPokemonList } = this.props;
    setPokemonList();
  }

  render() {
    const { pokemon } = this.props;
    return <div>{JSON.stringify(pokemon)}</div>;
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
