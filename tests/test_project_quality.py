from pathlib import Path
import py_compile


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_MODULES = [
    "etl_pipeline",
    "freshness_scoring_model",
    "smart_label_scanner",
    "allergen_detection",
    "surplus_food_marketplace",
]


def test_expected_project_modules_exist():
    missing = [name for name in REQUIRED_MODULES if not (ROOT / name).is_dir()]
    assert not missing, f"Missing expected project modules: {missing}"


def test_all_python_files_compile():
    python_files = list(ROOT.rglob("*.py"))
    assert python_files, "Expected Python source files were not found."

    failures = []
    for path in python_files:
        if any(part in {"__pycache__", ".venv", "venv"} for part in path.parts):
            continue
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            failures.append(f"{path}: {exc}")

    assert not failures, "\n".join(failures)


def test_no_environment_files_are_tracked_in_project_tree():
    forbidden = {".env", ".env.local", ".env.production"}
    found = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and p.name in forbidden]
    assert not found, f"Environment files must not be committed: {found}"
