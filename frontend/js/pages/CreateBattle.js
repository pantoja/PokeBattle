import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

import { setUserList } from '../actions/setUser';

const Page = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
`;

const Tag = styled.span`
  font-weight: 700;
  margin: 20px 0;
`;
const InviteButton = styled.a`
  position: relative;
  background-color: white;
  border-radius: 20px;
  padding: 5px 10px;
  font-weight: 500;
  :before {
    background: linear-gradient(
      145deg,
      #a2eef9 14%,
      #98ccff 28%,
      #d0b9f0 42%,
      #fecbfe 56%,
      #ccf998 70%,
      #ccf9e9 84%
    );
    border-radius: inherit;
    bottom: 0;
    content: '';
    left: 0;
    margin: -2px;
    position: absolute;
    right: 0;
    top: 0;
    z-index: -1;
  }
`;
class CreateBattle extends Component {
  componentDidMount() {
    const { setUserList } = this.props;
    setUserList();
  }

  render() {
    const { users } = this.props;
    return (
      <Page>
        <h2>Choose your opponent</h2>
        <select name="opponent" required>
          {users.map((user) => (
            <option key={user.id} value={user.id}>
              {user.email}
            </option>
          ))}
        </select>
        <Tag>OR</Tag>
        <InviteButton href="/invite/">Invite a friend!</InviteButton>
      </Page>
    );
  }
}

CreateBattle.propTypes = {
  setUserList: PropTypes.func,
  users: PropTypes.array,
};

const mapStateToProps = (state) => ({
  users: state.session.users,
});

const mapDispatchToProps = (dispatch) => {
  return {
    setUserList: () => dispatch(setUserList()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(CreateBattle);
