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
    <section className="container">
      <h2 className="fs-3 my-4">Cálculo Índice IBMWP</h2>
      <form className="row g-2 mt-3">{input}</form>
      <button className="btn btn-dark btn-lg my-4 px-5" onClick={handleSubmit}>
        Calcular
      </button>
      <p>Índice: {props.indexSum}</p>
      <p>Calidad: {props.quality}</p>
    </section>
  );
};

export default Form;
