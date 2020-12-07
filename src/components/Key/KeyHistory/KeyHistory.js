const KeyHistory = (props) => {
  const handleHistory = (ev) => {
    const ans = ev.currentTarget.id;
    const qu = props.history.find((item) => {
      return item.answer === ans;
    });
    props.sendHistory(qu.question, ans);
  };

  const history = props.history.map((item, index) => {
    return (
      <li key={index} id={item.answer} onClick={handleHistory}>
        {index + 1}: {item.description}
      </li>
    );
  });

  return (
    <section className="history">
      <h3>History:</h3>
      <nav>
        <ul>{history}</ul>
      </nav>
    </section>
  );
};

export default KeyHistory;
