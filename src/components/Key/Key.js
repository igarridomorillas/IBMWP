import KeyHistory from "./KeyHistory/KeyHistory";
import CardPage from "./Cards/CardPage";
import { Spinner } from "react-bootstrap";

const Key = (props) => {
  return (
    <section className="container my-3">
      <h2 className="fs-3 my-4">Clave Dicotómica</h2>
      <div className="row">
        <KeyHistory
          history={props.history}
          sendHistory={props.sendHistory}
          sendReset={props.sendReset}
        />
        {props.load === true ? (
          <div className="text-center">
            <Spinner
              animation="border"
              role="status"
              variant="success"
            ></Spinner>
            <span className="mx-4">Loading...</span>
          </div>
        ) : (
          <CardPage
            cardData={props.cardData}
            load={props.load}
            sendClick={props.sendClick}
          />
        )}
      </div>
    </section>
  );
};

export default Key;
