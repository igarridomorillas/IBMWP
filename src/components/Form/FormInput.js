const FormInput = (props) => {
  const handleInput = (ev) => {
    props.sendInput(ev.target.name, ev.target.value);
  };

  return (
    <div class="col-3 my-3">
      <label className="form-label text-capitalize" htmlFor={props.id}>
        {props.name}
      </label>
      <input
        className="form-control"
        type="number"
        name={props.name}
        id={props.id}
        placeholder="..."
        onChange={handleInput}
      />
    </div>
  );
};

export default FormInput;
