import FormInput from "./FormInput";

const Form = (props) => {
  const formData = props.formData;

  // Sort
  formData.sort((a, b) => {
    const macroInvA = a.name.toUpperCase();
    const macroInvB = b.name.toUpperCase();
    if (macroInvA < macroInvB) {
      return -1;
    }
    if (macroInvA > macroInvB) {
      return 1;
    }
    return 0;
  });

  // Map
  const input = formData.map((m) => {
    return (
      <FormInput
        name={m.name}
        index={m.index}
        id={m.id}
        key={m.id}
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
