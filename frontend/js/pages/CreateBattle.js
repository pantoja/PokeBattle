import React from 'react';
import styled from 'styled-components';

import ChooseTeam from '../components/ChooseTeam';

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

const CreateBattle = () => {
  return (
    <Page>
      <h2>Create a battle</h2>
      {/* <ChooseOpponent /> */}
      <ChooseTeam />
      <Tag>OR</Tag>
      <InviteButton href="/invite/">Invite a friend!</InviteButton>
    </Page>
  );
};

export default CreateBattle;
