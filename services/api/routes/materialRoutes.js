const upload = require('../middleware/upload');
const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const materialController = require('../controllers/materialController');
router.get('/', auth, materialController.getMaterials);
router.post('/', auth, upload.single('file'), materialController.uploadMaterial);
module.exports = router;
