const Card = (props) => {
  const handleClick = (ev) => {
    props.sendClick(ev.currentTarget.id, props.cardDetail.description);
  };

  return (
    <li
      className="col-3 bg-secondary bg-gradient rounded pointer shadow text-center py-3 mx-3"
      id={props.cardDetail.id}
      onClick={handleClick}
    >
      <p className="pb-2">{props.cardDetail.description}</p>
      <img
        src="https://via.placeholder.com/180x295/ffffff/000000/?text=Bicho"
        alt=""
        className=""
      />
    </li>
  );
};

export default Card;
