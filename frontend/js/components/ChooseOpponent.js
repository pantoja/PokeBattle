import { Field } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { setUserList } from '../actions/setBattle';

class ChooseOpponent extends Component {
  componentDidMount() {
    const { setUserList } = this.props;
    setUserList();
  }

  render() {
    const { users } = this.props;
    if (!users) {
      return <>Loading</>;
    }

    return (
      <Field as="select" name="opponent" required>
        <option disabled value="">
          -------
        </option>
        {users.map((user) => (
          <option key={user.id} value={user.id}>
            {user.email}
          </option>
        ))}
      </Field>
    );
  }
}

ChooseOpponent.propTypes = {
  setUserList: PropTypes.func,
  users: PropTypes.array,
};

const mapStateToProps = (state) => ({
  users: state.battles.users,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setUserList: () => dispatch(setUserList()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ChooseOpponent);
