#!/usr/bin/env python3
"""CR-IS-CAT-01C-P4. Deterministic generator for the P4 vendor-neutral
corroborated population of the ISF catalogue.

Emits and updates, relative to the repository root (default: the parent of
this directory):

- entities/v1-alpha/domains/<domain>/functions/<dir>/function.yaml  (new)
- entities/v1-alpha/domains/<domain>/functions/<dir>/README.md      (new)
- entities/v1-alpha/domains/<domain>/index.yaml    (updated; P4 rows merged)
- entities/v1-alpha/index.yaml                     (updated; P4 counts merged)
- docs/is-semantic-architecture/target-id-snapshots.yaml
  (updated; the P4 ISC snapshot entries merged and the application-components
  pin advanced to the CR-IS-CAT-02C-P4 head commit)

The generator is idempotent and deterministic (per G-10): re-running it against
the same repository state reproduces byte-identical files. The P4 function
inventory is read from scripts/p4_function_data.json.

Usage: python3 scripts/generate_p4_population.py [repo_root]
"""

from __future__ import annotations
import json
import os
import re
import sys
import textwrap

CR = "CR-IS-CAT-01C-P4"
CR_ISC = "CR-IS-CAT-02C-P4"
DATE = "2026-11-10"
FPREFIX = "dea:information-system-function-"
CPREFIX = "dea:information-system-component-"


def ystr(s):
    s = str(s)
    reserved = {"true", "false", "null", "yes", "no", "on", "off", "~", ""}
    scalar_like = (
        re.fullmatch(r"-?\d+(\.\d+)?", s)
        or re.fullmatch(r"\d{4}-\d{2}-\d{2}", s)
    )
    safe = (
        s != ""
        and not s[0].isspace()
        and not s[-1].isspace()
        and s[0] not in "!&*?|>%@`#'\""
        and ": " not in s
        and " #" not in s
        and "\n" not in s
    )
    if safe and not scalar_like and s.lower() not in reserved:
        return s
    return "'" + s.replace("'", "''") + "'"


def block(text, indent=2, width=94):
    """Wrap text for a YAML block scalar; deterministic."""
    pad = " " * indent
    lines = []
    for para in text.split("\n"):
        if not para.strip():
            lines.append("")
            continue
        lines.extend(textwrap.wrap(para, width=width) or [""])
    return "\n".join(pad + ln if ln else "" for ln in lines)


def emit_function_yaml(fn):
    out = []
    out.append(f"id: {fn['id']}")
    out.append("type: InformationSystemFunction")
    out.append(f"name: {ystr(fn['name'])}")
    out.append("description: |")
    out.append(block(fn["description"]))
    out.append('version: "1.0.0"')
    out.append("lifecycle_status: planned")
    out.append(f"functional_domain: {fn['domain_id']}")
    out.append(f"category: {fn['domain_id']}")
    out.append("decomposition_level: F4")
    out.append("executing_components:")
    out.append(f"- {fn['exec_id']}")
    out.append("governance:")
    out.append('  functional_owner: "IS Semantic Architecture programme"')
    out.append('  steward: "IS Semantic Architecture programme"')
    out.append("  approval_status: proposed")
    out.append("  criticality: business-critical")
    out.append(f"  source_and_evidence: {ystr(fn['evidence'])}")
    out.append('  review_date: "2027-11-10"')
    out.append("references:")
    out.append("- technehub-labs/dea-catalog-system-functions/change-requests/"
               "CR-IS-CAT-01C-P4-vendor-neutral-corroborated-population.md")
    out.append("- technehub-labs/dea-catalog-application-components "
               f"(executing component catalogue; component {fn['exec_id']})")
    out.append("metadata:")
    out.append("  created_by: Emmanuel A. Otchere")
    out.append(f'  created_date: "{DATE}"')
    out.append(f'  last_modified: "{DATE}"')
    out.append(f"  cr: {CR}")
    out.append("  notes: |")
    out.append(block(
        "F4 vendor-neutral leaf of the " + fn["subsystem"] + " sub-system of the "
        + fn["system"] + ". Grouping is by functional_domain; the crawl to the "
        "executing component is via executing_components (per G-06 and G-12). "
        "Vendor corroboration (at least 3 distinct vendor systems) is recorded in "
        "governance.source_and_evidence; evidence only, no vendor product is canonical.",
        indent=4))
    out.append("")
    return "\n".join(out)


