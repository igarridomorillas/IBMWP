import KeyHistory from "./KeyHistory/KeyHistory";
import CardPage from "./Cards/CardPage";

const Key = (props) => {
  return (
    <main className="main">
      {props.load === true ? (
        "Waiting..."
      ) : (
        <>
          <KeyHistory history={props.history} sendHistory={props.sendHistory} />
          <CardPage
            cardData={props.cardData}
            load={props.load}
            sendClick={props.sendClick}
            sendReset={props.sendReset}
          />
        </>
      )}
    </main>
  );
};

export default Key;
