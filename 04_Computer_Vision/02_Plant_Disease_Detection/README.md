# Plant Disease Detection

## 📋 Quick Overview

**Problem:** Detect crop diseases from leaf/plant images (Potato Leaf Disease Detection)

**Approach:** Deep learning using Convolutional Neural Networks with transfer learning

**Skills Demonstrated:**
- Image classification for agriculture
- Handling limited training data with augmentation
- Deploying ML models in production
- Real-world agricultural constraints
- Domain-specific model optimization
- Model compression for mobile deployment

**Dataset:** Potato Leaf Disease Dataset (images of healthy, early blight, late blight leaves)

---

## 🌾 Why This Project Matters

**Agricultural Context:**
Potato is a major global crop. Leaf diseases (Early Blight, Late Blight) cause significant yield losses. Automated detection enables early intervention and prevents epidemic spread.

**Agricultural Significance:**
- **Early detection:** Identify disease within days of onset
- **Field deployment:** Farmers use smartphones in the field
- **Real-time decisions:** Spray fungicide if disease detected
- **Cost savings:** Prevent crop loss
- **Regional impact:** Especially important in developing countries

---

## 📊 Key Results

*(See REPORT.md for detailed analysis)*

- Multi-class disease classification (3 or 4 classes)
- CNN architecture optimized for leaf images
- Per-disease classification accuracy
- Deployment on mobile/edge devices
- Disease symptoms explanation
- Treatment recommendations

---

## 🔗 Related Projects

- **Phase 2 (Previous):** Medical Image Classification (same CNN techniques)
- **Phase 1:** Breast Cancer Detection (medical image foundation)
- **Phase 3:** Crop Yield & Recommendation systems (downstream use)

---

## 💡 Key Concepts

### Multi-Class Classification
- Unlike binary (pneumonia: yes/no)
- Multiple classes: Healthy, Early Blight, Late Blight
- One-hot encoding for labels

### Leaf-Specific Augmentation
- Rotation (leaf orientation in photos)
- Zoom (different distances from camera)
- Contrast (different soil backgrounds)

### Agricultural Deployment
- Model must run on farmer's phone
- No internet required (privacy + reliability)
- Fast inference (real-time feedback)
- Visual interpretation helpful

### Model Conversion
- `.keras` format: Full model with architecture + weights
- Can be loaded for inference
- Can be deployed on mobile with TensorFlow Lite

---

## 🌍 Agricultural Impact

**For Smallholder Farmers:**
- Identify disease early (before massive spread)
- Decide whether to spray now or wait
- Choose appropriate fungicide
- Reduce unnecessary spraying (save money, environment)

**For Extension Officers:**
- Farmers send leaf photo by WhatsApp
- Officer confirms diagnosis with AI tool
- Recommends treatment protocol
- Monitors outcome in follow-up

**For Regional Planning:**
- Track disease spread across regions
- Alert when disease season approaches
- Coordinate bulk seed treatment
- Plan fungicide stockpiles

---
