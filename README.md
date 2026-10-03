# Confidence-Probe Reactivity Task

A PsychoPy experiment that tests whether **asking people to report their confidence changes the decisions they make**.
Participants judge the tilt of a briefly shown grating (left or right). Depending on their condition, they are asked for
a confidence rating on none, a few, or all of the trials, while everything else about the task is kept the same.

## Contents
1. [Purpose](#purpose)
2. [Design](#design)
3. [What a participant does](#what-a-participant-does)
4. [Trial timeline](#trial-timeline)
5. [Stimuli and parameters](#stimuli-and-parameters)
6. [Condition allocation](#condition-allocation)
7. [Data output](#data-output)
8. [How to run it](#how-to-run-it)
9. [Before collecting data](#before-collecting-data)
10. [Analysis suggestions](#analysis-suggestions)
11. [Files in this folder](#files-in-this-folder)

## Purpose
Confidence ratings are usually treated as a passive measure. Some work suggests that eliciting them can alter accuracy,
response times or decision thresholds. This task isolates that effect: the first-order decision is identical in every
condition, and only the amount of confidence reporting changes.

**Main question:** does repeatedly asking for confidence change first-order decision-making?

**Secondary question:** in the sparse condition, does being asked for confidence on trial *t* change accuracy or response time on trial *t+1*?
Because the probed trials are randomised within each person, this is a within-participant experimental contrast.

Hypotheses (no direction is predicted; findings in the literature are mixed):
- **H1:** accuracy differs between `full_probe` and `no_probe`.
- **H2:** choice response time differs between `full_probe` and `no_probe`.
- **H3:** in `sparse_probe`, accuracy or response time on trial *t+1* differs depending on whether confidence was requested on trial *t*.

Exploratory outcomes: confidence calibration and bias, serial dependence of confidence, metacognitive efficiency (meta-d′),
and decision-model parameters such as boundary separation.

## Design
Between-participant manipulation with three conditions. A between-participant design avoids carry-over, since people who
learn to monitor confidence on every trial may keep doing so in a later no-probe block.

| Condition | Confidence requested | Purpose |
|---|---|---|
| `no_probe` | 0 of 160 main trials | First-order behaviour without confidence reports |
| `sparse_probe` | 40 of 160 main trials (exactly 10 per block, random positions) | Immediate after-effects of a confidence report |
| `full_probe` | All 160 main trials | Conventional trial-by-trial metacognition design |

Everyone completes the same practice, calibration and a **no-confidence baseline** before the manipulation starts. The baseline gives each
person their own pre-manipulation accuracy and response time, which improves the comparison between groups.

## What a participant does
| Stage | Trials | Description |
|---|---|---|
| Welcome and consent | – | Information and consent screen |
| Condition allocation | – | Automatic, hidden from the participant |
| Instructions | – | Task rules; a confidence-rating explanation for `sparse_probe` and `full_probe`, a neutral screen for `no_probe` |
| Practice | 12 | Clearly tilted grating (12°) with feedback: "Correct" in green, "Incorrect" in red, nothing if no response |
| Calibration | 40 | Adaptive staircase (QUEST) finds each person's tilt threshold; no feedback |
| Baseline | 40 | Calibrated tilt, no confidence reports |
| Main task | 160 | 4 blocks of 40 (20 left and 20 right per block) with self-paced breaks; the condition applies here |
| Finish | – | "The experiment is finished" message for 3 seconds, then the experiment closes |

A full session has 252 perceptual decisions. Check the duration in your own pilot before advertising it.

## Trial timeline
Every trial (practice, calibration, baseline and main) follows this order:

1. **Fixation cross, 1.0 s** (0.5 s inter-trial interval plus 0.5 s fixation).
2. **Grating, 150 ms.** The cross is *not* shown while the grating is on screen; it reappears the moment the grating disappears.
3. **Response.** Press **F** for a left-tilted grating, **J** for a right-tilted one. The window is 1.5 s from grating onset, and reaction time is measured from onset.
   The trial moves on at the first response made after the 150 ms exposure (or at 1.5 s if there is none).
4. **After the decision:**
   - *Baseline and non-probe main trials:* the fixation cross stays for a further 1.5 s.
   - *Probe trials:* a **self-paced confidence rating** appears (see below). There is no fixation cross and no time limit.
   - *Practice trials:* feedback is shown for 0.6 s instead. *Calibration trials:* nothing follows the response.
5. Next trial. If the choice was missed, no confidence rating is requested for that trial.

**Confidence rating.** The question "How confident are you that your choice was correct?" appears with a scale from 1 (*Guessing*) to
6 (*Certain*) in the middle of the screen. The marker starts hidden. **F** moves it left, **J** moves it right (the first press places it at 3 or 4),
and **SPACE** confirms. SPACE only works once the marker has been placed.

**Timing note.** Because the rating is self-paced, probe trials are longer than non-probe trials by the participant's rating time.
This is a deliberate choice, but it means elapsed time differs between conditions. The rating time is saved (`confidenceRT`) so it can be modelled or controlled in analysis.

## Stimuli and parameters
| Setting | Value |
|---|---|
| Stimulus | Sinusoidal grating with a Gaussian mask |
| Size / spatial frequency / contrast | 0.18 screen heights / 4 cycles per stimulus / 0.8 |
| Background | Mid-grey |
| Window units | `height` (no monitor calibration needed; works online) |
| Tilt | Practice 12°; later trials use the person's calibrated tilt, left (-1) or right (+1) |
| Calibration | QUEST staircase, 40 trials, start 8° (SD 4), target 75% correct, guess rate 0.5, lapse rate 0.02, levels 0.5-15.5° |
| Threshold used | Median of the last 10 calibration levels, limited to 1-15°; missed calibration trials count as incorrect |

The settings are starting values for piloting, not validated parameters for every display or population. Parameters are defined in
`conditions/quest_conditions.csv` (staircase) and `conditions/two_orientations.csv` (left/right trials).

## Condition allocation
The Builder version assigns conditions automatically with PsychoPy's **Counterbalance Routine** (`conditionAllocation`, placed after consent).
It draws one of three equally likely groups: **0 = `no_probe`, 1 = `sparse_probe`, 2 = `full_probe`**.

- In the start dialog leave `condition` as `auto`. Typing `no_probe`, `sparse_probe` or `full_probe` overrides the allocation (useful for testing).
- The default is 2 slots per group and 15 repeats, i.e. **30 participants per group** (90 in total). Small batches keep the groups close to balanced as data come in.
  When all slots are used, new sessions end immediately.
- Slots are reserved when a participant starts, so dropouts can leave groups slightly uneven.
- **Local runs** keep their counts in a file called `shelf.json` next to the experiment. Delete it before real data collection so test sessions do not use up slots.
- **Online (Pavlovia)** counts are kept on the Pavlovia Shelf. Create a record there once (see [Running online](#running-online-pavlovia)).

The Coder script has no automatic allocation; choose the condition in its start dialog.

## Data output
Each session writes a CSV, a log and a `.psydat` file to `data/`. There is one row per perceptual trial. Key columns:

| Column | Meaning |
|---|---|
| `condition`, `assignedCondition` | Condition the participant received |
| `phase`, `trialIndex`, `blockIndex` | Where the trial is in the session |
| `main_resp.keys`, `.rt`, `.corr` | Choice, reaction time from grating onset, accuracy |
| `confidenceRating`, `confidenceRT` | Confidence (1-6) and the time taken to confirm it; empty on non-probe trials |
| `calibratedTiltDeg`, `calibrationAtBoundary` | Individual threshold, and a flag if it hit the 1° or 15° limit |

See **[docs/data_dictionary.md](docs/data_dictionary.md)** for every column.

## How to run it
### Requirements
- PsychoPy 2026.2.4 (the Builder version was developed with it; the standalone installer includes Python). Report the exact version you use.
- A keyboard. A desktop or laptop computer is recommended. Participants only use the F, J and SPACE keys.

### Builder (recommended)
1. Start PsychoPy and switch to the Builder view (**View → Go to Builder view**).
2. Open `confidence_probe.psyexp` (**File → Open**). Keep it inside this folder so it can find `conditions/`.
3. Press the green **Run** button. In the start dialog enter a participant ID and leave `condition` as `auto`.
4. The experiment runs fullscreen. Press **Escape** to quit. Data are saved in `data/`.

Builder may warn about an unknown `conditionsFile` entry on the calibration loop. This is expected and harmless.

### Coder script
Run `python confidence_probe.py` with a Python that has PsychoPy installed (for example the PsychoPy installer's Python).
Add `--quick` for a short, windowed run (2 blocks of 10 trials) while you test. Choose the condition in the start dialog.
The Coder script follows the same design but has no automatic allocation.

### Running online (Pavlovia)
1. In Builder use **Pavlovia → Sync** to upload the project, then set it to **Pilot** (testing) or **Running** (data collection) on pavlovia.org.
2. Check **Experiment settings → Online → Resources** lists both files in `conditions/`.
3. On pavlovia.org open **Dashboard → Shelf → Add Record** and create a counterbalance record:
   - **Key:** `conditionAllocation` (exact spelling)
   - **Scope:** Experiment, then this project
   - **Type:** Counterbalance
   - **Groups** `0`, `1`, `2`, each with 2 slots, and **nb reps** 15 (30 per group)
4. Run the Pilot link several times and check the downloaded files contain different `conditionAllocation.group` and `assignedCondition` values.

Pilot runs reserve slots too; reset the counters (circular arrow next to *completed*) before real collection.

## Before collecting data
- **Run a pilot** in every condition and open the output files. Confirm the counts: 12 practice, 40 calibration, 40 baseline and 160 main rows, with 0, 40 (10 per block) or 160 confidence ratings.
- **Check the tilt direction.** Confirm on your screen that a left-tilted grating (-1) looks tilted to the left. PsychoPy's `ori` is positive-clockwise.
- **Check calibration.** Look at `calibratedTiltDeg` and `calibrationAtBoundary`. Review rather than silently accept participants whose threshold sits at 1° or 15°.
- **Check timing** on the actual computers and browsers participants will use (frame rate, 150 ms exposure). Test Chrome, Firefox, Safari and Edge for online use.
- **Replace the consent text.** The consent screen contains placeholder text that must be replaced with your ethics-approved wording.
- **Set exclusion rules before looking at the data** (non-completion, many missed choices, near-chance accuracy, boundary calibration, implausibly fast responses, device and browser problems).
- Delete `shelf.json` and any test files in `data/`.

## Analysis suggestions
- Keep `phase == 'main'`; check 160 rows per participant and the probe counts for each condition.
- Primary models: a logistic mixed model for accuracy and a log-RT mixed model for valid responses, with condition, baseline performance, trial number and a random effect of participant.
- Local effect (sparse condition): model trial *t+1* accuracy and log-RT from whether trial *t* was probed, controlling for previous accuracy, previous RT, trial and block. Create lagged variables in your analysis script, within participant and block.
- Confidence models: confidence by correctness, RT, difficulty and previous confidence (serial dependence).
- Metacognition: meta-d′ is usable in the full condition; the sparse condition has about 40 ratings per person, so use hierarchical estimation or compare with the full condition down-sampled to the same schedule.
- Because probe trials take longer, include `confidenceRT` or total trial time when comparing conditions.

## Files in this folder
| File | Purpose |
|---|---|
| `confidence_probe.psyexp` | The Builder experiment (Python and JavaScript, so it also runs online) |
| `confidence_probe.py`, `helpers.py` | Standalone Coder version and its helper functions (`python helpers.py` runs a self-test) |
| `conditions/` | `two_orientations.csv` (left/right trials) and `quest_conditions.csv` (staircase settings) |
| `build_psyexp.py` | Regenerates the `.psyexp` from code. Once you edit the experiment in Builder, treat Builder as the master copy and do not re-run this |
| `simulate_session.py` | Runs a whole session with simulated key presses and clicks, for testing without a participant (`--trace` also checks what is on screen frame by frame) |
| `verify_output.py` | Checks a data file against the design (trial counts, probe counts, confidence only on probed trials, scoring) |
| `docs/data_dictionary.md` | Every output column |
| `confidence_probe.js`, `index.html`, `confidence_probe_lastrun.py` | Files generated by Builder when you run or sync the experiment |

To check a session you ran (use the Python that comes with PsychoPy, which has the needed packages):
```
python verify_output.py data/<your_file>.csv
```

## Citation and licence
If you use this task, please cite PsychoPy (Peirce et al., 2019, *Behavior Research Methods*) and add your own citation, licence and preregistration link here.
