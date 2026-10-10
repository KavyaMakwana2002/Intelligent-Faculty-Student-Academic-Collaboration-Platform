const upload = require('../middleware/upload');
const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const assignmentController = require('../controllers/assignmentController');

router.post('/', auth, upload.single('file'), assignmentController.createAssignment);
router.get('/', auth, assignmentController.getAssignments);

router.get('/:id', auth, assignmentController.getAssignmentById);

router.post('/:id/submit', auth, upload.single('file'), assignmentController.submitAssignment);
router.get('/:id/submission', auth, assignmentController.getSubmission);


router.get('/:id/submissions', auth, assignmentController.getSubmissionsForAssignment);
router.post('/submissions/:submission_id/grade', auth, assignmentController.gradeSubmission);
module.exports = router;

