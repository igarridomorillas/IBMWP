const Card = (props) => {
  const handleClick = (ev) => {
    props.sendClick(ev.currentTarget.id, props.cardDetail.next);
  };

  return (
    <li
      className="card"
      id={props.cardDetail.id}
      name={props.cardDetail.next}
      onClick={handleClick}
    >
      <p className="card__description">{props.cardDetail.description}</p>
      <img
        src="https://via.placeholder.com/210x295/808080/ffffff/?text=Bicho"
        alt=""
        className="card__img"
      />
    </li>
  );
};

export default Card;
