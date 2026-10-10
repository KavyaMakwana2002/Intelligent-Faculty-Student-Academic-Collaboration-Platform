const axios = require('axios');

exports.handleChat = async (req, res) => {
    try {
        const userMessage = req.body.message;
        
        // Forward the request to the Python FastAPI service
        const pythonServiceUrl = 'http://127.0.0.1:8000/chat';
        
        const response = await axios.post(pythonServiceUrl, {
            message: userMessage
        });
        
        res.json({
            success: true,
            reply: response.data.reply
        });
    } catch (error) {
        console.error("Error communicating with Python AI service:", error.message);
        // Fallback for Hackathon Demo if Python backend is not running
        res.json({
            success: true,
            reply: "I am EduConnect AI! 🤖 Since the Python backend is currently sleeping, I'll answer directly: Focus on understanding the core concepts of your semester! Feel free to refer to your study materials for deeper insights."
        });
    }
};
