const FormInput = (props) => {
  const handleInput = (ev) => {
    props.sendInput(ev.target.name, ev.target.value);
  };

  return (
    <>
      <label htmlFor={props.id}>{props.name}</label>
      <input
        type="number"
        name={props.name}
        id={props.id}
        onChange={handleInput}
      />
    </>
  );
};

export default FormInput;
