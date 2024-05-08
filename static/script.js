// Increase and Decrease Quantity
function increaseQuantity() {
    var effect = document.getElementById('qty');
    var qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        effect.value = qty + 1;
        updateQuantity();
    }
}


// Decrease Quantity
function decreaseQuantity() {
    var effect = document.getElementById('qty');
    var qty = parseInt(effect.value);
    if (!isNaN(qty) && qty > 1) {
        effect.value = qty - 1;
        updateQuantity();
    }
}

function updateQuantity() {
    var effect = document.getElementById('qty');
    var qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        console.log("Нове значення:", qty);
    }
}

