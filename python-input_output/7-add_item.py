#!/usr/bin/python3
"""Define module"""
import sys
import os.path


if __name__ == '__main()__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_filen


def main():
    """الدالة الرئيسية للتعامل مع إضافة المعاملات إلى ملف JSON."""
    data = []
    args = sys.argv[1:]
    
    if os.path.isfile("add_item.json"):
        data = load_from_json_file("add_item.json")
    
    # تأكد من أن البيانات هي قائمة لإضافة المعاملات الجديدة
    if not isinstance(data, list):
        raise ValueError("البيانات الموجودة في JSON ليست قائمة.")
    
    data.extend(args)
    save_to_json_file(data, "add_item.json")


