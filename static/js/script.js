console.log('Script loaded correctly')

// Total Calculation Script
    const eventSelect = document.getElementById('event');
    const ticketSelect = document.getElementById('tickets');
    const totalDisplay = document.getElementById('total');

    function updateTotal() {
      const price = parseFloat(eventSelect.selectedOptions[0].getAttribute('data-price')) || 0;
      const quantity = parseInt(ticketSelect.value) || 1;
      const total = price * quantity;
      totalDisplay.textContent = `£${total.toFixed(2)}`;
    }

    eventSelect.addEventListener('change', updateTotal);
    ticketSelect.addEventListener('change', updateTotal);

    