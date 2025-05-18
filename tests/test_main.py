import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import load_and_process_data  # ✅ correct function name

def test_no_duplicates():
    df = load_and_process_data()
    assert not df.empty, "DataFrame should not be empty"
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
