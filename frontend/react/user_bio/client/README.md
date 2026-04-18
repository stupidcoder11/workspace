# User Bio - React Frontend

A modern React application built with **Vite** and **Apollo Client** for seamless GraphQL integration. This project demonstrates a full-stack user biography management system with a GraphQL API backend.

## 📋 Project Overview

This is the **client-side** application that communicates with a GraphQL Apollo Server backend. It provides a responsive UI for managing and displaying user biographies in real-time using GraphQL queries and mutations.

**Tech Stack:**

- **React 19.2.4** - UI library
- **Vite 8.0.4** - Fast build tool and dev server
- **Apollo Client 4.1.7** - GraphQL client with caching
- **GraphQL 16.13.2** - Query language
- **ESLint** - Code quality and style enforcement

---

## 📁 Folder Structure

```
client/
├── public/                      # Static assets (favicon, etc.)
├── src/
│   ├── assets/                 # Images, icons, and other media
│   ├── App.jsx                 # Main application component
│   ├── App.css                 # Global application styles
│   ├── main.jsx               # Entry point
│   ├── index.css              # Global styles
│   └── gql/                   # GraphQL operations
│       ├── fragments.js        # GraphQL reusable fragments
│       ├── mutations.js        # GraphQL mutation operations
│       ├── queries.js          # GraphQL query operations
│       └── typeDefs.js         # Local GraphQL type definitions
├── index.html                  # HTML template
├── vite.config.js             # Vite configuration
├── eslint.config.js           # ESLint configuration
├── package.json               # Project dependencies and scripts
└── README.md                  # This file
```

### Key Directories Explained

- **`src/gql/`** - Contains all GraphQL operations:
  - `queries.js` - GraphQL queries for fetching user data
  - `mutations.js` - GraphQL mutations for creating/updating users
  - `fragments.js` - Reusable GraphQL fragments for data selection
  - `typeDefs.js` - Local schema definitions for Apollo Client

- **`src/assets/`** - Static files like images and icons

- **`public/`** - Assets served directly without bundling

---

## 🚀 Prerequisites

Before setting up the project, ensure you have:

- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js) or **yarn/pnpm**
- **Git** (for version control)

Check your versions:

```bash
node --version
npm --version
```

---

## 🛠️ Setup Instructions

### 1. Clone or Navigate to the Project

```bash
cd frontend/react/user_bio/client
```

### 2. Install Dependencies

```bash
npm install
```

This will install all required packages listed in `package.json`:

- React and React DOM
- Apollo Client for GraphQL
- Vite and its plugins
- ESLint for code quality

### 3. Setup Backend (Apollo Server)

Before running the frontend, you need to start the GraphQL server:

```bash
cd ../server
npm install
node server.js
```

The server will typically run on `http://localhost:4000`

### 4. Configure Client Connection (if needed)

Update the Apollo Client configuration to point to your GraphQL endpoint. Check `src/gql/` or `App.jsx` for the server URL configuration.

### 5. Start Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:5173` (default Vite port).

---

## 📜 Available Scripts

### Development

```bash
npm run dev
```

Starts the Vite development server with Hot Module Replacement (HMR). Changes are reflected instantly in the browser.

### Production Build

```bash
npm run build
```

Creates an optimized production bundle in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

Locally preview the production build before deployment.

### Linting

```bash
npm run lint
```

Runs ESLint to check for code quality issues and style violations.

---

## 🏗️ Project Architecture

### Frontend (This Project)

- **React Components** - Reusable UI components
- **Apollo Client** - Manages GraphQL queries, mutations, and caching
- **Vite** - Ultra-fast build tool with hot module replacement

### Backend Integration

The frontend communicates with the Apollo GraphQL Server located in the `../server/` directory:

- **Apollo Server** - GraphQL API endpoint
- **Express.js** - HTTP server framework
- **GraphQL Schema** - Defines available queries and mutations

### Data Flow

```
React Component → Apollo Client → GraphQL Query/Mutation
    ↓
Apollo Server → Resolvers → Data Processing
    ↓
Response → Apollo Cache → Component Re-render
```

---

## 📝 GraphQL Operations

### Writing Queries

Queries are defined in `src/gql/queries.js`:

```javascript
import gql from "graphql-tag";

export const GET_USER = gql`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      bio
    }
  }
`;
```

### Writing Mutations

Mutations are defined in `src/gql/mutations.js`:

```javascript
export const CREATE_USER = gql`
  mutation CreateUser($input: UserInput!) {
    createUser(input: $input) {
      id
      name
      bio
    }
  }
`;
```

### Using in Components

```javascript
import { useQuery, useMutation } from "@apollo/client";
import { GET_USER, CREATE_USER } from "./gql/queries";

function UserComponent() {
  const { data, loading } = useQuery(GET_USER);
  const [createUser] = useMutation(CREATE_USER);

  // Component logic
}
```

---

## 🔧 Configuration Files

### `vite.config.js`

Configures Vite build tool with React plugin for JSX support and Hot Module Replacement.

### `eslint.config.js`

Enforces code style and quality standards:

- React best practices
- React hooks rules
- React refresh plugin compatibility

### `package.json`

Manages dependencies and defines npm scripts for development, building, and linting.

---

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

### Deploy

The `dist/` folder contains the production-ready files. Deploy to:

- **Vercel** - Optimized for Vite apps
- **Netlify** - Simple git integration
- **AWS S3 + CloudFront** - Scalable static hosting
- **Docker** - Containerized deployment

Example Vercel deployment:

```bash
npm install -g vercel
vercel
```

---

## 🐛 Troubleshooting

### Port Already in Use

If port 5173 is already in use:

```bash
npm run dev -- --port 3000
```

### Apollo Client Connection Issues

- Verify the backend server is running on `http://localhost:4000`
- Check network tab in browser DevTools for GraphQL requests
- Ensure CORS is properly configured on the backend

### Build Errors

Clear cache and reinstall:

```bash
rm -rf node_modules dist
npm install
npm run build
```

---

## 📚 Resources

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [Apollo Client Documentation](https://www.apollographql.com/docs/react/)
- [GraphQL Documentation](https://graphql.org/learn/)

---

## 📄 License

This project is open source and available under the ISC license.

---

## ✨ Next Steps

1. Explore the GraphQL operations in `src/gql/`
2. Review component structure in `src/`
3. Check the backend server implementation in `../server/`
4. Start building features and components!

For questions or issues, refer to the troubleshooting section or check the official documentation links above.
