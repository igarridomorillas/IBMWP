import React from "react";
import { useEffect, useState } from "react";
import "../stylesheet/App.scss";
import Header from "./Header/Header";
// import Form from "./Form/Form";
import CardPage from "./Cards/CardPage";
import { sendData } from "../services/fetch";

const App = () => {
  const [question] = useState(0);
  const [answer, setAnswer] = useState(0);
  const [cardData, setCardData] = useState({
    option: "",
    cards: {
      1: { id: "", description: "", image: "", next: "" },
      2: { id: "", description: "", image: "", next: "" },
    },
  });
  const [load, setLoad] = useState(true);

  useEffect(() => {
    setLoad(true);
    sendData(question, answer).then((result) => {
      setCardData(result);
      setLoad(false);
    });
  }, [answer]);

  const handleClick = (id) => {
    console.log(id);
    setAnswer(id);
  };

  return (
    <>
      <Header />
      <main className="main">
        {load === true ? (
          "Waiting..."
        ) : (
          <CardPage cardData={cardData} load={load} sendClick={handleClick} />
        )}

        {/* <Form /> */}
      </main>
    </>
  );
};

export default App;
