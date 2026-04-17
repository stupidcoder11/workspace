import { gql } from "@apollo/client";
import { USER_FIELDS } from "./fragments.js";

export const GET_USERS_BIO = gql`
  query GET_USERS_BIO {
    users {
      id
      ...UserFields
    }
  }
  ${USER_FIELDS}
`;
