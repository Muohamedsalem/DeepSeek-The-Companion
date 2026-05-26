"""
Automated tests for handling corrupted .dsconv files.
Part of PRP-633: Test Automation.
"""
import json
import os
import pytest

def import_dsconv(file_path):
    """محاكاة استيراد ملف .dsconv. ترفع استثناء إذا كان الملف تالفًا."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Invalid or corrupted .dsconv file")
    return data

def test_import_valid_file(tmp_path):
    """اختبار استيراد ملف .dsconv صالح."""
    file_path = tmp_path / "valid.dsconv"
    valid_data = {"messages": [{"role": "user", "content": "اختبار"}]}
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(valid_data, f)

    data = import_dsconv(file_path)
    assert len(data["messages"]) == 1

def test_import_corrupt_file(tmp_path):
    """اختبار استيراد ملف .dsconv تالف (نص عشوائي)."""
    file_path = tmp_path / "corrupt.dsconv"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("هذا ليس JSON صالحًا")

    with pytest.raises(ValueError, match="Invalid or corrupted"):
        import_dsconv(file_path)

def test_import_missing_file(tmp_path):
    """اختبار استيراد ملف .dsconv غير موجود."""
    file_path = tmp_path / "nonexistent.dsconv"

    with pytest.raises(FileNotFoundError):
        import_dsconv(file_path)
