function searchBlogs() {
    var input, filter, cards, card, title, i, txtValue;
    input = document.getElementById("form1"); // Use the ID of your search input
    filter = input.value.toUpperCase();
    cards = document.getElementsByClassName("col-sm-4");

    for (i = 0; i < cards.length; i++) {
        card = cards[i];
        title = card.querySelector(".card-text");
        txtValue = title.textContent || title.innerText;

        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    }
}