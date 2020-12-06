import React from "react";
import { useEffect, useState } from "react";
import { Route, Switch } from "react-router-dom";
import { sendData } from "../services/fetch";
import { sendFormData } from "../services/formFetch";

import "../stylesheet/App.scss";
import Header from "./Header/Header";
import Menu from "./Menu/Menu";
import Form from "./Form/Form";
import CardPage from "./Cards/CardPage";
import KeyHistory from "./KeyHistory/KeyHistory";
import Home from "./Home/Home";

const App = () => {
  // State
  const [question, setQuestion] = useState(0);
  const [answer, setAnswer] = useState(0);
  const [cardData, setCardData] = useState({});
  const [load, setLoad] = useState(true);
  const [history, setHistory] = useState([]);
  const [formData, setFormData] = useState([]);
  const [formValues, setFormValues] = useState([]);
  const [indexSum, setIndexSum] = useState();

  // Startup
  useEffect(() => {
    setLoad(true);
    sendData(question, answer).then((result) => {
      setCardData(result);
      setLoad(false);
    });
  }, [answer]);

  useEffect(() => {
    setLoad(true);
    sendFormData().then((result) => {
      setFormData(result);
      setLoad(false);
    });
  }, []);

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

  // Index Calculation
  const handleInput = (inputName, inputValue) => {
    console.log(inputName);
    let inputCalc;
    if (isNaN(parseInt(inputValue))) {
      inputCalc = 0;
    } else {
      inputCalc = formData[inputName].index * parseInt(inputValue);
    }
    setFormValues([...formValues, inputCalc]);
  };

  const handleSubmit = () => {
    let sum;
    console.log(formValues);
    if (formValues.length === 0) {
      sum = "Error";
    } else {
      sum = formValues.reduce((acc, index) => acc + index);
    }
    setIndexSum(sum);
  };

  return (
    <>
      <Header />
      <Menu />
      <main className="main">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/key">
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
          </Route>
          <Route path="/form">
            <Form
              formData={formData}
              sendInput={handleInput}
              sendSubmit={handleSubmit}
              indexSum={indexSum}
            />
          </Route>
        </Switch>
      </main>
    </>
  );
};

export default App;
