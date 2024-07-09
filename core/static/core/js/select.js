const input = document.getElementById('my-input');
const select = document.getElementById('my-select');
const options = select.getElementsByTagName('option');
const miInput = document.getElementById("miInput");

input.addEventListener('input', () => {
    const searchTerm = input.value.toLowerCase();
    for (let i = 0; i < options.length; i++) {
    const option = options[i];
    const text = option.text.toLowerCase();
    const match = text.includes(searchTerm);
    option.style.display = match ? '' : 'none';
    }
});

select.addEventListener("change", function () {
    if (select.value === "input") {
    miInput.style.display = "block";
    } else {
    miInput.style.display = "none";
    }
});


