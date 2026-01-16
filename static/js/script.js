document.addEventListener("DOMContentLoaded", () => {
  const textarea = document.getElementById("dream_text");
  const placeholder = document.querySelector(".custom-placeholder");
  const button = document.getElementById("analyzeBtn");

  // Fade placeholder on input
  textarea.addEventListener("input", () => {
    placeholder.classList.toggle("hidden", textarea.value.length > 0);
  });

  // Change button text on submit (no animation nonsense)
  document.getElementById("dreamform").addEventListener("submit", () => {
    button.textContent = "stepping through the threshold...";
    button.classList.add("fading");
  });
});
