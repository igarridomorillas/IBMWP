import React from "react";
import "../stylesheet/App.scss";
// import CardPage from "./Cards/CardPage";
import Header from "./Header/Header";
import Form from "./Form/Form";

const App = (props) => {
  return (
    <>
      <Header />
      <main className="main">
        {/* <CardPage /> */}
        <Form />
      </main>
    </>
  );
};

export default App;
