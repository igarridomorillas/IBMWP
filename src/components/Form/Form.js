import FormInput from "./FormInput";

const Form = (props) => {
  let formData = props.formData;

  const sortedData = Object.keys(formData).sort((a, b) => {
    return formData[a] - formData[b];
  });

  sortedData.map((n) => formData[n]);
  console.log(formData);

  const input = Object.keys(formData).map((m) => {
    return (
      <FormInput
        name={m}
        index={formData[m].index}
        id={formData[m].id}
        key={formData[m].id}
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
      <p>Calidad: {props.quality}</p>
    </>
  );
};

export default Form;
