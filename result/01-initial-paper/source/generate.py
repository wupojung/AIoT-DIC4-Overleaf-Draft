"""Render the authoritative Markdown manuscript to modular IEEE LaTeX."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SECTIONS = (
    "01-abstract",
    "02-introduction",
    "03-related-work",
    "04-proposed-design",
    "05-experiment",
    "06-conclusion",
)
BANNER = "% Generated from {source} by generate.py.\n"


def render_inline(line):
    line = re.sub(r"\[@([a-zA-Z0-9_-]+)\]", r"\\cite{\1}", line)
    return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\\emph{\1}", line)


def render_section(stem):
    lines = (ROOT / f"{stem}.md").read_text(encoding="utf-8").splitlines()
    latex = []
    in_block = False
    for line in lines:
        if in_block:
            if line == "\x60\x60\x60":
                in_block = False
            else:
                latex.append(line)
        elif line == "\x60\x60\x60latex":
            in_block = True
        elif match := re.fullmatch(r"(#{1,2}) (.+?)(?: \{#([\w:-]+)\})?", line):
            marks, title, label = match.groups()
            if stem == "01-abstract":
                if title == "Abstract":
                    latex.append(r"\begin{abstract}")
                elif title == "Index Terms":
                    latex.extend((r"\end{abstract}", "", r"\begin{IEEEkeywords}"))
                else:
                    raise ValueError(f"Unexpected abstract heading: {title}")
            else:
                command = "section" if len(marks) == 1 else "subsection"
                latex.append(fr"\{command}{{{title}}}")
                if label:
                    latex.append(fr"\label{{{label}}}")
        else:
            latex.append(render_inline(line))
    if in_block:
        raise ValueError(f"Unclosed LaTeX block in {stem}.md")
    if stem == "01-abstract":
        latex.append(r"\end{IEEEkeywords}")
    return BANNER.format(source=f"{stem}.md") + "\n".join(latex).rstrip() + "\n"


def render_main():
    lines = (ROOT / "00-main.md").read_text(encoding="utf-8").splitlines()
    title = lines[0].removeprefix("# ")
    metadata = dict(
        line[2:].split(": ", 1) for line in lines if line.startswith("- ")
    )
    includes = "\n".join(fr"\input{{sections/{stem}}}" for stem in SECTIONS)
    return BANNER.format(source="00-main.md") + rf"""\documentclass[conference]{{IEEEtran}}

\usepackage[T1]{{fontenc}}
\usepackage{{cite}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\usepackage{{tabularx}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta,positioning}}
\usepackage[hidelinks]{{hyperref}}

\title{{{title}}}
\author{{\IEEEauthorblockN{{{metadata['Author']}}}
\IEEEauthorblockA{{{metadata['Affiliation']}\\{metadata['Location']}}}}}

\begin{{document}}
\maketitle

{includes}

\bibliographystyle{{IEEEtran}}
\bibliography{{references}}

\end{{document}}
"""


def render_bibliography():
    markdown = (ROOT / "07-references.md").read_text(encoding="utf-8")
    entries = re.findall(r"^\x60\x60\x60bibtex\n(.*?)^\x60\x60\x60$", markdown, re.M | re.S)
    if not entries:
        raise ValueError("07-references.md contains no BibTeX block")
    return "@comment{Generated from 07-references.md by generate.py.}\n" + "\n".join(entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check generated files")
    args = parser.parse_args()
    outputs = {
        "main.tex": render_main(),
        "references.bib": render_bibliography(),
        **{f"sections/{stem}.tex": render_section(stem) for stem in SECTIONS},
    }
    stale = []
    for name, content in outputs.items():
        path = ROOT / name
        if path.is_file() and path.read_text(encoding="utf-8") == content:
            continue
        if args.check:
            stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        parser.exit(1, "Stale generated files: " + ", ".join(stale) + "\n")


if __name__ == "__main__":
    main()
