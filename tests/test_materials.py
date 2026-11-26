"""资料完整性检查，不验证尚未提供的业务功能。"""
import unittest
from support.inspect_data import load_materials

class MaterialTests(unittest.TestCase):
    def test_read_all_materials(self):
        materials = load_materials()
        self.assertGreater(len(materials), 2)
        for name, value in materials.items():
            with self.subTest(file=name):
                self.assertTrue(value)
                if isinstance(value, list):
                    ids = [r["id"] for r in value if isinstance(r, dict) and "id" in r]
                    if name != "gazetteer.json":
                        self.assertEqual(len(ids), len(set(ids)))

    def test_text_ranges(self):
        def visit(value):
            if isinstance(value, dict):
                if "text" in value:
                    text = value["text"]
                    for key in ["teacher_marks", "theme_evidence", "annotations"]:
                        for mark in value.get(key, []):
                            pieces=[]
                            for start, end in mark.get("segments", []):
                                self.assertTrue(0 <= start < end <= len(text))
                                pieces.append(text[start:end])
                            self.assertEqual("…".join(pieces), mark["surface"])
                for child in value.values(): visit(child)
            elif isinstance(value, list):
                for child in value: visit(child)
        visit(load_materials())
