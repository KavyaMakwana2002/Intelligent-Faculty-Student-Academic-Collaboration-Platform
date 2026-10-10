const express = require('express');
const cors = require('cors');
const aiChatRoutes = require('./routes/aiChat');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.use('/api', aiChatRoutes);

app.get('/', (req, res) => {
    res.json({ message: "Welcome to EduConnect Node API" });
});

app.listen(PORT, () => {
    console.log(`Node API server is running on http://localhost:${PORT}`);
});
