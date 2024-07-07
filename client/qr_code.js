const form = document.getElementById('qr-code-form');
const qrCodeContainer = document.getElementById('qr-code-container');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Get form data (optional)
  const data = document.getElementById('data').value;

  // Create a new FormData object (optional, if sending data)
  const formData = new FormData();
  if (data) {
    formData.append('data', data);
  }

  // Show loading indicator (optional)
  qrCodeContainer.innerHTML = '<p>Generating QR Code...</p>';

  fetch('/user/lecturer/generate-qr-code', {
    method: 'POST',
    body: formData || null  // Send FormData or null if no data
  })
  .then(response => response.json())
  .then(data => {
    if (data.qr_code_image) {
      const img = document.createElement('img');
      img.src = data.qr_code_image;
      qrCodeContainer.innerHTML = '';  // Clear container before adding image
      qrCodeContainer.appendChild(img);
    } else {
      console.error('Error generating QR code');
      // Display user-friendly error message in UI (optional)
      qrCodeContainer.innerHTML = '<p>Error: Failed to generate QR code.</p>';
    }
  })
  .catch(error => {
    console.error(error);
    // Display user-friendly error message in UI
    qrCodeContainer.innerHTML = '<p>Error: An error occurred.</p>';
  })
  .finally(() => {
    // Hide loading indicator (optional)
    qrCodeContainer.innerHTML = '';
  });
});
