"""Run pytest and generate a readable HTML report."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)
command = [
    sys.executable, "-m", "pytest", "tests",
    "--json-report", f"--json-report-file={REPORTS / 'pytest-report.json'}",
]
result = subprocess.run(command, cwd=ROOT)
if result.returncode == 0:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "make_html_report.py")], cwd=ROOT, check=False)
sys.exit(result.returncode)
