const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();

// Middleware
app.use(bodyParser.json());

// MongoDB Connection
mongoose.connect('mongodb://localhost:27017/lab-tests', { useNewUrlParser: true, useUnifiedTopology: true });

// Mongoose Schemas
const TestOrderSchema = new mongoose.Schema({
    userId: String,
    testType: String,
    status: { type: String, default: 'ordered' },
    results: String
});

const TestOrder = mongoose.model('TestOrder', TestOrderSchema);

// Routes
app.post('/order', async (req, res) => {
    const newOrder = new TestOrder(req.body);
    await newOrder.save();
    res.send('Test ordered successfully!');
});

app.get('/results/:userId', async (req, res) => {
    const results = await TestOrder.find({ userId: req.params.userId });
    res.send(results);
});

app.post('/results/:orderId', async (req, res) => {
    await TestOrder.findByIdAndUpdate(req.params.orderId, { results: req.body.results, status: 'completed' });
    res.send('Results updated successfully!');
});

// Start Server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
