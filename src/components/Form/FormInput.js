const FormInput = (props) => {
  const handleInput = (ev) => {
    props.sendInput(ev.target.name, ev.target.value);
  };

  return (
    <div class="col-auto">
      <label className="col form-label" htmlFor={props.id}>
        {props.name}
      </label>
      <input
        className="col form-control"
        type="number"
        name={props.name}
        id={props.id}
        onChange={handleInput}
      />
    </div>
  );
};

export default FormInput;
