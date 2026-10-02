"""Run with python3 tests/test_diagram_design.py before publishing the skill."""
from pathlib import Path
import re
import sys

SKILL = Path(__file__).resolve().parents[1] / "skills/diagram-design"
sys.path.insert(0, str(SKILL / "scripts"))
import mermaid_extract as mermaid


def check_resources():
    links = re.findall(r"\]\(([^)]+)\)", (SKILL / "SKILL.md").read_text())
    missing = [link for link in links if not link.startswith(("https:", "http:", "#"))
               and not (SKILL / link.split("#", 1)[0]).is_file()]
    gallery = (SKILL / "assets/index.html").read_text()
    for attributes, name in re.findall(r'<button\b([^>]*\bdata-type="([^"]+)"[^>]*)>', gallery):
        for variant in ([""] if "data-single" in attributes else ["", "-full", "-dark"]):
            target = f"assets/example-{name}{variant}.html"
            if not (SKILL / target).is_file():
                missing.append(target)
    assert not missing, f"{len(missing)} missing diagram resources: {missing}"


def check_edges():
    chains = ["A---B---C", "A--oB-->C", "A--xB-->C", "A===B==>C", "A-.-B-.->C"]
    for chain in chains:
        diagram = mermaid.parse_block(mermaid.SourceBlock(0, "flowchart LR\n" + chain, 1))
        assert [(edge.source, edge.target, edge.label) for edge in diagram.edges] == [
            ("A", "B", ""), ("B", "C", "")], chain
    for syntax, source, label, target in [
        ("A--yes-->B", "A", "yes", "B"),
        ("A<--yes-->B", "A", "yes", "B"),
        ("A o--yes--o B", "A", "yes", "B"),
        ("x--yes-->B", "x", "yes", "B"),
        ("A -- open --> B", "A", "open", "B"),
    ]:
        diagram = mermaid.parse_block(mermaid.SourceBlock(0, "flowchart LR\n" + syntax, 1))
        assert [(edge.source, edge.target, edge.label) for edge in diagram.edges] == [
            (source, target, label)], syntax


if __name__ == "__main__":
    check_resources()
    check_edges()
    print("Diagram resource links and Mermaid edge regressions passed.")
