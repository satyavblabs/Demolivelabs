# Author review and publication notes

## Status

Local workshop draft. Cloud provisioning, regional capacity, service entitlement, and deletion workflows have not been executed. No workshop has been registered, submitted, or published in Oracle LiveLabs or WMS.

## Before facilitating

1. Fill the environment worksheet with the assigned Azure and OCI context and verify read/create/delete permissions separately. Linking, service onboarding, networking, quotas, and shared Exadata provisioning are prerequisites, not implemented by this workshop.
2. Run Lab 1 in the assigned region. Confirm Autonomous storage minimum and units: the source text says 30 GB while screenshots show 1024 GB or 1 TB. Confirm compute and storage scaling policies and supported versions.
3. Confirm Base Database shape, compute units, database version, backup policy, and anchors. The source repeats Autonomous fields under Base Database; those copied fields were omitted rather than treated as Base Database configuration.
4. Confirm Exascale memory, ECPUs, Grid Infrastructure release, vault, and network values. Screenshots supplied settings absent from the source prose. The workflow creates a VM cluster, not an Exascale database; database creation remains outside scope.
5. Confirm the actual Autonomous recovery configuration. Source claims about a fixed US East/US West pairing were replaced with a review of the configured peer. Storage autoscaling is described separately from the compute multiplier.
6. Verify monitoring scope and metric availability. The source's `nace-demo-rg-eastus1-Metrics` wording was interpreted as a resource-group metrics view; no monitoring resource with that name is assumed.
7. Verify cleanup for every allowed provisioning path and document retained storage or backup artifacts. Confirm current regional support and cost visibility in the target environment.

## Before publishing

1. Add the real workshop stakeholder help email in the manifest's `help` field. It was omitted because the source does not supply one.
2. Review all screenshots for public distribution, including visible subscription IDs, tenancy names, user names, resource IDs, hostnames, network details, and source-specific resource names. Replace or redact them before public hosting. Original sample passwords were removed from all authored text; do not reintroduce them.
3. Use current screenshots for target-region settings, verify alt text against the final images, and confirm organizational rights to distribute source imagery.
4. Run the LiveLabs browser checker with `qa=true`, verify every navigation item and image, and complete the official LiveLabs QA checklist.
5. Register or update the workshop in WMS, place files in the assigned Oracle LiveLabs repository, configure hosting, and follow the publishing and review workflow from the authoring guide. This local folder does not perform those steps.

## Source traceability

The current source filename is Demo_Script 3.3.docx; its cover now identifies Ver 2.1 dated May 20, 2026. The content date was retained without asserting the file version.

Selected screenshots were extracted from the supplied DOCX and placed beside the labs. The adaptation turns demonstration narration into learner tasks, adds checkpoints, an environment worksheet, and workshop navigation, and preserves the distinction between shared review resources and learner-created resources.

## Local validation performed

* The manifest resolves all seven modules, and all 32 referenced PNG files decode successfully.
* All module Markdown files return HTTP 200 from the local preview server.
* Browser navigation rendered the introduction and all six labs using the official Oracle launcher. The browser checker displayed zero issues on the inspected lab pages.
* Source screenshots were visually reviewed for selection. Public-distribution review and current target-environment screenshots remain publication prerequisites.
* Azure and OCI provisioning, telemetry integration, and resource deletion were not executed.

## Attribution update

The latest supplied script adds Satya Bhamidipati and Padma Priya Natarjan as authors. Workshop acknowledgements credit both as authors and use the updated user-requested name Padma Priya Rajan Natarajan. The subsequent version 2.1 update also identifies Autonomous Database, Exadata, Exascale, and Base Database as preprovisioned. Review mode is now the default path; optional provisioning instructions remain available.

The introduction includes two overview screenshots from the supplied script: the Azure service overview and the linked OCI Exadata infrastructure view.

## Updated source incorporated on November 18 2026

The latest document adds GoldenGate to the preprovisioned services, a Lab 1.4 GoldenGate deployment walkthrough with seven screenshots, and Recovery Service configuration with four screenshots. Six representative screenshots were added to the workshop. Lab 1 now includes GoldenGate settings, deployment verification, and its illustrative 60-minute wait. Lab 4 includes the automatic-backup dialog, Recovery Service destination, and Bronze 14-day policy. Review mode cancels dialogs; optional configuration applies only to the facilitator-designated exercise database. The worksheet, cleanup coverage, module descriptions, and timing estimates were updated. Existing main-page images and author credits remain.

Before facilitating, verify GoldenGate entitlement, anchors, region, OCPU allocation, console credential policy, and deletion workflow. Confirm Recovery Service prerequisites, policy availability, network access, IAM permissions, and treatment of retained backups. The new cloud operations have not been executed. The updated GoldenGate task and Recovery Service task were verified in the local browser preview; structural validation was rerun for the updated package.

## Workshop acknowledgements

At the user’s request, author credits appear once, in a separate introduction subsection. Repeated lab acknowledgement sections were removed. The local validator enforces this workshop-wide arrangement; Oracle’s checker may flag missing per-lab acknowledgements during publication QA.

## Source document 3.3 verification

The supplied Demo_Script 3.3.docx was compared with the latest Demo_Script 3.2.docx on November 18, 2026. All paragraph text and all 80 embedded screenshot occurrences match. The existing workshop covers that source content; lab wording and user-requested titles were preserved. The environment worksheet and introduction images remain, and the single acknowledgement in the introduction credits Satya Bhamidipati and Padma Priya Rajan Natarajan. No spelling corrections were applied.
