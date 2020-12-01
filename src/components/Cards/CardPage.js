const { default: Card } = require("./Card");

const CardPage = (props) => {
  let card = "";
  for (let index in props.cardData.cards) {
    const element = props.cardData.cards[index];
    card = <Card cardDetail={element} />;
  }

  return (
    <section className="card-page">
      <h2 className="card-page__title">{props.cardData.option}</h2>
      <ul className="card-page__cards">
        {/* {cardData} */}
        {card}
        {/* <Card
          description="Con concha"
          cardData={props.cardData.cards[1]}
          sendClick={props.sendClick}
        />
        <Card
          description="Sin concha"
          cardData={props.cardData.cards[2]}
          sendClick={props.sendClick}
        /> */}
      </ul>
    </section>
  );
};

export default CardPage;