def emit_function_readme(fn):
    r = []
    r.append(f"# {fn['name']}")
    r.append("")
    r.append("## 1. Identity")
    r.append(f"- Canonical ID: `{fn['id']}`")
    r.append("- Version: 1.0.0")
    r.append("- Lifecycle: planned")
    r.append(f"- Functional Domain: {fn['domain_code']} {fn['domain_name']} (`{fn['domain_id']}`)")
    r.append(f"- Category: {fn['domain_code']} {fn['domain_name']} (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)")
    r.append("- Decomposition Level: F4")
    r.append("- Parent Function: none (vendor-neutral leaf; grouping is by functional domain per " + CR + ")")
    r.append("")
    r.append("## 2. Definition")
    r.append("")
    r.append(fn["description"])
    r.append("")
    r.append("## 3. Purpose and Responsibility")
    r.append("")
    r.append("Responsibility: " + fn["description"])
    r.append("")
    r.append(f"The function contributes to the {fn['sector']} sector outcome: {fn['sector_outcome']}.")
    r.append("")
    r.append("## 4. Functional Scope")
    r.append("### In Scope")
    r.append(f"- {fn['subsystem']} behaviour of the {fn['system']} (generic system class)")
    r.append(f"- Realized by the {fn['component']} via the {fn['service']}")
    r.append("### Out of Scope")
    r.append("- Workflow coordination across sub-systems (separate concern; the orchestration lives at the ISC layer)")
    r.append("- Cross-domain data persistence (owned by the information and data management domain where applicable)")
    r.append("- Vendor-specific extensions of the corroborating products (not canonical per G-12)")
    r.append("")
    r.append("## 5. Behavioural Specification")
    r.append("### Trigger")
    r.append(f"Invocation within the {fn['subsystem']} sub-system (request, event or schedule depending on deployment).")
    r.append("### Preconditions")
    r.append("- The executing component is reachable")
    r.append("- The required business objects are present")
    r.append("### Main Behaviour")
    r.append(fn["description"])
    r.append("### Alternative Behaviour")
    r.append("Not applicable to this function.")
    r.append("### Exception Behaviour")
    r.append("- Failure of the executing component produces a structured error response")
    r.append("- Errors are recorded in the sub-system log")
    r.append("### Postconditions")
    r.append("- The function outcome is produced (or a structured error)")
    r.append("")
    r.append("## 6. Inputs")
    r.append("Typed inputs are not declared by this vendor-neutral record; the function consumes the business objects named in its definition. The typed input contract is populated via a follow-on CR.")
    r.append("")
    r.append("## 7. Outputs")
    r.append("Typed outputs are not declared by this vendor-neutral record; the function produces the outcome named in its definition. The typed output contract is populated via a follow-on CR.")
    r.append("")
    r.append("## 8. Data and Event Interaction")
    r.append("### Consumed Data")
    r.append("- (see the definition; typed inputs follow in a follow-on CR)")
    r.append("### Produced Data")
    r.append("- (see the definition; typed outputs follow in a follow-on CR)")
    r.append("### Consumed Events")
    r.append("None declared.")
    r.append("### Produced Events")
    r.append("None declared.")
    r.append("")
    r.append("## 9. Composition and Dependencies")
    r.append("### Parent")
    r.append("None (no synthetic F2 parent; grouped by functional domain per G-06).")
    r.append("### Child Functions")
    r.append("None.")
    r.append("### Dependencies")
    r.append(f"- The executing component ({fn['exec_id']})")
    r.append(f"- The {fn['service']}")
    r.append("### Orchestration")
    r.append("Not applicable to this function. The function is F4 (leaf); orchestration is at the ISC layer.")
    r.append("")
    r.append("## 10. Execution Characteristics")
    r.append("Per-record execution characteristics are not asserted by the vendor-neutral tranche; they vary across the corroborating vendor implementations and are recorded per-deployment.")
    r.append("")
    r.append("## 11. Business Alignment")
    r.append("Capability and process alignment is not asserted by this tranche; the realizes/enables allocations remain owned by their catalogues per the metamodel relationship contracts (see CR-IS-CAT-01D). See the P4 coverage report for the sector outcome mapping.")
    r.append("")
    r.append("## 12. Executing Components")
    r.append("")
    r.append(f"- `{fn['exec_id']}`")
    r.append("")
    r.append("## 13. Non-Functional Characteristics")
    r.append("")
    r.append("| Characteristic | Value |")
    r.append("|---|---|")
    r.append("| Criticality | business-critical (generic tranche-level value; refined per-deployment) |")
    r.append("")
    r.append("## 14. Security and Governance")
    r.append("")
    r.append("- Functional owner: IS Semantic Architecture programme")
    r.append("- Steward: IS Semantic Architecture programme")
    r.append("- Approval status: proposed")
    r.append("- Criticality: business-critical (generic tranche-level value)")
    r.append("- Vendor evidence: see governance.source_and_evidence in the function record (at least 3 distinct vendor systems; evidence only per G-12)")
    r.append("")
    r.append("## 15. Measurement and Observability")
    r.append("### Relevant Metrics")
    r.append("Metric allocation is owned by the Metric catalogue per G-11 (OpenDEAM v0.7.0 measured_by). No metric is asserted by this record.")
    r.append("### Monitoring Expectations")
    r.append("Monitoring expectations are recorded per-deployment.")
    r.append("### Evidence Sources")
    r.append("- The executing component log")
    r.append("- The sub-system audit trail")
    r.append("")
    r.append("## 16. Examples and Use Cases")
    r.append("")
    r.append(f"- Use case 1: a standard invocation of {fn['name']} within the {fn['subsystem']} sub-system")
    r.append("- Use case 2: a high-volume invocation under load with horizontal scaling of the executing component")
    r.append("- Use case 3: an exceptional case (validation failure, dependency unavailability) with the structured error response")
    r.append("")
    r.append("## 17. Limitations and Assumptions")
    r.append("")
    r.append("- The function depends on the executing component being available")
    r.append("- The record is vendor-neutral: vendor products corroborate the function as evidence only (per G-12)")
    r.append("- No synthetic F2 parent is admitted by this tranche; grouping is by functional domain and the executing_components crawl (per G-06)")
    r.append("- Typed inputs, outputs and execution characteristics follow in a follow-on CR")
    r.append("")
    r.append("## 18. References")
    r.append("")
    r.append("- `change-requests/CR-IS-CAT-01C-P4-vendor-neutral-corroborated-population.md` (the CR doc)")
    r.append("- `taxonomy/functional-domains.yaml` (the classification layer)")
    r.append("- `schemas/entities/information-system-function.v2.json` (the v2 schema)")
    r.append("- `technehub-labs/dea-catalog-application-components` (the executing component catalogue; " + CR_ISC + ")")
    r.append("")
    r.append("## 19. Change History")
    r.append("")
    r.append(f"- {DATE}: Initial creation ({CR}; vendor-neutral corroborated population).")
    r.append("")
    return "\n".join(r)


