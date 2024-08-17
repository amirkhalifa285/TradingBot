document.addEventListener("DOMContentLoaded", function() {
    const imgElement = document.getElementById('fvg-chart');
    
    // Fetch the image from the backend
    fetch('http://localhost:3000/api/fvg')
        .then(response => {
            if (response.ok) {
                return response.blob();  // Convert to blob if it's an image
            } else {
                throw new Error('Failed to load image');
            }
        })
        .then(blob => {
            const imgUrl = URL.createObjectURL(blob);
            imgElement.src = imgUrl;
        })
        .catch(error => {
            console.error('Error fetching the chart:', error);
            imgElement.alt = 'Failed to load chart';
        });
});
