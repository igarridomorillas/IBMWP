import React from "react";
import "../stylesheet/App.scss";
import CardPage from "./Cards/CardPage";
import Header from "./Header/Header";

const App = (props) => {
  return (
    <>
      <Header />
      <main className="main">
        <CardPage />
      </main>
    </>
  );
};

export default App;