# ---------------------------------------------------------------------------
# Index merges.
# ---------------------------------------------------------------------------

def parse_domain_index(text):
    """Parse a per-domain index. Returns (pre_lines, entries, ch_lines)."""
    lines = text.split("\n")
    entries = []
    i = 0
    fn_at = None
    ch_at = None
    while i < len(lines):
        if lines[i].startswith("functions:"):
            fn_at = i
            i += 1
            cur = None
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("  ")):
                if lines[i].startswith("- "):
                    if cur is not None:
                        entries.append(cur)
                    cur = {}
                    k, _, v = lines[i][2:].partition(": ")
                    cur[k] = v
                    if v.startswith("["):  # flow list e.g. children: []
                        cur[k] = [] if v == "[]" else v
                elif lines[i].startswith("  - "):
                    cur.setdefault("_children", []).append(lines[i][4:].strip())
                elif lines[i].startswith("  "):
                    k, _, v = lines[i].strip().partition(": ")
                    cur[k] = v
                i += 1
            if cur is not None:
                entries.append(cur)
            continue
        if lines[i].startswith("change_history:"):
            ch_at = i
            break
        i += 1
    return lines[: (fn_at + 1) if fn_at is not None else 0], entries, lines[ch_at:]


def merge_domain_index(ipath, fns):
    with open(ipath) as f:
        text = f.read()
    pre, entries, ch = parse_domain_index(text)
    p4_ids = {fn["id"] for fn in fns}
    kept = []
    for e in entries:
        if e["id"] in p4_ids:
            continue
        e = dict(e)
        if "_children" in e:
            e["children"] = e.pop("_children")
        kept.append(e)
    new = [
        {"id": fn["id"], "decomposition_level": "F4", "lifecycle_status": "planned",
         "parent": "null", "children": []}
        for fn in sorted(fns, key=lambda f: f["id"])
    ]
    out = list(pre)
    for e in kept + new:
        out.append(f"- id: {e['id']}")
        out.append(f"  decomposition_level: {e['decomposition_level']}")
        out.append(f"  lifecycle_status: {e['lifecycle_status']}")
        if e.get("parent") in (None, "null", "(none)"):
            out.append("  parent: null")
        else:
            out.append(f"  parent: {e['parent']}")
        ch_list = e.get("children") or []
        if isinstance(ch_list, str):
            ch_list = [c.strip("- ") for c in ch_list.strip("[]").split(",") if c.strip()]
        if ch_list:
            out.append("  children:")
            for c in ch_list:
                out.append(f"  - {c}")
        else:
            out.append("  children: []")
    out.append("")
    if not any(CR in ln for ln in ch):
        while ch and ch[-1] == "":
            ch.pop()
        ch.append("- version: '1.1'")
        ch.append(f"  date: '{DATE}'")
        ch.append(f"  cr: {CR}")
        ch.append(
            f"  note: 'P4 vendor-neutral corroborated population. {len(fns)} F4 records "
            f"added. Total {len(kept) + len(new)} records.'"
        )
        ch.append("")
    out.extend(ch)
    with open(ipath, "w") as f:
        f.write("\n".join(out))


