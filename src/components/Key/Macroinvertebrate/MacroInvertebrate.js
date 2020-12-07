const Macroinvertebrate = (props) => {
  return (
    <section className="col-10 mt-4">
      <article id={props.cardData.id}>
        <h2 className="text-capitalize">{props.cardData.name}</h2>
        <img
          src="https://via.placeholder.com/210x295/808080/ffffff/?text=Bicho"
          alt=""
          className="card__img"
        />
        <p>{props.cardData.description}</p>
        <p>Índice IBMWP: {props.cardData.index}</p>
        <p>Tolerancia: {props.cardData.tolerance}</p>
      </article>
    </section>
  );
};

export default Macroinvertebrate;
