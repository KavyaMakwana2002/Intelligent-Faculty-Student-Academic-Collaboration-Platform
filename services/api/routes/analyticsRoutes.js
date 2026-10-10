const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const analyticsController = require('../controllers/analyticsController');
router.get('/dashboard', auth, analyticsController.getDashboardStats);

router.get('/faculty-insights', auth, analyticsController.getFacultyInsights);
router.get('/student-recommendations', auth, analyticsController.getStudentRecommendations);

module.exports = router;

