document.querySelectorAll(".favorite-btn").forEach((button) => {
  button.addEventListener("click", async () => {
    const product_id = button.getAttribute("data-product-id");
    const icon = button.querySelector("i");

    const response = await fetch("/accounts/toggle-favorite", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({ product_id }),
    });

    if (response.ok) {
      const data = await response.json();

      if (data.is_favorite) {
        icon.classList.remove("fa-regular");
        icon.classList.add("fa-solid", "text-yellow-400");
      } else {
        icon.classList.remove("fa-solid", "text-yellow-400");
        icon.classList.add("fa-regular");

        // If on favorites page, remove the card
        if (window.location.pathname.includes("/favorites")) {
          button.closest(".group")?.remove();
        }
      }
    } else {
      alert("Error toggling favorite. Please try again.");
    }
  });
});

// CSRF helper
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
