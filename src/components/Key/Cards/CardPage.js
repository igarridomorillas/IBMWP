import Macroinvertebrate from "../Macroinvertebrate/MacroInvertebrate";

const { default: Card } = require("./Card");

const CardPage = (props) => {
  // Card Map
  let card;
  if (props.cardData.cards === undefined) {
    return (
      <Macroinvertebrate
        cardData={props.cardData}
        sendReset={props.sendReset}
      />
    );
  } else {
    card = Object.keys(props.cardData.cards).map((key) => {
      return (
        <Card
          key={key}
          cardDetail={props.cardData.cards[key]}
          sendClick={props.sendClick}
        />
      );
    });
  }

  // Return
  return (
    <section className="col-10 text-center">
      <h2 className="py-4 fs-4">{props.cardData.option}</h2>
      <ul className="row justify-content-center">{card}</ul>
    </section>
  );
};

export default CardPage;
