const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());
const path = require('path');
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Routes
const aiChatRoutes = require('./routes/aiChat');
const authRoutes = require('./routes/authRoutes');
const userRoutes = require('./routes/userRoutes');
const assignmentRoutes = require('./routes/assignmentRoutes');

app.use('/api/ai-chat', aiChatRoutes);
app.use('/api/auth', authRoutes);
app.use('/api/users', userRoutes);
app.use('/api/assignments', assignmentRoutes);
const analyticsRoutes = require('./routes/analyticsRoutes');
const materialRoutes = require('./routes/materialRoutes');
app.use('/api/analytics', analyticsRoutes);
app.use('/api/materials', materialRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Node.js API running on port ${PORT}`);
});
