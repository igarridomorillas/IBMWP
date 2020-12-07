const KeyHistory = (props) => {
  const handleReset = () => {
    props.sendReset();
  };

  const handleHistory = (ev) => {
    const ans = ev.currentTarget.id;
    const qu = props.history.find((item) => {
      return item.answer === ans;
    });
    props.sendHistory(qu.question, ans);
  };

  const history = props.history.map((item, index) => {
    return (
      <li
        className="pointer bg-light p-1 rounded"
        key={index}
        id={item.answer}
        onClick={handleHistory}
      >
        {index + 1}. {item.description}
      </li>
    );
  });

  return (
    <section className="col-2 bg-dark rounded">
      <button className="btn btn-success my-4 px-5" onClick={handleReset}>
        Reiniciar
      </button>
      <h3 className="fs-5 text-white mb-3">Historial:</h3>
      <nav>
        <ul>{history}</ul>
      </nav>
    </section>
  );
};

export default KeyHistory;