def merge_root_index(rpath, by_domain):
    with open(rpath) as f:
        text = f.read()
    has_p4 = CR + " " in text or CR + "'" in text or CR in text
    if not has_p4:
        for dslug, fns in by_domain.items():
            n = len(fns)
            pat = re.compile(
                r"(- code: \w+-\d+\n  id: isf:domain:" + re.escape(dslug) +
                r"\n  name: [^\n]*\n  index: [^\n]*\n  function_count: )(\d+)"
            )
            m = pat.search(text)
            if m:
                text = text[: m.start(2)] + str(int(m.group(2)) + n) + text[m.end(2):]
        text = text.replace("version: '1.2'", "version: '1.3'", 1)
        text = text.replace("date: '2026-10-18'", f"date: '{DATE}'", 1)
        m = re.search(r"change_history:\n", text)
        if m:
            total = sum(len(fns) for fns in by_domain.values())
            doms = len(by_domain)
            entry = (
                f"- version: '1.3'\n"
                f"  date: '{DATE}'\n"
                f"  cr: {CR}\n"
                f"  note: 'P4 vendor-neutral corroborated population. {total} F4 records "
                f"across {doms} domains. Total: {total + 50} functions across 15/15 "
                f"domains.'\n"
            )
            text = text[: m.end()] + entry + text[m.end():]
        with open(rpath, "w") as f:
            f.write(text)


# ---------------------------------------------------------------------------
# Target-id snapshot merge.
# ---------------------------------------------------------------------------

