import { gql } from "@apollo/client";
import { USER_FIELDS } from "./fragments.js";

export const CREATE_USER = gql`
  mutation CREATE_USER($name: String!, $age: Int!, $isMarried: Boolean!) {
    createUser(name: $name, age: $age, isMarried: $isMarried) {
      ...UserFields
    }
  }
  ${USER_FIELDS}
`;

export const DELETE_USER = gql`
  mutation DELETE_USER($id: ID!) {
    deleteUser(id: $id) {
      ...UserFields
    }
  }
  ${USER_FIELDS}
`;
