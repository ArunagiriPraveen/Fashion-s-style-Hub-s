// add_to_card
const cartButtons = document.querySelectorAll(".cart");
const cartDisplay = document.getElementById("cart-count");

cartButtons.forEach((button) => {
    button.addEventListener("click", function () {

        const productCard = this.closest(".card");
        const productName = productCard.querySelector("h5").innerText;
        const productPrice = productCard.querySelector("b").innerText;

        // CONFIRM before adding
        const confirmAdd = confirm(
            `🛒 Add this product?\n\n${productName}\n${productPrice}`
        );

        if (confirmAdd) {
            cartCount++;
            cartDisplay.innerText = cartCount;

            alert(`✅ ${productName} added to cart!`);
        } else {
            alert("❌ Item not added.");
        }
    });
});

// search icon
document.querySelector(".icon li:nth-child(1)").addEventListener("click", function () {
    let searchItem = prompt("🔍 What are you looking for?");

    if (searchItem) {
        alert(`Searching for "${searchItem}"... 🚀`);
    }
});

//cart
// document.getElementById("cart-icon").addEventListener("click", function () {

//     if (cartCount === 0) {
//         alert("🛒 Your cart is empty!");
//     } else {
//         alert(`🛍️ ${userName}, you have ${cartCount} items in your cart.`);
//     }
// });

let cart = JSON.parse(localStorage.getItem("cart")) || [];

document.querySelectorAll(".cart").forEach(btn => {
    btn.addEventListener("click", function () {

        const card = this.closest(".card");
        const name = card.querySelector("h5").innerText;
        const priceText = card.querySelector("b").innerText;
        const price = parseInt(priceText.replace(/[^0-9]/g, ""));

        const existing = cart.find(item => item.name === name);

        if (existing) {
            existing.quantity++;
        } else {
            cart.push({ name, price, quantity: 1 });
        }

        localStorage.setItem("cart", JSON.stringify(cart));

        alert("Added to cart ✅");
    });
});