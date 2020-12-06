const sendFormData = () => {
  return fetch(`http://localhost:4443/?macroinvertebrates`)
    .then((response) => response.json())
    .then((result) => {
      return result;
    });
};

export { sendFormData };
