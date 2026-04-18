let cart = [];

function addToCart(name, price) {
    cart.push({ name, price });
    console.log(cart);
    alert(name + " added to cart");
}

function goToPayment() {
    const cart = JSON.parse(localStorage.getItem("cart") || "[]");
    if (!cart || cart.length === 0) {
        alert("Cart is empty!");
        return;
    }

    window.location.href = "/payment";
}
