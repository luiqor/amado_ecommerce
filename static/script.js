function updatePage() {
    location.reload(); 
}


function increaseQuantity() {
    var effect = document.getElementById('qty');
    var qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        effect.value = qty + 1;
        updateQuantity();
    }
}


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
}


function adjustQuantity(itemId, change) {
    var effect = document.getElementById('qty-' + itemId);
    var qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        var newQty = qty + change;
        if (newQty >= 1) {
            effect.value = newQty;
        }
    }
}


function increaseQuantityConcret(itemId) {
    adjustQuantity(itemId, 1);
}


function decreaseQuantityConcret(itemId) {
    adjustQuantity(itemId, -1);
}


function updateQuantityConcret(itemId) {
    var effect = document.getElementById('qty-' + itemId);
    var qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        console.log("Нове значення для елемента з id", itemId + ":", qty);
    }
}

