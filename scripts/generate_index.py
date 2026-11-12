#!/usr/bin/env python3
"""Regenerate the notes index in README.md from the repo's folder structure.

Every .md file in a topic folder (except README.md) is listed under a heading
for its folder. The link text comes from the filename, followed by the note's
first Markdown heading when it has one. Only the block between the INDEX:START
and INDEX:END markers in README.md is rewritten.

Usage (from anywhere inside the repo):
    python3 scripts/generate_index.py
"""

import re
from pathlib import Path
from urllib.parse import quote

# Repo root = the folder above this script, so no absolute paths are needed.
REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"
SKIP_DIRS = {"scripts", "images"}
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")


def note_title(path: Path) -> str:
    """Return the first Markdown heading in the note, or a title from its name."""
    in_code = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        match = HEADING.match(line)
        if match and not in_code:
            return match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").capitalize()


# Words to keep in their usual capitalisation when turning names into titles.
SPECIAL_WORDS = {
    "ai": "AI", "ami": "AMI", "aws": "AWS", "boto3": "boto3", "cd": "CD",
    "ci": "CI", "cidr": "CIDR", "devops": "DevOps", "ec2": "EC2",
    "ansible": "Ansible", "github": "GitHub", "iac": "IaC", "ip": "IP",
    "jenkins": "Jenkins", "mongodb": "MongoDB", "nginx": "Nginx",
    "s3": "S3", "ssh": "SSH", "vpc": "VPC",
}


def pretty_name(name: str) -> str:
    """Turn 'deploy-app-with-mongodb' into 'Deploy app with MongoDB'."""
    words = re.split(r"[-_ ]+", name)
    words = [SPECIAL_WORDS.get(w.lower(), w) for w in words if w]
    if words and words[0] == words[0].lower():
        words[0] = words[0].capitalize()
    return " ".join(words)


def topic_name(folder: str) -> str:
    return " / ".join(pretty_name(part) for part in folder.split("/"))


def skipped(rel: Path) -> bool:
    return any(part.startswith(".") or part in SKIP_DIRS for part in rel.parts[:-1])


def build_index() -> str:
    notes = sorted(
        rel
        for rel in (p.relative_to(REPO_ROOT) for p in REPO_ROOT.rglob("*.md"))
        if len(rel.parts) > 1 and rel.name != "README.md" and not skipped(rel)
    )
    lines = [START, ""]
    current_folder = None
    for rel in notes:
        folder = rel.parent.as_posix()
        if folder != current_folder:
            if current_folder is not None:
                lines.append("")
            lines.append(f"### {topic_name(folder)}")
            lines.append("")
            current_folder = folder
        name = pretty_name(rel.stem)
        heading = note_title(REPO_ROOT / rel)
        entry = f"- [{name}]({quote(rel.as_posix())})"
        if heading and heading.lower() != name.lower():
            entry += f": {heading}"
        lines.append(entry)
    lines += ["", END]
    return "\n".join(lines)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    index = build_index()
    if START in text and END in text:
        before = text.split(START, 1)[0]
        after = text.split(END, 1)[1]
        new_text = before + index + after
    else:
        new_text = text.rstrip("\n") + "\n\n## Notes index\n\n" + index + "\n"
    if new_text != text:
        README.write_text(new_text, encoding="utf-8")
        print(f"Updated {README.relative_to(REPO_ROOT)}")
    else:
        print("Index already up to date")


if __name__ == "__main__":
    main()
