const form = document.getElementById("login-form");
const dashboard = document.getElementById("dashboard");
const tasks = document.getElementById("tasks");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const res = await fetch("http://localhost:8000/token", {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: new URLSearchParams({username: email, password})
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.detail);

        localStorage.setItem("token", data.access_token);
        form.style.display = "none";
        dashboard.style.display = "block";
        loadDashboard();

    } catch (err) {
        document.getElementById("error").textContent = err.message;
    }
});

async function loadDashboard() {
    const token = localStorage.getItem("token");

    const res = await fetch("http://localhost:8000/dashboard/", {
        headers: {Authorization: `Bearer ${token}`}
    });

    const data = await res.json();

    tasks.innerHTML = `
        <li>Total Tasks: ${data.total_tasks}</li>
        <li>Overdue Tasks: ${data.overdue_tasks}</li>
    `;
}

function logout() {
    localStorage.removeItem("token");
    location.reload();
}