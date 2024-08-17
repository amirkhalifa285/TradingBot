const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const app = express();

app.use(cors());

app.get('/api/fvg', (req, res) => {
    const python = spawn('python', ['visualize_fvg.py']);

    let dataString = '';

    python.stdout.on('data', (data) => {
        dataString += data.toString();
    });

    python.stdout.on('end', () => {
        try {
            const jsonData = JSON.parse(dataString.trim());  // Remove any extra whitespace
            res.json(jsonData);
        } catch (error) {
            console.error('Failed to parse JSON:', error);
            console.error('Python Output:', dataString);  // Log the raw output for debugging
            res.status(500).send('Error processing request');
        }
    });

    python.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
        if (!res.headersSent) {
            res.status(500).send('Error processing request');
        }
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
