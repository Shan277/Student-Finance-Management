function showForm(id) {
  let activeForm = document.querySelector('.active');
  activeForm.classList.remove('active');
  let newform = document.getElementById(id);
  newform.classList.add('active');
}

async function register() {

  let username = document.getElementById("reg-username").value;
  let password = document.getElementById("reg-password").value;
  let email = document.getElementById("reg-email").value;

  console.log("USERNAME:", username);
  console.log("PASSWORD:", password);
  console.log("EMAIL:", email);

  let res = await fetch("http://127.0.0.1:5000/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      username: username,
      password: password,
      email: email
    })
  })//return response object and we need to extract the text from it
  let data = await res.text();//get the response as text as res is response object and we need to extract the text from it
  alert(data);//show the response in an alert box
}