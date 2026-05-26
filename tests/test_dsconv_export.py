"""
Automated tests for .dsconv export functionality.
Part of PRP-633: Test Automation.
"""
import json
import os
import pytest

SAMPLE_DATA = {
    "metadata": {
        "export_version": "1.0",
        "export_date": "2026-05-26T10:00:00Z",
        "user_name": "حلمي الجميل",
        "project": "DeepSeek-The-Companion"
    },
    "messages": [
        {"role": "user", "content": "اختبار تصدير"},
        {"role": "model", "content": "تم استلام الاختبار"}
    ]
}

def test_create_sample_dsconv(tmp_path):
    """اختبار إنشاء ملف .dsconv صالح."""
    file_path = tmp_path / "test.dsconv"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(SAMPLE_DATA, f, ensure_ascii=False)

    assert os.path.exists(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    assert data["metadata"]["user_name"] == "حلمي الجميل"
    assert len(data["messages"]) == 2
