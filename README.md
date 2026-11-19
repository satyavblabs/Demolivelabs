# Oracle AI Database@Azure Enterprise Architecture

A LiveLabs workshop adapted from Satya Bhamidipati's demo script dated May 20, 2026. It includes an introduction, six labs, and selected original screenshots. The version 2.1 source describes preprovisioned Autonomous Database, Exadata, Exascale, Base Database, and GoldenGate resources; review mode is the default, with optional provisioning.

Source document: `Demo_Script 3.3.docx`. Its cover identifies version 2.1, dated May 20, 2026.

## Preview

From this folder run:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000/workshops/tenancy/?lab=introduction&nav=open in a browser. Internet access is required for Oracle's hosted LiveLabs JavaScript and CSS. Add `&qa=true` to enable the LiveLabs checker. Serve through HTTP; opening the HTML directly from disk will not reliably load the manifest and Markdown.

The launcher is Oracle's official sample tenancy launcher. The manifest uses relative paths so the workshop can be placed under a repository folder without changing lab paths.

## Contents

| Lab | Topic | Estimated minutes |
| --- | --- | --- |
| Introduction | Prerequisites and environment worksheet | 10 |
| 1 | Autonomous Base Database Exascale and GoldenGate workflows | 80 |
| 2 | Azure subscriptions and networking | 20 |
| 3 | Dedicated Exadata infrastructure | 20 |
| 4 | OCI management backups and Recovery Service configuration | 45 |
| 5 | Azure and OCI monitoring | 15 |
| 6 | Cleanup and cost review | 15 |

Total author estimate: 205 minutes plus deployment and deletion waits. Timing has not been validated with learners.

## Validation

Run `python3 scripts/validate.py` to check the manifest, required Markdown structure, local links, image names, and image references. These checks do not execute the cloud provisioning workflows or certify Oracle publication readiness. See AUTHOR_NOTES.md for environment and publication prerequisites.

## Authoring references

* [Oracle LiveLabs workshop authoring guide](https://oracle-livelabs.github.io/common/sample-livelabs-templates/create-labs/labs/workshops/livelabs/?lab=introduction&nav=open)
* [Oracle sample workshop](https://github.com/oracle-livelabs/common/tree/main/sample-livelabs-templates/sample-workshop)
* Product-specific documentation is linked in the labs.
