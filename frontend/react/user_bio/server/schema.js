export const typeDefs = `
  type User {
    id: ID!
    name: String!
    age: Int!
    isMarried: Boolean
  }

  type Query {
    users: [User!]!
  }

  type Mutation {
    createUser(name: String!, age: Int, isMarried: Boolean): User!
    deleteUser(id: ID!): User
  }
`;
