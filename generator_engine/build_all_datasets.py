"""
Aagron Master Dataset Pipeline Builder
Runs all generators to synthesize 100% of the dataset requirements from both PDFs:
- Aagron_School_AI_Master_Dataset_List.pdf (93 categories across 5 capabilities)
- Aagron_School_Datasets_WHITE_REGENERATED.pdf (97 categories across Operations, Cost, Expansion)
- Comprehensive Exam Prep (K-12 Boards CBSE/ICSE, JEE, NEET, CAT, CA)
"""

import sys
import time
from pathlib import Path

# Add current folder to path
sys.path.append(str(Path(__file__).parent))

import exam_prep_generator
import ncert_curriculum_master
import operations_generator
import cost_expansion_generator
import student_voice_generator
import governance_eval_generator

def main():
    start_time = time.time()
    print("================================================================")
    print("STARTING AAGRON CAMPUS AI MASTER DATASET GENERATION PIPELINE")
    print("================================================================\n")

    root = Path(".")
    datasets_root = root / "datasets"

    # 1. Exam Prep & Personal AI Teacher (K-12, JEE, NEET, CAT, CA)
    print(">>> [1/5] Building Personal AI Teacher & Exam Mastery Datasets...")
    exam_dir = datasets_root / "02_personal_ai_teacher_and_exam_prep"
    ncert_curriculum_master.generate_ncert_curriculum_and_books(exam_dir / "k12_boards")
    exam_prep_generator.generate_k12_datasets(exam_dir / "k12_boards")
    exam_prep_generator.generate_competitive_jee_neet(exam_dir / "competitive_jee_neet")
    exam_prep_generator.generate_management_ca_cat(exam_dir / "management_ca_cat")

    # 2. Autonomous Brain & Operations Management
    print("\n>>> [2/5] Building Autonomous Brain & Operations Management Datasets...")
    ops_dir = datasets_root / "01_autonomous_brain_and_operations"
    operations_generator.generate_operations_datasets(ops_dir)

    # 3. Cost Intelligence & Expansion Strategy
    print("\n>>> [3/5] Building Cost Intelligence & Campus Expansion Datasets...")
    cost_dir = datasets_root / "04_cost_intelligence_and_optimization"
    exp_dir = datasets_root / "05_expansion_strategy_and_forecasting"
    cost_expansion_generator.generate_cost_and_expansion(cost_dir, exp_dir)

    # 4. Student Voice & School Intelligence
    print("\n>>> [4/5] Building Student Voice Intelligence & School Intelligence Datasets...")
    voice_dir = datasets_root / "03_student_voice_intelligence"
    school_dir = datasets_root / "04_school_intelligence"
    student_voice_generator.generate_student_voice_and_school_intelligence(voice_dir, school_dir)

    # 5. Shared AI Governance, CoT, Tool-Use & Evaluation
    print("\n>>> [5/5] Building Shared AI Governance, Tool-Calling & Safety Datasets...")
    gov_dir = datasets_root / "06_ai_training_evaluation_and_governance"
    governance_eval_generator.generate_governance_and_eval_datasets(gov_dir)

    # Calculate statistics
    print("\n================================================================")
    print("DATASET GENERATION COMPLETED - GENERATING INVENTORY AUDIT")
    print("================================================================")

    total_files = 0
    total_records = 0
    total_bytes = 0

    print(f"\n{'Category / Directory':<55} | {'Files':<6} | {'Records':<8} | {'Size'}")
    print("-" * 80)
    for folder in sorted(datasets_root.glob("**/*")):
        if folder.is_dir():
            files = list(folder.glob("*.jsonl"))
            if files:
                folder_records = 0
                folder_bytes = 0
                for f in files:
                    with open(f, "r", encoding="utf-8") as fp:
                        count = sum(1 for _ in fp)
                    folder_records += count
                    folder_bytes += f.stat().st_size
                rel_path = folder.relative_to(root)
                print(f"{str(rel_path):<55} | {len(files):<6} | {folder_records:<8} | {folder_bytes/1024:.1f} KB")
                total_files += len(files)
                total_records += folder_records
                total_bytes += folder_bytes

    print("-" * 80)
    print(f"{'TOTAL AGGREGATE':<55} | {total_files:<6} | {total_records:<8} | {total_bytes/1024:.1f} KB")
    print(f"Elapsed Time: {time.time() - start_time:.2f} seconds")
    print("================================================================\n")

if __name__ == "__main__":
    main()
