
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


// Add Item
  $(document).on("click", "#add-button", function (e) {
    e.preventDefault();
    var addToCartUrl = '{% url "cart:cart_add" %}';
    console.log(addToCartUrl)
    var itemid = $(this).val();
    var itemqty = $("#qty").val();
    console.log(itemid, itemqty)
    $.ajax({
      type: "POST",
      url: addToCartUrl,
      data: {
        itemid: itemid,
        itemqty: itemqty,  
        csrfmiddlewaretoken: "{{ csrf_token }}",
        action: "post",
      },
      success: function (json) {
        if (json) { 
          document.getElementById("cart-qty").innerHTML = json.qty;
          console.log("Товар успішно додано у кошик");
        } else {
          console.log("Помилка: товар не було додано у кошик");
        }
      },
      error: function (xhr, errmsg, err) {
        console.log("Помилка: не вдалося відправити запит на сервер");
      },
    });
  });


  // Update Item
  $(document).on("click", ".update-button", function (e) {
    e.preventDefault();
    var prodid = $(this).data("index");
    console.log(prodid);
    var itemQty = $("#qty-" + prodid).val();
    console.log("Item Quantity:", itemQty);
    $.ajax({
      type: "POST",
      url: '{% url "cart:cart_update" %}',
      data: {
        itemid: prodid,
        itemqty: itemQty,
        csrfmiddlewaretoken: "{{csrf_token}}",
        action: "post",
      },
      success: function (json) {
        console.log("Success:", json);
        document.getElementById("cart-qty").innerHTML = json.qty;
        document.getElementById("subtotal").innerHTML = json.subtotal;
      },
      error: function (xhr, errmsg, err) {
        console.log("Error:", errmsg);
      },
    });
  });


   // Delete Item
  $(document).on('click', '.delete-button', function (e) {
    e.preventDefault();
    var prodid = $(this).data("index");
    console.log("id", prodid)
    $.ajax({
      type: 'POST',
      url: '{% url "cart:cart_delete" %}',
      data: {
       itemid: $(this).data('index'),
        csrfmiddlewaretoken: "{{csrf_token}}",
        action: 'post'
      },
      success: function (json) {
        $('.this-item[data-index="' + prodid + '"]').remove();
        document.getElementById("cart-qty").innerHTML = json.qty
        document.getElementById("subtotal").innerHTML = json.subtotal;
        
      },
      error: function (xhr, errmsg, err) {}
    });
  })