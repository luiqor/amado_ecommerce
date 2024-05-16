function updatePage() {
    location.reload();
};


function adjustQuantity(itemId, change) {
    let effect = document.getElementById('qty-' + itemId);
    let qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        let newQty = qty + change;
        if (newQty >= 1) {
            effect.value = newQty;
        };
    };
};


function increaseQuantityConcret(itemId) {
    adjustQuantity(itemId, 1);
};


function decreaseQuantityConcret(itemId) {
    adjustQuantity(itemId, -1);
};


function updateQuantityConcret(itemId) {
    let effect = document.getElementById('qty-' + itemId);
    let qty = parseInt(effect.value);
    if (!isNaN(qty)) {
        console.log("Нове значення для елемента з id", itemId + ":", qty);
    };
};
