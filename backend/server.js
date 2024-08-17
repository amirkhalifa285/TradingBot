const express = require('express');
const { spawn } = require('child_process');
const app = express();

// Endpoint to fetch FVG data
app.get('/api/fvg', (req, res) => {
    const python = spawn('python', ['../visualize_fvg.py']);  // Adjust the path if needed

    python.stdout.on('data', (data) => {
        res.json(JSON.parse(data));
    });

    python.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
        res.status(500).send('Error processing request');
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server running on port 3000');
});
