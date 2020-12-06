import FormInput from "./FormInput";

const Form = (props) => {
  // console.log(props.formData);
  const input = Object.keys(props.formData).map((m) => {
    return (
      <FormInput
        name={m}
        index={props.formData[m].index}
        id={props.formData[m].id}
        key={props.formData[m].id}
      />
    );
  });

  const preventSubmit = (ev) => {
    ev.preventDefault();
  };

  return (
    <>
      <form>
        {input}
        <input type="submit" value="Calcular" onSubmit={preventSubmit} />
      </form>
    </>
  );
};

export default Form;
