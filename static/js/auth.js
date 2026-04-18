let auth;
let provider;

async function initFirebase() {
    try {
        const res = await fetch('/api/config');
        const config = await res.json();

        firebase.initializeApp(config.firebase);
        auth = firebase.auth();
        provider = new firebase.auth.GoogleAuthProvider();

        const loginBtns = document.querySelectorAll("#loginBtn");
        const logoutBtns = document.querySelectorAll("#logoutBtn");
        const userNameDisplays = document.querySelectorAll("#userNameDisplay");

        // Login buttons
        loginBtns.forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                auth.signInWithPopup(provider);
            });
        });

        // Logout buttons
        logoutBtns.forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                auth.signOut();
            });
        });

        // 🔥 SINGLE AUTH LISTENER
       auth.onAuthStateChanged((user) => {
            const path = window.location.pathname;

            console.log("PATH:", path, "USER:", user);

            if (user) {
                console.log("Logged in");

                // 🔥 ALWAYS redirect if on login page
                if (path.includes("login") || path === "/") {
                    console.log("Redirecting to home...");
                    window.location.href = "/home";
                }

                // update UI (optional)
                const loginBtn = document.getElementById("loginBtn");
                const logoutBtn = document.getElementById("logoutBtn");
                const userNameDisplay = document.getElementById("userNameDisplay");

                if (loginBtn) loginBtn.style.display = "none";
                if (logoutBtn) logoutBtn.style.display = "inline-block";
                if (userNameDisplay) {
                    userNameDisplay.innerText = "Hello " + user.displayName;
                }

                return;
            }

            // not logged in
            if (!path.includes("login")) {
                window.location.href = "/login";
            }
        });

    } catch (err) {
        console.error("Firebase error:", err);
    }
}

document.addEventListener("DOMContentLoaded", initFirebase);