const Card = (props) => {
  return (
    <div className="card">
      <p className="card__description">{props.description}</p>
      <img
        src="https://via.placeholder.com/210x295/808080/ffffff/?text=Bicho"
        alt=""
        className="card__img"
      />
    </div>
  );
};

export default Card;
