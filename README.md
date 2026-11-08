# Intelligent Knowledge-Based System for Industrial Equipment Fault Diagnosis and Maintenance Decision Support

## Project Overview
This project is a rule-based Knowledge-Based System (KBS) developed for the CT-359 Knowledge-Based Systems course at NED University of Engineering and Technology.

The system provides advisory fault diagnosis and maintenance decision support for three types of industrial equipment:

- Electric Motor
- Water Pump
- Air Compressor

It uses stored diagnostic knowledge, user-provided symptoms, and additional evidence to identify possible faults and generate maintenance recommendations.

## Key Features
- CSV-based knowledge representation
- Forward chaining inference
- Limited backward-chaining hypothesis checking
- Three-level reasoning process
- Evidence-based rule activation
- High-priority safety alerts
- Hypothetical maintenance cost estimates
- Stakeholder-based weighted priority ranking
- Illustrative certainty-factor scores

## Technologies Used
- Python
- CSV
- Rule-Based Reasoning
- Knowledge Representation

## Project Files
- `main.py` — Main program and inference engine
- `knowledge_base.csv` — Diagnostic and inference rules
- `sources.csv` — Technical references used for the knowledge base
- `Project_Report.pdf` — Project documentation
- `Presentation.pptx` — Project presentation

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

```bash
python main.py
```

## Limitations
This system is an academic decision-support prototype. Its diagnostic results are possible explanations, not confirmed equipment diagnoses. Cost estimates, stakeholder scores, and certainty factors are illustrative assumptions and require expert validation. The system does not directly monitor or control industrial equipment.

## Academic Information
**Course:** CT-359 Knowledge-Based Systems  
**University:** NED University of Engineering and Technology  
**Department:** Computer Science and Information Technology

## Disclaimer
This project is developed for educational purposes and should not replace qualified industrial inspection, professional engineering judgment, or established safety procedures.
