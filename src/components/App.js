import React from "react";
import { useEffect, useState } from "react";
import { Route, Switch } from "react-router-dom";
import { sendKeyData } from "../services/keyFetch";
import { sendFormData } from "../services/formFetch";

import "../stylesheet/App.scss";
import Header from "./Header/Header";
import Key from "./Key/Key";
import Form from "./Form/Form";
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
  const [quality, setQuality] = useState();

  // Startup
  useEffect(() => {
    setLoad(true);
    sendKeyData(question, answer).then((result) => {
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
  const handleKeyClick = (id, description) => {
    setAnswer(id);
    setQuestion(cardData.choice);
    setHistory([
      ...history,
      { question: cardData.choice, answer: id, description: description },
    ]);
  };

  // Key Reset
  const handleKeyReset = () => {
    setQuestion(0);
    setAnswer(0);
    setHistory([]);
  };

  // Key History
  const handlekeyHistory = (qu, ans) => {
    setQuestion(qu);
    setAnswer(ans);
  };

  // Form Index Calculation
  const handleFormInput = (inputName, inputValue) => {
    const macroInvModified = formData.find((m) => {
      return m.name === inputName;
    });

    if (macroInvModified) {
      const result = macroInvModified.index * inputValue;
      const foundValue = formValues.find((m) => {
        return m.name === inputName;
      });

      if (foundValue) {
        foundValue.indexResult = result;
        formValues.indexResult = result;
        setFormValues([...formValues]);
      } else {
        setFormValues([
          ...formValues,
          { name: inputName, indexResult: result },
        ]);
      }
    }
  };

  const handleFormSubmit = () => {
    let sum;
    console.log(formValues);
    if (formValues.length === 0) {
      sum = "Error";
    } else {
      sum = formValues.reduce((acc, index) => {
        return acc + parseInt(index.indexResult);
      }, 0);
    }
    setIndexSum(sum);

    if (sum > 100) {
      setQuality("Muy buena");
    } else if (sum <= 100 && sum > 60) {
      setQuality("Aceptable");
    } else if (sum <= 60 && sum > 35) {
      setQuality("Dudosa");
    } else if (sum <= 35 && sum > 15) {
      setQuality("Crítica");
    } else if (sum <= 15) {
      setQuality("Muy crítica");
    } else {
      setQuality("Error");
    }
  };

  // Return
  return (
    <>
      <Header />
      <main className="container">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/key">
            <Key
              history={history}
              cardData={cardData}
              load={load}
              sendHistory={handlekeyHistory}
              sendClick={handleKeyClick}
              sendReset={handleKeyReset}
            />
          </Route>
          <Route path="/form">
            <Form
              formData={formData}
              indexSum={indexSum}
              quality={quality}
              sendSubmit={handleFormSubmit}
              sendInput={handleFormInput}
            />
          </Route>
        </Switch>
      </main>
    </>
  );
};

export default App;
