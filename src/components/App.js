import React from "react";
import { useEffect, useState } from "react";
import "../stylesheet/App.scss";
import Header from "./Header/Header";
import Form from "./Form/Form";
import CardPage from "./Cards/CardPage";
import { sendData } from "../services/fetch";

const App = () => {
  useEffect(() => {
    sendData(1, 4).then((result) => {
      console.log(result);
    });
  });
  return (
    <>
      <Header />
      <main className="main">
        <CardPage />
        {/* <Form /> */}
      </main>
    </>
  );
};

export default App;
