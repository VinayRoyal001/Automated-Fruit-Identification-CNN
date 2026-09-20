# 🍎 Automated Industrial Fruit Identification & Deep Learning Edge-Training Orchestrator

[![GitHub License](https://shields.io)](LICENSE)
[![Python Version](https://shields.io)](https://python.org)
[![Django Framework](https://shields.io)](https://djangoproject.com)
[![Deep Learning Framework](https://shields.io)](https://tensorflow.org)
[![Asynchronous Engine](https://shields.io)](https://readthedocs.io)
[![Docker Compliant](https://shields.io)](https://docker.com)

An enterprise-grade, full-stack **Computer Vision Application** and autonomous deep learning automation dashboard. Powered by an advanced **Django** asynchronous backend and **TensorFlow/Keras**, this application automates sub-50ms multi-class fruit classification alongside real-time, browser-driven edge model retraining.

Designed for automated packaging facilities, supply-chain quality checking hubs, and smart retail systems, this platform replaces archaic CLI workflows with an interactive web panel built purely with semantic **HTML5, CSS3, and Vanilla JavaScript**. Users can drag and drop images to classify produce or trigger heavy CNN training pipelines directly from the browser, monitoring training metrics (Loss, Accuracy, Validation splits) over active **WebSocket telemetry streams**.

---

## 📖 Table of Contents
- [✨ Core Capabilities](#-core-capabilities)
- [🏗️ Complete System Architecture & Data Topology](#%EF%B8%8F-complete-system-architecture--data-topology)
- [🛠️ Deep Tech Stack & Core Dependencies](#%EF%B8%8F-deep-tech-stack--core-dependencies)
- [📁 Granular Modular Directory Tree](#-granular-modular-directory-tree)
- [💾 Database Schema & Object-Relational Mapping (ORM)](#-database-schema--object-relational-mapping-orm)
- [🚀 Local & Production Deployment Blueprints](#-local--production-deployment-blueprints)
  - [Bare-Metal Local Setup](#bare-metal-local-setup)
  - [Containerized Multi-Service Docker Orchestration](#containerized-multi-service-docker-orchestration)
- [💻 Deep Dive: Frontend Interface Modules](#-deep-dive-frontend-interface-modules)
  - [1. Real-Time Vision Inference Panel](#1-real-time-vision-inference-panel)
  - [2. Live Training Supervisor UI](#2-live-training-supervisor-ui)
- [⚙️ The Deep Learning Core Pipeline Implementation](#%EF%B8%8F-the-deep-learning-core-pipeline-implementation)
- [🔌 Production-Grade REST & WebSocket API Specification](#-production-grade-rest--websocket-api-specification)
- [🧪 Automated Test Automation Suite](#-automated-test-automation-suite)
- [🤝 Contributing Standards](#-contributing-standards)
- [📄 Governance & License](#-governance--license)

---

## ✨ Core Capabilities

* **⚡ Ultra-Low Latency Inference Engine:** Optimized Convolutional Neural Network pipelines parse raw image matrix arrays to return multi-class confidence breakdowns with sub-50ms edge processing times.
* **🏋️ Asynchronous Web-Driven Training:** Moves intensive deep learning workloads off the main HTTP request/response thread into isolated background execution threads via custom async workers.
* **📊 Live WebSockets Telemetry:** Pipes per-epoch learning analytics (Loss, Validation Loss, Categorical Accuracy) straight from the running Keras execution loop down to reactive web progress monitors using zero-refresh connection sockets.
* **🔄 Dynamic Automated Dataset Engine:** Dynamically ingests browser-uploaded training samples, scales pixel values, strips mismatched color spaces, executes transformations, and structures files cleanly into class directories.
* **🛡️ Versioned Weights Management:** Hot-swaps compiled neural layers (`.keras` / `.h5`) seamlessly via the dashboard interface, permitting real-time configuration changes without restarting the host web instances.

---

## 🏗️ Complete System Architecture & Data Topology

```text
       [ CLUSTER FRONTIER: HTML5 / CSS3 / VANILLA JAVASCRIPT ]
             │                                       ▲
             │ POST /api/classifier/predict/         │ Live WebSockets Telemetry
             │ (Multipart Image Payload)             │ (Loss, Val Accuracy, Epoch Metrics)
             ▼                                       │
┌────────────────────────────────────────────────────┴──────────────────────────────────────┐
│                    [ FULL-STACK DJANGO APPLICATION ORCHESTRATOR ]                         │
│                                                                                           │
│  ┌─────────────────────────┐   ASGI Router/Routing    ┌─────────────────────────┐         │
│  │    WSGI Http Views      │ ───────────────────────> │  Async WebSocket Consumer│         │
│  │ (Inference / Base HTML) │                          │  (Pipes Live Telemetry) │         │
│  └─────────────────────────┘                          └─────────────────────────┘         │
│               │                                                   ▲                       │
│               │ Ingest / Read Image                               │ Intercepts Callbacks  │
│               ▼                                                   │                       │
│  ┌─────────────────────────┐                          ┌─────────────────────────┐         │
│  │     Pillow / OpenCV     │                          │ Custom Keras Callback   │         │
│  │  Matrix Normalization   │                          │ (Pipes Metrics to WS)   │         │
│  └─────────────────────────┘                          └─────────────────────────┘         │
│               │                                                   ▲                       │
│               ▼                                                   │                       │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐  │
│  │                        [ TENSORFLOW DEEP LEARNING SYSTEM ]                          │  │
│  │                                                                                     │  │
│  │  Dataset Ingestion  ──>   Conv2D Spatial Layers  ──>   Dense Target Classifier Head  │  │
│  └─────────────────────────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Deep Tech Stack & Core Dependencies

### Core Framework Layout
* **Application Framework:** `Django 5.0.x` / `Django REST Framework (DRF)`
* **Real-time Pipeline Router:** `Channels 4.x` (ASGI execution wrapper supporting persistent connections)
* **Asynchronous Communication Layer:** Native `asyncio` execution loops + WebSocket interface bindings
* **Deep Learning Engine:** `TensorFlow 2.15+` / `Keras Core API`
* **Computer Vision Suite:** `OpenCV (opencv-python-headless)`, `Pillow (PIL)`

### Analytical Ecosystem
* **Scientific Computation & Matrices:** `NumPy 1.24+`, `Pandas 2.x`
* **Statistical Verification Models:** `Scikit-Learn` (Confusion matrices, F1-Score calculations, precision metrics parsing)
* **Static Plotting & Diagnostics:** `Matplotlib` (Renders analytical training history images saved directly into media folders)

---

## 📁 Granular Modular Directory Tree

```text
.
├── Automated_Fruit_Identification_Using_CNN/
│   ├── __init__.py
│   ├── asgi.py                  # Asynchronous server configurations for WebSockets
│   ├── settings.py              # System security settings, dynamic paths, and channel routing
│   ├── urls.py                  # Core root routing directory map
│   └── wsgi.py                  # Standard synchronous WSGI app container interface
├── classifier/                  # Primary Business Logic Context Application
│   ├── __init__.py
│   ├── admin.py                 # Extends Django Admin to view classification logs
│   ├── apps.py                  # App initializer parameters
│   ├── consumers.py             # Asynchronous WebSocket protocols routing training telemetry
│   ├── migrations/              # Automated database change scripts
│   │   └── __init__.py
│   ├── models.py                # Database models schema representing platform operations
│   ├── routing.py               # WebSocket explicit internal URL routes
│   ├── urls.py                  # Application REST API and dashboard mapping
│   ├── views.py                 # Handles views for base templates and file analysis APIs
│   ├── ml_engine/               # Machine Learning Engineering Subsystem
│   │   ├── __init__.py
│   │   ├── network.py           # Explicit CNN layers layout & model compilation rules
│   │   ├── pipeline.py          # Image augmentation operations and pixel scaling steps
│   │   └── supervisor.py        # Keras Callback override capturing metrics per epoch
│   └── templates/
│       └── classifier/          # Semantic presentation screens
│           ├── base.html        # Shared head structure, global layouts, and assets
│           ├── dashboard.html   # Main system panel for image analysis
│           └── training.html    # Hyperparameter selection configurations dashboard
├── static/                      # Static Application Core Assets
│   ├── css/
│   │   └── app.css              # Custom UI stylesheet with responsive flex layouts
│   └── js/
│       ├── uploader.js          # Handles drag-drop and dynamic REST file handling
│       └── ws_telemetry.js      # WebSocket client manager displaying live graphics
Use code with caution.├── media/                       # Storage Area for System Files│   ├── dataset_vault/           # Ingested datasets grouped by label (e.g., Apple, Mango)│   ├── optimized_models/        # Saved network structures (.keras weights)│   └── inference_cache/         # Temporarily stored prediction snapshots├── tests/                       # Unit Testing Infrastructure│   ├── init.py│   ├── test_model.py            # Deep neural structure layer structural tests│   └── test_views.py            # API operational check validation cases├── Dockerfile                   # Deployment isolation setup file├── docker-compose.yml           # Multi-service container pipeline orchestration setup├── manage.py                    # Django management utility script└── requirements.txt             # Project system explicit dependencies lock file```💾 Database Schema & Object-Relational Mapping (ORM)The internal system relies on a high-integrity data layer to track user requests, track dynamic dataset balances, and map custom training metrics accurately.```pythonConceptual representation of classifier/models.pyfrom django.db import modelsclass FruitCategory(models.Model):"""Stores information about the system's target fruit categories."""name = models.CharField(max_length=100, unique=True)slug = models.SlugField(max_length=120, unique=True)created_at = models.DateTimeField(auto_now_add=True)def str(self):return self.nameclass ModelWeightCheckpoint(models.Model):"""Tracks saved CNN instances, hyperparameter setups, and operational states."""version = models.CharField(max_length=20, unique=True)file_path = models.FileField(upload_to='optimized_models/')is_active = models.BooleanField(default=False)training_accuracy = models.FloatField(null=True, blank=True)training_loss = models.FloatField(null=True, blank=True)created_at = models.DateTimeField(auto_now_add=True)class ClassificationLog(models.Model):"""Logs analytical calls processed by the vision application server."""uploaded_image = models.ImageField(upload_to='inference_cache/')predicted_category = models.ForeignKey(FruitCategory, on_delete=models.SET_NULL, null=True)confidence_score = models.FloatField()latency_ms = models.FloatField()processed_at = models.DateTimeField(auto_now_add=True)```🚀 Local & Production Deployment BlueprintsBare-Metal Local SetupClone the repository:   bash git clone https://github.com cd Automated_Fruit_Identification_Using_CNN    Initialize an isolated python environment:   bash python -m venv venv source venv/bin/activate  # On Windows terminal use: venv\Scripts\activate    Install the exact package dependency lockfile:   bash pip install --upgrade pip pip install -r requirements.txt    Construct the environment configuration file:Create a .env file in the root workspace folder:   env DEBUG=True SECRET_KEY=django-insecure-your-super-secret-production-key-here ALLOWED_HOSTS=127.0.0.1,localhost DB_ENGINE=django.db.backends.sqlite3 DB_NAME=db.sqlite3    Execute schema migrations and aggregate presentation files:   bash python manage.py migrate python manage.py collectstatic --noinput    Fire up the localized execution engine server:   bash python manage.py runserver    Open http://127.0.0.1:8000 inside any standard modern web browser.Containerized Multi-Service Docker OrchestrationTo deployment inside scalable production ecosystems (e.g., AWS EC2, DigitalOcean Droplets), launch the containerized application using Docker Compose.```bashCompile dependencies and bring up the container network in background configuration modedocker-compose up --build -d``````yamldocker-compose.yml configuration footprintversion: '3.8'services:web:build: .command: python manage.py runserver 0.0.0.0:8000volumes:- .:/appports:- "8000:8000"environment:- DEBUG=False- SECRET_KEY=production-secure-hash-key-xyz- ALLOWED_HOSTS=*restart: always```💻 Deep Dive: Frontend Interface Modules1. Real-Time Vision Inference PanelFile Processing Mechanism (uploader.js): Intercepts standard drag-and-drop operations, converts raw multi-part structures asynchronously using JavaScript's native Form Data objects, and passes payloads over HTTP REST channels.Dynamically Rendered States: The UI tracks client loading indicators, handles client-side image compression pre-flight if required, and maps class probability tables out neatly with CSS Flexbox element layouts.```javascript// Native Vanilla JS implementation sample snippet from uploader.jsconst dropZone = document.getElementById('drop-zone');dropZone.addEventListener('drop', async (e) => {e.preventDefault();const files = e.dataTransfer.files;if(files.length === 0) return;const formData = new FormData();formData.append('image', files[0]);const response = await fetch('/api/classifier/predict/', {method: 'POST',body: formData});const result = await response.json();document.getElementById('result-label').innerText = Classified As: ${result.prediction};document.getElementById('confidence-bar').style.width = ${result.confidence_score * 100}%;});```2. Live Training Supervisor UIHyperparameter Matrix Control: Users choose training parameters (Epoch lengths, Batch distributions, Optimization profiles, Validation split ratios) using structured dropdown forms.WebSocket Channel Implementation (ws_telemetry.js): Establishes an active channel connection immediately upon request confirmation. It updates visual CSS progress bars and maps learning rate optimizations live as individual epoch execution passes conclude.⚙️ The Deep Learning Core Pipeline ImplementationThe underlying engine configures highly descriptive, custom Convolutional configurations decoupled from standard views logic to enforce separation of concerns.```pythonConceptual representation of classifier/ml_engine/network.pyimport tensorflow as tffrom tensorflow.keras import layers, modelsdef build_custom_fruit_cnn(input_shape=(128, 128, 3), num_classes=10):"""Compiles a highly optimized sequential matrix parsing CNN architecture."""model = models.Sequential([# Initial Spatial Transformation Mapping Blockslayers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),layers.MaxPooling2D((2, 2)),# Intermediate Abstract Feature Extractor Blockslayers.Conv2D(64, (3, 3), activation='relu'),layers.MaxPooling2D((2, 2)),layers.Conv2D(128, (3, 3), activation='relu'),layers.MaxPooling2D((2, 2)),# Dimensional Flattening & Normalization Blocklayers.Flatten(),layers.Dense(128, activation='relu'),layers.Dropout(0.5),  # Mitigates training dataset overfitting# Evaluation Decision Categorical Output Target Nodelayers.Dense(num_classes, activation='softmax')])model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])return model```🔌 Production-Grade REST & WebSocket API Specification1. High-Speed Image Inference Processing Endpointhttp POST /api/classifier/predict/ Content-Type: multipart/form-dataRequest Payload Parameters:image: Raw binary format image asset (.jpg, .png, .webp).Server JSON Response Blueprint (200 OK):json { "status": "success", "prediction": "Alphonso Mango", "confidence_score": 0.9812, "inference_latency_ms": 24.85, "alternatives": [ { "class": "Yellow Pear", "confidence": 0.0124 }, { "class": "Lemon", "confidence": 0.0064 } ], "timestamp": "2026-09-20T22:47:00Z" } 2. Live Training Workflow Launch Endpointhttp POST /api/classifier/train/initiate/ Content-Type: application/jsonJSON Body Payload:json { "epochs": 30, "batch_size": 16, "learning_rate": 0.0005, "data_augmentation": true } Server JSON Response Blueprint (202 Accepted):json { "status": "training_job_queued", "session_token": "job_sess_77291a", "websocket_connection_endpoint": "/ws/training/job_sess_77291a/" } 3. Active Real-Time WebSocket Telemetry Protocolhttp WEBSOCKET /ws/training/job_sess_77291a/ Dynamic Outbound Frame Format Streamed per Epoch Completion:json { "current_epoch": 14, "total_epochs": 30, "metrics": { "loss": 0.2415, "accuracy": 0.9124, "validation_loss": 0.2819, "validation_accuracy": 0.8954 }, "estimated_time_remaining_seconds": 210 } 🧪 Automated Test Automation SuiteThe platform ships equipped with comprehensive automated test scripts to enforce strict runtime behavior validations on both web endpoints and tensor shapes.```bashExecute localized system tests through the built-in management runnerpython manage.py test tests/```Execution CoverageTensor Array Integrity Verification (test_model.py): Passes test tensors through the network definition layer routines to ensure output vector counts match label dimensions without sizing conflicts.REST API Route Failsafe Testing (test_views.py): Submits malformed payloads and empty files to the system routes to ensure the API safely catches issues and returns appropriate bad request error responses instead of crashing.🤝 Contributing StandardsWe love updates! Follow this workflow to introduce enhancements to the application ecosystem smoothly:Fork this repository asset to your personal GitHub profile workspace.Initialize an isolated feature workspace:   bash git checkout -b feature/OptimalFeatureName    Commit codebase adjustments using clean, descriptive commit messaging standards:   bash git commit -m 'feat: optimize cnn pooling layout layers to reduce processing overhead'    Push your localized development branch changes upstream:   bash git push origin feature/OptimalFeatureName    Open an official production-targeted Pull Request (PR), listing out all introduced updates and verification test results.📄 Governance & LicenseThis software system pipeline ecosystem framework is safely distributed under the MIT Open Source License. Check out the internal project LICENSE script file for complete platform usage rules.
