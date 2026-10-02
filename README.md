# Conservation Biology – interactive course site

Streamlit site for an undergraduate Conservation Biology course: lessons, class activities,
data exercises (GBIF), and simulations across 11 units.

Live: https://lundquistecology.com/conservation/ · Author: Matthew J. Lundquist, Ph.D.

## Run

```bash
docker compose up -d --build   # serves on http://localhost:8501
```

Open a unit directly with `?unit=N` (for example `?unit=5`).

## Structure

- `app.py` – navigation; the course outline lives in the `UNITS` table
- `unit1/` … `unit9/`, `paper_summary/`, `data_analysis_activity/` – one module per page (`pageN_content()`)
- `common/instructor.py` – instructor-only controls

## Instructor tools

Class activity pages store submissions on the server. Clearing them requires an instructor key,
set as `CONSERVATION_INSTRUCTOR_KEY` in a `.env` file next to `docker-compose.yml` (not committed).
Without it, the clear controls are turned off.
