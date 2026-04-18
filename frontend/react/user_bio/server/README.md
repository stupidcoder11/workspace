# User Bio - GraphQL Apollo Server (Backend)

A GraphQL API server built with **Apollo Server** for managing user biography data. This backend provides a REST-less GraphQL interface for creating, reading, and managing user information with real-time data synchronization.

## 📋 Project Overview

This is the **server-side** GraphQL API that the React frontend communicates with. It implements a complete Apollo GraphQL server with type definitions, resolvers, and sample data, allowing the frontend to query and mutate user data efficiently.

**Tech Stack:**

- **Apollo Server 5.5.0** - Production-ready GraphQL server
- **GraphQL 16.13.2** - Query language and type system
- **Node.js** - JavaScript runtime
- **ES Modules** - Modern JavaScript module system

---

## 📁 Folder Structure

```
server/
├── server.js              # Main Apollo Server entry point
├── schema.js              # GraphQL type definitions and schema
├── resolvers.js           # GraphQL resolver functions
├── dummyUsersData.js      # Sample user data
├── package.json           # Project dependencies and metadata
├── package-lock.json      # Locked dependency versions
├── node_modules/          # Installed dependencies
└── README.md              # This file
```

### File Descriptions

- **`server.js`** - Initializes and starts the Apollo GraphQL server
  - Configures Apollo Server instance
  - Sets up standalone server with port 4000
  - Includes startup logging

- **`schema.js`** - Defines GraphQL schema using type definitions
  - `User` type: Represents user entity with fields (id, name, age, isMarried)
  - `Query` type: Defines available queries (users)
  - `Mutation` type: Defines available mutations (createUser, deleteUser)

- **`resolvers.js`** - Implements resolver functions
  - Query resolvers: Fetch user data
  - Mutation resolvers: Create and delete users
  - Connects GraphQL operations to business logic

- **`dummyUsersData.js`** - In-memory data store with sample users
  - Contains initial user records
  - Used for development and testing

---

## 🚀 Prerequisites

Before setting up the project, ensure you have installed:

- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js) or **yarn/pnpm**
- **Git** (optional, for version control)

Verify your installation:

```bash
node --version
npm --version
```

---

## 🛠️ Setup Instructions

### 1. Navigate to Server Directory

```bash
cd frontend/react/user_bio/server
```

### 2. Install Dependencies

```bash
npm install
```

This installs the required packages:

- `@apollo/server@^5.5.0` - Apollo GraphQL server framework
- `graphql@^16.13.2` - GraphQL type system and utilities

### 3. Start the Server

```bash
node server.js
```

**Expected Output:**

```
🚀  Server ready at: http://localhost:4000/
```

The GraphQL server is now running and ready to accept requests.

### 4. Access GraphQL Playground

Open your browser and navigate to:

```
http://localhost:4000/
```

This will open the Apollo Sandbox (GraphQL IDE) where you can:

- Explore the schema
- Write and test queries
- Write and test mutations
- View real-time documentation

---

## 📜 Available Operations

### Queries

#### Get All Users

```graphql
query GetAllUsers {
  users {
    id
    name
    age
    isMarried
  }
}
```

**Response:**

```json
{
  "data": {
    "users": [
      {
        "id": "1",
        "name": "John Doe",
        "age": 30,
        "isMarried": true
      },
      {
        "id": "2",
        "name": "Jane Smith",
        "age": 25,
        "isMarried": false
      },
      {
        "id": "3",
        "name": "Alice Johnson",
        "age": 28,
        "isMarried": true
      }
    ]
  }
}
```

### Mutations

#### Create a New User

```graphql
mutation CreateNewUser {
  createUser(name: "Bob Wilson", age: 32, isMarried: true) {
    id
    name
    age
    isMarried
  }
}
```

**Response:**

```json
{
  "data": {
    "createUser": {
      "id": "4",
      "name": "Bob Wilson",
      "age": 32,
      "isMarried": true
    }
  }
}
```

#### Delete a User

```graphql
mutation DeleteUser {
  deleteUser(id: "2") {
    id
    name
    age
    isMarried
  }
}
```

**Response:**

```json
{
  "data": {
    "deleteUser": {
      "id": "2",
      "name": "Jane Smith",
      "age": 25,
      "isMarried": false
    }
  }
}
```

---

## 📊 GraphQL Schema

### Type Definitions

```graphql
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
```

### Field Descriptions

- **id**: Unique identifier for each user (non-nullable)
- **name**: User's full name (non-nullable, String)
- **age**: User's age (nullable, Integer)
- **isMarried**: Marital status (nullable, Boolean)

### Query Usage

- **users**: Retrieves all users in the system (always returns non-empty array)

### Mutation Usage

- **createUser**: Creates a new user with provided data
  - Required: `name`
  - Optional: `age`, `isMarried`
- **deleteUser**: Deletes a user by ID
  - Required: `id`
  - Returns deleted user data or error if not found

---

## 🏗️ Architecture

### Request/Response Flow

```
Frontend (React/Apollo Client)
    ↓
HTTP POST Request (GraphQL Query/Mutation)
    ↓
Apollo Server (Port 4000)
    ↓
Schema Validation
    ↓
Resolver Functions
    ↓
Data Processing (dummyUsersData.js)
    ↓
Response (JSON with GraphQL structure)
    ↓
Frontend (Apollo Cache Update + Re-render)
```

### Resolver Implementation

Resolvers are functions that resolve GraphQL fields to actual data:

```javascript
// Query Resolver
Query: {
  users: () => users; // Simply returns the users array
}

// Mutation Resolver
Mutation: {
  createUser: (_, args) => {
    // Create new user object
    // Add to array
    // Return created user
  };
}
```

