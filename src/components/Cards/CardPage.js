import Macroinvertebrate from "../Macroinvertebrate/MacroInvertebrate";

const { default: Card } = require("./Card");

const CardPage = (props) => {
  // Reset button
  const handleReset = () => {
    props.sendReset();
  };

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

  return (
    <section className="card-page">
      <button onClick={handleReset}>Reiniciar</button>
      <h2 className="card-page__title">{props.cardData.option}</h2>
      <ul className="card-page__cards">{card}</ul>
    </section>
  );
};

export default CardPage;
