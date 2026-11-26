"""读取并检查JSON资料是否完整，不推断业务结果。"""
import json
from pathlib import Path

def load_materials(root=None):
    base = Path(root) if root else Path(__file__).resolve().parents[1] / "data"
    return {p.name: json.loads(p.read_text(encoding="utf-8")) for p in sorted(base.glob("*.json"))}

def main():
    for name, value in load_materials().items():
        print(f"{name}：{len(value) if isinstance(value, (list, dict)) else 1}项")

if __name__ == "__main__":
    main()
