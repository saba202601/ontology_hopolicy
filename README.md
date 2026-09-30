# Florida homeowners ontology demo

A fictional agent-to-homeowner demonstration with a shared domain model, Excel workbook, Streamlit interface and sample client letter. No carrier form was provided. This is not a quote, binding document, legal opinion or claims system.

## Run

Requires Python 3.10 or later.

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

## Files and data flow

- `data/demo.json`: fictional policy facts, classes, relationships and source URLs.
- `data/ontology.ttl`: OWL/RDFS vocabulary and example policy/coverage instances.
- `homeowners-ontology.xlsx`: editable policy inputs, dictionary, relationships, rules and sources.
- `client-letter.txt`: sample letter using the default inputs.
- `app.py`: interactive exploration, deductible arithmetic and downloadable letter.

JSON supplies the app and initial workbook/letter values. Excel changes do not update JSON. The app letter reflects the sidebar assumptions; the saved text letter is a static default example. Relationship cardinalities in JSON/Excel are design expectations, not OWL restrictions or enforced validation. This lightweight ontology is intended to be extended with carrier forms and evidence, not treated as a complete insurance standard.

## Demo walkthrough

1. Review the six illustrative coverage limits.
2. Inspect the ontology classes and relationships.
3. Compare a first hurricane deductible with a subsequent hurricane after $3,000 prior credit.
4. Read and download the resulting client letter.
5. Open the source references and identify missing policy evidence.

The scenario assumes one structure, a covered hurricane wind loss below the limit, unchanged dwelling limit, and (for subsequent storms) the same calendar year and insurer group. It illustrates deductible arithmetic only. It does not infer coverage from a peril or calculate final claim payment. Flood insurance, wind exclusions, roof settlement, special deductibles and endorsements require separate review.

## Verification and Git

```powershell
python -m unittest test_model.py
```

This folder is a local Git repository. To publish, create your own remote repository, add its URL with `git remote add origin <URL>`, commit using your own identity, and push. No GitHub repository or public deployment is created by this demo.

Sources are Florida DFS consumer guidance, accessed September 30, 2026; URLs are in the app and workbook. Reverify guidance and the issued contract before real client use.
