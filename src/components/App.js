import React from "react";
import { useEffect, useState } from "react";
import "../stylesheet/App.scss";
import Header from "./Header/Header";
import Form from "./Form/Form";
import CardPage from "./Cards/CardPage";
import { sendData } from "../services/fetch";

const App = () => {
  const [question, setQuestion] = useState(0);
  const [answer, setAnswer] = useState(0);

  useEffect(() => {
    sendData(question, answer).then((result) => {
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
