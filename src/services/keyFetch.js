const sendKeyData = (question, answer) => {
  return fetch(`http://localhost:4443/?qu=${question}&ans=${answer}`)
    .then((response) => response.json())
    .then((result) => {
      return result;
    });
};

export { sendKeyData };
