async function pay() {
    try {
        const res = await fetch("/place-order", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                item: "sample food",
                price: 200,
                status: "paid"
            })
        });

        const data = await res.json();
        alert(data.message);

    } catch (err) {
        console.error(err);
        alert("Failed to place order");
    }
}
