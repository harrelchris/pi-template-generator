function generate_template() {
    let template = {}
    return JSON.stringify(template);
}

const form = document.getElementById("form");

form.onsubmit = function(e) {
  e.preventDefault();

  const output = generate_template();

  navigator.clipboard.writeText(output)
      .then(() => {
          console.log("Template copied to clipboard")
      })
      .catch((error) => {
          console.error(error)
      });
};
