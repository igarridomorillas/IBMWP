import FormInput from "./FormInput";

const Form = (props) => {
  const input = Object.keys(props.formData).map((m) => {
    return (
      <FormInput
        name={m}
        index={props.formData[m].index}
        id={props.formData[m].id}
        key={props.formData[m].id}
        sendInput={props.sendInput}
      />
    );
  });

  // Submit
  const handleSubmit = (ev) => {
    props.sendSubmit();
    ev.preventDefault();
  };

  // Return
  return (
    <>
      <form>
        {input}
        <input type="submit" value="Calcular" onClick={handleSubmit} />
      </form>
      <p>Índice: {props.indexSum}</p>
    </>
  );
};

export default Form;
