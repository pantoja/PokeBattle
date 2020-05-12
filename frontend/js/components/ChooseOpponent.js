import { Formik, Field, Form } from 'formik';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { setUserList } from '../actions/setBattle';
import { postBattleAPI } from '../utils/services';

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
      <Formik
        initialValues={{
          opponent: '',
        }}
        onSubmit={(fields) => {
          const data = {
            user_opponent: fields.opponent,
          };
          postBattleAPI(data);
        }}
      >
        {() => (
          <Form>
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
            <input type="submit" value="Go!" />
          </Form>
        )}
      </Formik>
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