---

## 💾 Data Management

### In-Memory Storage

The server uses an in-memory JavaScript array (`dummyUsersData.js`) to store user data. This means:

**Advantages:**

- ⚡ Fast data access
- 🚀 Zero database setup needed
- ✅ Perfect for development and testing
- 📚 Easy to understand and modify

**Limitations:**

- ❌ Data is lost when server stops
- ❌ Not suitable for production with multiple instances
- ❌ No persistent storage

### For Production

To persist data, upgrade to:

- **MongoDB** - NoSQL database
- **PostgreSQL** - Relational database
- **Firebase** - Cloud database
- **AWS DynamoDB** - Serverless database

---

## 🔧 Configuration

### Server Configuration (server.js)

```javascript
const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 }, // Change port here
});
```

**Change Port:**

```bash
# Edit server.js and modify:
listen: { port: 3001 }  // Use different port
```

### CORS Configuration

For production, configure CORS to allow requests from your frontend domain:

```javascript
await startStandaloneServer(server, {
  listen: { port: 4000 },
  context: async ({ req }) => ({ req }),
});
```

---

## 🚀 Running the Server

### Development Mode

```bash
# Terminal 1: Start the server
node server.js

# Server runs on http://localhost:4000

# Terminal 2 (Optional): Run frontend
cd ../client
npm run dev

# Frontend runs on http://localhost:5173
```

### With Auto-Restart (Using Nodemon)

For development with auto-restart on file changes:

```bash
# Install nodemon globally
npm install -g nodemon

# Run with nodemon
nodemon server.js

# Now the server restarts automatically when you edit files
```

---

## 🐛 Troubleshooting

### Port Already in Use

If port 4000 is already in use:

**Option 1:** Kill the process on port 4000

```bash
lsof -i :4000        # List process on port 4000
kill -9 <PID>        # Kill the process
```

**Option 2:** Use a different port
Edit `server.js`:

```javascript
listen: {
  port: 3001;
} // Use port 3001 instead
```

### CORS Errors

If the frontend can't connect to the backend:

```
Access to XMLHttpRequest at 'http://localhost:4000/'
from origin 'http://localhost:5173' has been blocked by CORS policy.
```

**Solution:** Add CORS headers to Apollo Server. Modify `server.js`:

```javascript
import cors from "cors";

// If using Express integration
app.use(
  cors({
    origin: "http://localhost:5173",
    credentials: true,
  }),
);
```

### Resolver Not Found

Check that resolvers are properly exported from `resolvers.js`:

```javascript
export const resolvers = {
  /* ... */
}; // ✅ Correct
const resolvers = {
  /* ... */
}; // ❌ Wrong (forgot export)
```

### Memory Issues

If server crashes or becomes slow:

```bash
# Restart the server
node server.js

# Check available memory
node --max-old-space-size=4096 server.js  # Allocate 4GB
```

---

## 📈 Extending the Server

### Add a New Query

**Step 1:** Update schema in `schema.js`

```javascript
type Query {
  users: [User!]!
  user(id: ID!): User  # New query
}
```

**Step 2:** Implement resolver in `resolvers.js`

```javascript
Query: {
  users: () => users,
  user: (_, args) => users.find(u => u.id === args.id),  # New resolver
}
```

### Add a New Field to User Type

**Step 1:** Update schema

```javascript
type User {
  id: ID!
  name: String!
  age: Int!
  isMarried: Boolean
  email: String  # New field
}
```

**Step 2:** Update dummy data

```javascript
const users = [
  {
    id: "1",
    name: "John Doe",
    age: 30,
    isMarried: true,
    email: "john@example.com",
  },
];
```

---

## 📚 Resources

- [Apollo Server Documentation](https://www.apollographql.com/docs/apollo-server/)
- [GraphQL Documentation](https://graphql.org/)
- [GraphQL Best Practices](https://graphql.org/learn/best-practices/)
- [Apollo Sandbox Docs](https://www.apollographql.com/docs/apollo-server/testing/apollo-sandbox/)

---

## 🚀 Deployment

### Deploy to Heroku

```bash
# Install Heroku CLI
brew install heroku

# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main
```

### Deploy to Vercel

```bash
npm install -g vercel
vercel
```

### Deploy to AWS Lambda

Use AWS Amplify or Serverless Framework to deploy as serverless GraphQL API.

### Deploy with Docker

**Dockerfile:**

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 4000
CMD ["node", "server.js"]
```

Build and run:

```bash
docker build -t user-bio-server .
docker run -p 4000:4000 user-bio-server
```

---

## 📝 Adding NPM Scripts

To make development easier, update `package.json`:

```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "node --test"
  }
}
```

Then run:

```bash
npm start     # Production start
npm run dev   # Development with auto-restart
npm test      # Run tests
```

---

## 📄 License

This project is open source and available under the ISC license.

---

## ✨ Next Steps

1. **Explore the Schema** - Open Apollo Sandbox and test queries/mutations
2. **Extend Data Model** - Add more fields to the User type
3. **Connect Database** - Replace in-memory data with a real database
4. **Add Authentication** - Implement JWT or API key authentication
5. **Write Tests** - Add unit tests for resolvers
6. **Deploy** - Deploy to production environment

---

## 🤝 Integration with Frontend

This server works with the React frontend located in `../client/`.

**To run both together:**

```bash
# Terminal 1: Start server
cd server
node server.js

# Terminal 2: Start client
cd ../client
npm run dev
```

Visit `http://localhost:5173` to see the frontend interact with this GraphQL server.

For frontend setup, see [../client/README.md](../client/README.md).
