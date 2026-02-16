async function check_login(){
  let res = await fetch("http://127.0.0.1:5000/check_login", {
    credentials: "include"
  });
  let data = await res.text();
  if(data=="OK"){
    alert("User is logged in");
  }
  else{
    alert("Please login first");
    window.location.href = "index.html";
  }
}
check_login();

async function logout(){
  let res = await fetch("http://127.0.0.1:5000/logout",{
    credentials: "include"
  });
  let data = await res.text();
  alert(data);
  window.location.href = "index.html";

}