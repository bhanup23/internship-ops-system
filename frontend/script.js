const API = "https://internship-ops-backend-production.up.railway.app/";

function login() {
  document.getElementById("msg").innerText = "Login demo (backend auth can be added)";
  window.location.href = "dashboard.html";
}

function addIntern() {
  fetch(`${API}/intern`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: document.getElementById("internName").value,
      department: document.getElementById("department").value
    })
  }).then(() => alert("Intern added"));
}

function addTask() {
  fetch(`${API}/task`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: document.getElementById("taskTitle").value,
      intern_id: Number(document.getElementById("internId").value)
    })
  }).then(() => alert("Task assigned"));
}
