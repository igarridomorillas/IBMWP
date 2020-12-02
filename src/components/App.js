import React from "react";
import { useEffect, useState } from "react";
import "../stylesheet/App.scss";
import Header from "./Header/Header";
// import Form from "./Form/Form";
import CardPage from "./Cards/CardPage";
import { sendData } from "../services/fetch";
import KeyHistory from "./KeyHistory/KeyHistory";

const App = () => {
  // State
  const [question, setQuestion] = useState(0);
  const [answer, setAnswer] = useState(0);
  const [cardData, setCardData] = useState({});
  const [load, setLoad] = useState(true);
  const [history, setHistory] = useState([]);

  // Startup
  useEffect(() => {
    setLoad(true);
    sendData(question, answer).then((result) => {
      setCardData(result);
      setLoad(false);
    });
  }, [answer]);

  // Key Card choice
  const handleClick = (id, description) => {
    setAnswer(id);
    setQuestion(cardData.choice);
    setHistory([
      ...history,
      { question: cardData.choice, answer: id, description: description },
    ]);
  };

  // Key Reset
  const handleReset = () => {
    setQuestion(0);
    setAnswer(0);
    setHistory([]);
  };

  // Key History
  const handleHistory = (qu, ans) => {
    setQuestion(qu);
    setAnswer(ans);
  };

  return (
    <>
      <Header />
      <main className="main">
        {load === true ? (
          "Waiting..."
        ) : (
          <>
            <KeyHistory history={history} sendHistory={handleHistory} />
            <CardPage
              cardData={cardData}
              load={load}
              sendClick={handleClick}
              sendReset={handleReset}
            />
          </>
        )}

        {/* <Form /> */}
      </main>
    </>
  );
};

export default App;
