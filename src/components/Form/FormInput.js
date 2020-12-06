const FormInput = (props) => {
  return (
    <>
      <label htmlFor={props.id}>{props.name}</label>
      <input type="number" name={props.name} id={props.id} />
    </>
  );
};

export default FormInput;
