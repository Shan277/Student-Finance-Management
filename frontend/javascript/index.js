function showForm(id) {
  let activeForm = document.querySelector('.active');
  activeForm.classList.remove('active');
  let newform = document.getElementById(id);
  newform.classList.add('active');
}

async function login(){
  let formData = new FormData(document.getElementById("loginForm")); //create a FormData object from the login form to easily extract form data
  let username = formData.get("username").trim(); //get the username from the form data and trim any whitespace
  let password = formData.get("password").trim(); //get the password from the form data and trim any whitespace
      if(username === "" || password === ""){
        alert("Please fill all the fields");
        return;
      }
  console.log(formData.get("username"));
  console.log(formData.get("password"));
  let res = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    body : formData,
    credentials: "include"
})
  let data = await res.text();
  alert(data);
  if(data === "Login Successful"){
      window.location.href = "dashboard.html";
  }
}



async function register() {
  let username = document.getElementById("reg-username").value;
  let password = document.getElementById("reg-password").value;
  let email = document.getElementById("reg-email").value;

  if(username.trim() === "" || password.trim() === "" || email.trim() === ""){
    alert("Please fill all the fields");
    return;
  }
  
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
    }),

    credentials: "include" //include credentials (cookies) in the request to maintain session

  })//return response object and we need to extract the text from it


  let data = await res.text();//get the response as text as res is response object and we need to extract the text from it
  alert(data);//show the response in an alert box

  
  if(data === "Registered Successful"){  //if registration is successful, then redirect to dashboard

      window.location.href = "dashboard.html";
      
  }
}

async function checkLogin(){
  let res = await fetch("http://127.0.0.1:5000/check_login",{
    credentials: "include"
  });
  let data = await res.text();
  if (data === "OK"){
    alert("User already logged in");
    window.location.href = "dashboard.html";
  }
}
checkLogin();


