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

function ToggleDarkMode() {
    // Toggle the dark mode status
    dark_mode_active = !dark_mode_active;
  
    // Get the container element to apply the background color class
    var body = document.body;
    var heading = document.getElementById("main-heading");
    // Check if dark mode is active and update the class accordingly
    if (dark_mode_active) {
      console.log("dark mode active")
      body.classList.add('bg-dark');
      document.body.style.color = 'white'; // Set text color to white
      heading.style.color = 'black'; // Set text color to white
    } else {
      console.log("light mode active")
      body.classList.remove('bg-dark');
      document.body.style.color = ''; // Reset text color to default (black or as defined in your CSS)
    }
  }
  document.getElementById('dark').addEventListener('click', ToggleDarkMode);