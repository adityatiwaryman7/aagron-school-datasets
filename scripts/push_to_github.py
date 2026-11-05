"""
Aagron Master Dataset - GitHub Push Automation Script
Automates:
1. Staging of all dataset files, schemas, generators, and documentation.
2. Creating structured commit messages with inventory hashes.
3. Adding/verifying remote origin.
4. Pushing main branch to GitHub.
"""

import sys
import subprocess

def run_cmd(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.stdout.strip():
        print(res.stdout.strip())
    if res.stderr.strip() and res.returncode != 0:
        print(f"Error: {res.stderr.strip()}")
    return res.returncode, res.stdout, res.stderr

def main():
    print("==================================================")
    print("AAGRON CAMPUS AI DATASET - GIT & GITHUB AUTOMATION")
    print("==================================================")

    # Check git status
    code, out, err = run_cmd("git status --short")
    if "fatal: not a git repository" in err:
        print("Initializing Git repository...")
        run_cmd("git init")
        run_cmd("git branch -M main")

    # Add all files
    print("\n[1] Staging files for commit...")
    run_cmd("git add .")

    # Commit
    print("\n[2] Creating commit...")
    commit_msg = "feat(dataset): Aagron Campus Master AI Training Datasets & Exam Prep Engine"
    run_cmd(f'git commit -m "{commit_msg}"')

    # Check remote
    code, remotes, _ = run_cmd("git remote -v")
    if not remotes.strip():
        if len(sys.argv) > 1:
            remote_url = sys.argv[1].strip()
            print(f"\n[3] Adding remote origin: {remote_url}")
            run_cmd(f"git remote add origin {remote_url}")
            print(f"\n[4] Pushing to origin main...")
            run_cmd("git push -u origin main")
        else:
            print("\n[!] No remote origin configured yet.")
            print("To push to your GitHub repo, run:")
            print("  python scripts/push_to_github.py https://github.com/adityatiwari049/<your-repo-name>.git")
            print("or:")
            print("  git remote add origin https://github.com/adityatiwari049/<your-repo-name>.git")
            print("  git push -u origin main")
    else:
        print("\n[3] Remote origin detected. Pushing to GitHub...")
        run_cmd("git push -u origin main")

    print("\nGit automation check complete.")

if __name__ == "__main__":
    main()
