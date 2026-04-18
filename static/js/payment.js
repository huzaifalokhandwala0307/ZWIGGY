function completePayment() {
    let cart = JSON.parse(localStorage.getItem("cart") || "[]");

    fetch("/place-order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            items: cart,
            status: "paid"
        })
    })
    .then(res => res.json())
    .then(() => {
        alert("Payment successful!");
        localStorage.removeItem("cart");
        window.location.href = "/home";
    });
}
