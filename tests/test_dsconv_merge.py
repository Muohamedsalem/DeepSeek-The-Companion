"""
Automated tests for .dsconv merge functionality.
Part of PRP-633: Test Automation.
"""
import json
import os
import pytest

SAMPLE_FILE1 = {
    "messages": [
        {"role": "user", "content": "رسالة من الملف الأول"}
    ]
}

SAMPLE_FILE2 = {
    "messages": [
        {"role": "user", "content": "رسالة من الملف الثاني"}
    ]
}

def merge_dsconv(data1, data2):
    """دمج ملفين .dsconv في ملف واحد."""
    return {
        "messages": data1.get("messages", []) + data2.get("messages", [])
    }

def test_merge_two_files(tmp_path):
    """اختبار دمج ملفين .dsconv."""
    file1 = tmp_path / "file1.dsconv"
    file2 = tmp_path / "file2.dsconv"

    with open(file1, 'w', encoding='utf-8') as f:
        json.dump(SAMPLE_FILE1, f)
    with open(file2, 'w', encoding='utf-8') as f:
        json.dump(SAMPLE_FILE2, f)

    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    merged = merge_dsconv(data1, data2)

    assert len(merged["messages"]) == 2
    assert merged["messages"][0]["content"] == "رسالة من الملف الأول"
    assert merged["messages"][1]["content"] == "رسالة من الملف الثاني"
