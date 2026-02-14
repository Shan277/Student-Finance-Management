function showForm(id) {
  let activeForm = document.querySelector('.active');
  activeForm.classList.remove('active');
  document.getElementById(id).classList.add('active');
}