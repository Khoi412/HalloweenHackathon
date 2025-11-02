console.log("Script loaded correctly");

document.addEventListener("DOMContentLoaded", () => {
  const scare1 = document.getElementById("scare1");
  const scare2 = document.getElementById("scare2");

  window.addEventListener("scroll", () => {
    const scrollY = window.scrollY;
    const windowHeight = window.innerHeight;
    const docHeight = document.body.scrollHeight;

    // --- Scare 1 logic ---
    if (scare1) {
      if (scrollY > windowHeight * 1.2 && scrollY < windowHeight * 1.9) {
        scare1.style.opacity = "1";
        scare1.style.zIndex = "-999";
      } else {
        scare1.style.opacity = "0";
        scare1.style.zIndex = "-1";
      }
    }

  });
});


// Total Calculation Script
const eventSelect = document.getElementById("event");
const ticketSelect = document.getElementById("tickets");
const totalDisplay = document.getElementById("total");

function updateTotal() {
  const price =
    parseFloat(eventSelect.selectedOptions[0].getAttribute("data-price")) || 0;
  const quantity = parseInt(ticketSelect.value) || 1;
  const total = price * quantity;
  totalDisplay.textContent = `£${total.toFixed(2)}`;
}

eventSelect.addEventListener("change", updateTotal);
ticketSelect.addEventListener("change", updateTotal);

// Shows Overlay
document.addEventListener("DOMContentLoaded", function () {
  const paymentButton = document.getElementById("start-payment");

  paymentButton.addEventListener("click", function () {
    document.getElementById("loading-overlay").style.display = "block";

    setTimeout(function () {
      document.getElementById("loading-overlay").style.display = "none";

      alert("Payment successful!");
    }, 3000);
  });
});
