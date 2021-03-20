function validateForm() {
    var x = document.forms["signupform"]["email"].value;
    if (x == "" || x==null) {
      alert("Please type your email!");
      return false;
    }
  }