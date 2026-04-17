import { useMutation, useQuery } from "@apollo/client/react";
import "./App.css";
import { GET_USERS_BIO } from "../gql/queries";
import { CREATE_USER, DELETE_USER } from "../gql/mutations";

function App() {
  const {
    loading: fetchingUsers,
    error: fetchingUsersError,
    data: usersData,
  } = useQuery(GET_USERS_BIO);

  const [createUser] = useMutation(CREATE_USER);
  const [deleteUser] = useMutation(DELETE_USER);

  const handleCreateUser = async () => {
    try {
      await createUser({
        variables: {
          name: "Donnie Darko",
          age: 30,
          isMarried: false,
        },
        refetchQueries: [{ query: GET_USERS_BIO }],
      });
    } catch (error) {
      console.error("Error creating user:", error);
    }
  };

  const handleDeleteUser = async () => {
    try {
      await deleteUser({
        variables: { id: 2 },
        refetchQueries: [{ query: GET_USERS_BIO }],
      });
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  };

  if (fetchingUsers) {
    return (
      <section id="center">
        <p
          style={{
            border: "4px solid #f3f3f3",
            borderTop: "4px solid #3498db",
            borderRadius: "50%",
            width: "40px",
            height: "40px",
            animation: "spin 1s linear infinite",
          }}
        ></p>
      </section>
    );
  }

  if (fetchingUsersError) {
    return (
      <section id="center">
        <p>Error: {fetchingUsersError.message}</p>
      </section>
    );
  }

  return (
    <>
      <section className="hero">
        <h1>User Bio Application</h1>
        <p>
          This is a simple application to demonstrate how to fetch and display
          user bios using GraphQL and React.
        </p>
      </section>
      <section id="center">
        <section id="actions">
          <h2>Actions</h2>
          <hr />
          <p>Here you can perform various operations related to user bios.</p>
          <div className="action-buttons">
            <button className="action-btn" onClick={handleCreateUser}>
              Add User
            </button>
            <button className="action-btn" onClick={handleDeleteUser}>
              Delete User
            </button>
          </div>
        </section>
        <section id="users">
          <h2>User List</h2>
          <hr />
          <div id="users-list">
            {usersData?.users?.map((user) => (
              <div key={user.id} className="user-card">
                <p>Name: {user.name}</p>
                <p>Age: {user.age}</p>
                <p>Married: {user.isMarried ? "Yes" : "No"}</p>
              </div>
            ))}
          </div>
        </section>
      </section>
    </>
  );
}

export default App;
