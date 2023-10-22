// Get references to the modal and close button
var modal = document.getElementById("myModal");
var closeModal = document.getElementById("closeModal");

// Get reference to the "?" button
var questionButton = document.querySelector(".question-button");

// Function to open the modal
questionButton.addEventListener("click", function() {
  modal.style.display = "block";
});

// Function to close the modal
closeModal.addEventListener("click", function() {
  modal.style.display = "none";
});

// Close the modal if the user clicks outside of it
window.addEventListener("click", function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
});