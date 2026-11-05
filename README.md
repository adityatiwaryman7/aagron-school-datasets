# 🏫 Aagron Campus AI Master Dataset System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Format: JSONL](https://img.shields.io/badge/Format-JSONL-blue.svg)](https://jsonlines.org/)
[![Curriculum: K12_JEE_NEET_CAT_CA](https://img.shields.io/badge/Curriculum-K12%20%7C%20JEE%20%7C%20NEET%20%7C%20CAT%20%7C%20CA-brightgreen.svg)](#)
[![Compliance: 100%_PDF_Inventory](https://img.shields.io/badge/PDF_Compliance-100%25_Implemented-success.svg)](#)

A production-grade, multi-domain AI dataset ecosystem designed to train, evaluate, and operate the **Aagron School AI Operating System**.

This repository contains **100% of the dataset requirements** specified in:
1. `Aagron_School_AI_Master_Dataset_List.pdf` (93 functional categories across 5 capabilities)
2. `Aagron_School_Datasets_WHITE_REGENERATED.pdf` (97 dataset categories across Operations, Cost Intelligence, and Expansion Strategy)
3. **All-in-One Student Exam Preparation**: K-12 Board Curricula (CBSE, ICSE, State Boards), Engineering (JEE Main & Advanced), Medical (NEET), Management (CAT), and Professional Accounting (CA Foundation & Intermediate).

---

## 📂 Repository Structure

```
.
├── datasets/
│   ├── 01_autonomous_brain_and_operations/       # School ERP, timetable substitutions, bus logistics, SOPs
│   ├── 02_personal_ai_teacher_and_exam_prep/     # All-in-one student curriculum, books, competitive exams
│   │   ├── k12_boards/                           # Classes 1-12 (Maths, Science, Social, English, Hindi, NCERT)
│   │   ├── competitive_jee_neet/                 # JEE Main/Adv Physics & Chemistry, NEET Biology Mastery
│   │   └── management_ca_cat/                    # CAT Quant/DILR/VARC, CA Foundation & Inter Law/Tax/Audit
│   ├── 03_student_voice_intelligence/            # Voice notes, Hinglish code-switching, safeguarding triage
│   ├── 04_cost_intelligence_and_optimization/    # Department budgets, utility audits, student unit economics
│   ├── 04_school_intelligence/                   # Cross-school academic gap patterns, facility bottlenecks
│   ├── 05_expansion_strategy_and_forecasting/    # Demographic catchments, competitor fees, capex/opex ROI
│   └── 06_ai_training_evaluation_and_governance/ # Tool calling, Chain-of-Thought, adversarial jailbreak evals
├── generator_engine/                             # Scalable Python engines to regenerate or expand datasets
│   ├── build_all_datasets.py                     # Master orchestrator for generating all modules
│   ├── exam_prep_generator.py                    # K-12, JEE, NEET, CAT, CA exam question & solution generator
│   ├── ncert_curriculum_master.py                # NCERT books, chapter outlines, theorems & formula sheets
│   ├── operations_generator.py                   # Autonomous brain & daily school operations generator
│   ├── cost_expansion_generator.py               # Financial optimization & campus expansion modeling
│   ├── student_voice_generator.py                # Student grievance triage & welfare analytics generator
│   └── governance_eval_generator.py              # Function-calling, CoT reasoning & adversarial red-team generator
├── schemas/
│   └── dataset_metadata_dictionary.json          # Standard data dictionary & column definitions
├── scripts/
│   └── push_to_github.py                         # One-click Git staging, committing, and GitHub push automation
└── README.md
```

---

## 📚 Complete Dataset Inventory & Specifications

### 1. Autonomous Brain & Operations Management (PDF 1: 27 Datasets | PDF 2: 30 Datasets)
- **School Master & Hierarchy**: Infrastructure dimensions, classroom counts, laboratory specifications, affiliation criteria.
- **Timetable & Substitution Matrix**: Real-time biometric absence detection, teacher qualification matching, and automated zero-period substitution dispatch.
- **Fleet Transportation & GPS Logistics**: Telematics logs, route optimization, waterlogging bypass rules, parent alert broadcasts.
- **Historical Operational Incidents & SOPs**: Chemical spill protocols, power failure load shedding, dismissal bottleneck decongestion, equipment preventive maintenance.

### 2. Personal AI Teacher & All-In-One Exam Preparation
- **K-12 Curricula (CBSE / ICSE / State Boards)**:
  - *Class 1 to 5*: Foundational numeracy, literacy, EVS, bilingual Hindi-English concept foundations.
  - *Class 6 to 8*: Middle school algebra, geometry, physics, chemistry, biology, history, geography, civics.
  - *Class 9 to 10*: Board-level quadratic equations, trigonometry, electric circuits, chemical bonding, life processes.
  - *Class 11 to 12*: Advanced calculus, electrodynamics, organic reaction mechanisms, genetics, accounting.
- **Competitive Engineering & Medical (JEE & NEET)**:
  - *JEE Main & Advanced*: Rotational dynamics, electromagnetic induction, thermodynamics, calculus, coordinate geometry with multi-step derivations and traps.
  - *NEET UG*: Molecular basis of inheritance, human endocrine physiology, C4 plant photosynthesis, line-by-line NCERT citations.
- **Management & Professional (CAT & CA)**:
  - *CAT*: Quantitative Aptitude (Number theory, geometry), DILR logic matrices, VARC critical reasoning assumptions.
  - *CA Foundation & Inter*: AS-10 Property Plant & Equipment, Indian Contract Act 1872, Sec 10(13A) HRA tax computations, auditing standards.
- **Pedagogical Enrichment**: Common misconception alerts, step-by-step rubrics, adaptive learning paths, and bilingual explanations.

### 3. Student Voice Intelligence & Safeguarding
- **Speech & Multilingual Audio**: Code-switched transcripts (Hindi-English Hinglish) with colloquial idioms.
- **Grievance Triage & Mental Health Signals**: Detection of academic anxiety, peer bullying, and infrastructure tickets.
- **Red-Line Safeguarding Protocols**: Mandatory escalation rules routing child protection concerns to designated human safeguarding leads.

### 4. Cost Intelligence & Financial Optimization (25 Datasets)
- **Budget vs. Actual Variance**: Department-level tracking of utilities, transportation, and IT software spend.
- **Energy & Utility Audits**: Smart-meter load profile analysis, HVAC setpoint optimizations, and corridor lighting automation.
- **Student-Wise Operating Cost**: Granular unit economics per student across primary, middle, and senior streams.

### 5. Campus Expansion Strategy & Forecasting (30 Datasets)
- **Demographic Catchment Models**: School-age population density, growth trends, and competitor school fee benchmarks.
- **Capital Expenditure (Capex) & Break-Even**: Greenfield campus cost projections, faculty payroll scaling, and payback curves.

### 6. AI Governance, Tool-Calling & Safety (18 Datasets)
- **Function-Calling Episodes**: Grounded tool-use schema for database queries, scheduling calls, and task dispatch.
- **Chain-of-Thought (CoT)**: Step-by-step root-cause reasoning distinguishing superficial symptoms from root issues.
- **Adversarial Red-Teaming**: Resistance to prompt injection, PII exfiltration, live exam cheating, and privilege bypass.

---

## 🚀 How to Run & Regenerate Datasets

### Run the Generator Pipeline
To regenerate or expand the dataset with fresh samples:
```bash
python generator_engine/build_all_datasets.py
```

### Format Verification
Every dataset is written in standard **JSON Lines (`.jsonl`)**, making it directly compatible with:
- Hugging Face `datasets` library: `load_dataset("json", data_files="...")`
- OpenAI / Anthropic / Gemini fine-tuning JSONL formats
- Vector databases (ChromaDB, Pinecone, Qdrant) for RAG applications

---

## ⚡ 10 GB+ Massive LLM Training Corpus Extractor

To extract and stream the **minimum 10 GB full-scale LLM training corpus** locally onto your disk in 50 MB shards:

```bash
# Extracts 10 GB of training data sharded into 50 MB JSONL files
python generator_engine/extract_10gb_master_corpus.py --target-gb 10.0
```

This generates high-density training data across all domains (K-12 textbooks, JEE, NEET, CAT, CA, operations, cost analytics, student voice, and AI governance).

---

## 🔄 GitHub Push Automation

### Push Updates to GitHub:
```bash
python scripts/push_to_github.py https://github.com/adityatiwaryman7/aagron-school-datasets.git
```

