# Project Fact Sheet Registry

This directory contains the canonical, repo-backed fact sheets for Vitan Architects projects. 
These files serve as the single source of truth for all project-specific deliverables (portal submissions, client proposals, monograph chapters).

## YAML Schema Definition

Each project file should follow this schema:

```yaml
id: "project-slug"                # Unique identifier (e.g., "ara", "seventy", "privilon")
title: "Official Project Name"
location:
  city: "City"
  state: "State"
  country: "Country"
  address: "Full Address (optional)"
typology: "Primary Category (e.g., Residential, Institutional, Commercial)"
status: "Current Status (Completed, In-Progress, Concept)"
timeline:
  start_year: YYYY                # Optional
  completion_year: YYYY
technical_data:
  gross_built_area:
    value: 0
    unit: "sqm"                   # Default unit
  site_area:
    value: 0
    unit: "sqm"                   # Default unit
  height:
    value: 0
    unit: "m"                     # Optional
  floors: 0                       # Optional
  units: 0                        # Optional
team:
  client: "Client Name"
  lead_architect: "Ar. Jagrut Patel"
  design_team: []                 # List of names
  international_architect: ""     # Optional
  collaborators: []               # Optional
  structural_engineer: ""         # Optional
  mep_consultant: ""              # Optional
  landscape_architect: ""         # Optional
  contractor: ""                  # Optional
media:
  photographer: "Name"
  photography_permission: true    # boolean
  key_features: []                # List of short strings
  awards: []                      # List of awards won/shortlisted
identifiers:
  rera: ""                        # Optional
  internal_id: ""                 # Optional (e.g., VITA-NNN)
```
