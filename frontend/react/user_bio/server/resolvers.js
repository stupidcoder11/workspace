import { users } from "./dummyUsersData.js";

export const resolvers = {
  Query: {
    users: () => users,
  },
  Mutation: {
    createUser: (_, args) => {
      const newUser = {
        id: users.length + 1, // Simple ID generation
        name: args.name,
        age: args.age,
        isMarried: args.isMarried,
      };
      users.push(newUser);
      return newUser;
    },
    deleteUser: (_, args) => {
      const userIndex = users.findIndex((user) => user.id === args.id);
      if (userIndex === -1) {
        throw new Error("User not found");
      }
      const deletedUser = users[userIndex];
      users.splice(userIndex, 1);
      return deletedUser;
    },
  },
};
