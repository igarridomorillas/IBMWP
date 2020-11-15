const { default: Card } = require("./Card");

const CardPage = (props) => {
  return (
    <div className="card-page">
      <h2 className="card-page__title">Opción</h2>
      <div className="card-page__cards">
        <Card description="Con concha" />
        <Card description="Sin concha" />
      </div>
    </div>
  );
};

export default CardPage;
