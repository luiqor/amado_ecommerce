let slider1 = document.getElementById("min_price");
let slider2 = document.getElementById("max_price");
let range_price = document.getElementById("range_price");
let min_price_input = document.getElementById("min_price_input");
let max_price_input = document.getElementById("max_price_input");

function updateSlider() {
    if(parseInt(slider1.value) > parseInt(slider2.value)){
        let tmp = slider2.value;
        slider2.value = slider1.value;
        slider1.value = tmp;
    }
    range_price.innerHTML = slider1.value + "₴ - " + slider2.value + "₴";
    min_price_input.value = slider1.value;
    max_price_input.value = slider2.value;
}

slider1.oninput = function() {
    updateSlider();
}

slider2.oninput = function() {
    updateSlider();
}

updateSlider();