def merge_snapshots(spath, comp_entries, pin):
    with open(spath) as f:
        lines = f.read().split("\n")
    # locate blocks
    snaps_at = next(i for i, ln in enumerate(lines) if ln.startswith("snapshots:"))
    comp_at = next(i for i, ln in enumerate(lines)
                   if ln == "  dea-catalog-application-components:" and i > snaps_at)
    counts_at = next(i for i, ln in enumerate(lines) if ln.startswith("counts:"))
    pinned_at = next(i for i, ln in enumerate(lines)
                     if ln.startswith("  dea-catalog-application-components: ") and i < snaps_at)
    # parse existing component entries
    entries = {}
    i = comp_at + 1
    cur = None
    while i < counts_at:
        ln = lines[i]
        if ln.startswith("    ") and ln.endswith(":"):
            cur = ln.strip()[:-1]
            entries[cur] = {}
        elif ln.startswith("      ") and cur:
            k, _, v = ln.strip().partition(": ")
            entries[cur][k] = v
        i += 1
    # merge new entries
    for e in comp_entries:
        cid = e["id"]
        assert cid not in entries or entries[cid].get("name", "").strip("'") == e["name"], cid
        entries[cid] = {
            "name": e["name"],
            "definition_or_outcome": "",
            "source_file": e["source_file"],
        }
    # re-emit
    out = []
    out.extend(lines[:pinned_at])
    out.append(f"  dea-catalog-application-components: {pin}")
    out.extend(lines[pinned_at + 1: comp_at + 1])
    for cid in sorted(entries):
        v = entries[cid]
        out.append(f"    {cid}:")
        out.append(f"      name: {v['name']}")
        out.append("      definition_or_outcome: ''")
        out.append(f"      source_file: {v['source_file']}")
    out.extend(lines[counts_at:])
    # counts section
    text = "\n".join(out)
    m = re.search(r"(  dea-catalog-application-components: )(\d+)", text[text.index("counts:"):])
    pre, post = text[: text.index("counts:")], text[text.index("counts:"):]
    post = re.sub(r"(  dea-catalog-application-components: )(\d+)",
                  lambda mm: mm.group(1) + str(len(entries)), post, count=1)
    with open(spath, "w") as f:
        f.write(pre + post)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(here)
    data_path = os.path.join(here, "p4_function_data.json")
    if not os.path.exists(data_path):
        data_path = os.path.join(repo, "scripts", "p4_function_data.json")
    data = json.load(open(data_path))

    fns = data["functions"]
    for fn in fns:
        fn["domain_id"] = f"isf:domain:{fn['domain_slug']}"
    by_domain = {}
    for fn in fns:
        by_domain.setdefault(fn["domain_slug"], []).append(fn)

    # 1. emit function records
    for fn in fns:
        dirn = "dea-isf-" + fn["id"][len(FPREFIX):]
        base = os.path.join(repo, "entities", "v1-alpha", "domains",
                            fn["domain_slug"], "functions", dirn)
        os.makedirs(base, exist_ok=True)
        with open(os.path.join(base, "function.yaml"), "w") as f:
            f.write(emit_function_yaml(fn))
        with open(os.path.join(base, "README.md"), "w") as f:
            f.write(emit_function_readme(fn))

    # 2. merge domain indexes
    for dslug, dfns in by_domain.items():
        merge_domain_index(
            os.path.join(repo, "entities", "v1-alpha", "domains", dslug, "index.yaml"), dfns)

    # 3. merge root index
    merge_root_index(os.path.join(repo, "entities", "v1-alpha", "index.yaml"), by_domain)

    # 4. merge target-id snapshots
    merge_snapshots(
        os.path.join(repo, "docs", "is-semantic-architecture", "target-id-snapshots.yaml"),
        data["component_snapshot_entries"],
        data["components_pin"],
    )

    print(f"OK: {CR} emitted {len(fns)} function records across "
          f"{len(by_domain)} domains (repo root: {repo})")


if __name__ == "__main__":
    main()
