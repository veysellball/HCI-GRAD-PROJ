# Git Workflow

This repository follows a simple, safe workflow suitable for a small team.

## Branch Roles

- `main`  
  Stable, release-ready branch. Only updated via PR from `dev`.

- `dev`  
  Integration branch. All work is merged here via PRs from feature branches.

- `feature/*`  
  Short-lived branches created per task/feature. Merged into `dev` via PR.

## Rules

1. Do NOT push directly to `main`.
2. Do NOT push directly to `dev`.
3. Every change must be done in a `feature/*` branch.
4. All merges happen through Pull Requests targeting `dev`.
5. Contracts are special:
   - Any change under `contracts/` requires PR label: `[CONTRACT CHANGE]`
   - Requires at least 2 approvals (Frontend + ML mandatory)

## Naming Convention

Use one branch per task. Examples:

- `feature/osman-session-consent`
- `feature/osman-capture-v1`
- `feature/emir-db-schema`
- `feature/emir-api-skeleton`
- `feature/veys-extractor-v1`

## Daily Development Flow

### 1) Sync `dev`
```bash
git checkout dev
git pull origin dev