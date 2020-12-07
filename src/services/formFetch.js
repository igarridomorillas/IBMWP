const sendFormData = () => {
  return fetch(`http://localhost:4443/?macroinvertebrates`)
    .then((response) => response.json())
    .then((result) => {
      Object.keys(result).map((m) => {
        delete result[m].description;
        delete result[m].tolerance;
        return result;
      });

      const macroInv = Object.values(result);
      return macroInv;
    });
};

export { sendFormData };
