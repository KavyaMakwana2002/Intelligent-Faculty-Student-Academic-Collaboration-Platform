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
        res.status(500).json({
            success: false,
            error: "Failed to connect to the AI service."
        });
    }
};
