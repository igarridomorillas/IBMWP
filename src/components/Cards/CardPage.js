const { default: Card } = require("./Card");

const CardPage = (props) => {
  const card = Object.keys(props.cardData.cards).map((key) => {
    return (
      <Card
        key={key}
        cardDetail={props.cardData.cards[key]}
        sendClick={props.sendClick}
      />
    );
  });

  return (
    <section className="card-page">
      <h2 className="card-page__title">{props.cardData.option}</h2>
      <ul className="card-page__cards">{card}</ul>
    </section>
  );
};

export default CardPage;
