const Card = (props) => {
  const handleClick = (ev) => {
    props.sendClick(props.cardDetail.choice, ev.currentTarget.id);
  };

  return (
    <li className="card" id={props.cardDetail.id} onClick={handleClick}>
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
