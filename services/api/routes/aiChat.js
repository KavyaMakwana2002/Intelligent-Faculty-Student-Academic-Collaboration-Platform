const express = require('express');
const router = express.Router();
const aiChatController = require('../controllers/aiChatController');

router.post('/ai-chat', aiChatController.handleChat);

module.exports = router;
