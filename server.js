const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;

//MongoDB connection

mongoose.connect(process.env.MONGODB_URI, {usenewUrlParser: true, useUnifiedTopology: true})
	.then(() => console.log('MongoDB connected'))
	.catch(err => console.error(err));

//Example route

app.get('/api/items', (req, res) => {
	res.json({message: "API is working!"});
});

// Start server

app.listen(PORT, () => {
	console.log('Server is running on port ${PORT}');
});




