# Data dictionary

Data are written to `data/` as one row per perceptual trial (plus a few summary rows). The wide CSV
(`<participant>_confidence_probe_<date>.csv`) is the main file. Columns marked *(Builder)* or *(Coder)* exist only in that version.

## Session and condition
| Column | Meaning |
|---|---|
| `participant` | Participant ID typed in the start dialog |
| `condition` | `no_probe`, `sparse_probe` or `full_probe`. In Builder it reads `auto` on the first rows (before allocation) and the real condition on every trial row after allocation |
| `assignedCondition`, `conditionSource` *(Builder)* | Resolved condition, and whether it came from `counterbalance` or a `manual` override; written once, on one row |
| `conditionAllocation.group`, `.remaining` *(Builder)* | Counterbalance group (0, 1, 2) and slots left in that group |
| `probeScheduleString` | The full 160-flag probe schedule (1 = probe scheduled) |
| `sessionCompleted` *(Coder)* | 1 if the session finished, 0 if it was aborted with ESC |

## Trial structure
| Column | Meaning |
|---|---|
| `phase` | `practice`, `calibration`, `baseline` or `main` |
| `trialIndex`, `blockIndex`, `trialInBlock` | Main task only: 0-159, 0-3, 0-39 |
| `tiltDegUsed` | Absolute grating tilt in degrees (the calibrated value for baseline and main) |
| `tiltSignUsed` | -1 (left tilt) or +1 (right tilt) |
| `corrAns` | Correct key: `f` (left) or `j` (right) |

## Choice (orientation) response
| Column | Meaning |
|---|---|
| `practice_resp.*`, `calibration_resp.*`, `baseline_resp.*`, `main_resp.*` | Choice key (`.keys`), reaction time in seconds from grating onset (`.rt`), and correct = 1 / incorrect = 0 (`.corr`). Empty or null if no response was made |
| `choiceMade` | 1 if a choice was made on the trial |

## Confidence probe (main task)
| Column | Meaning |
|---|---|
| `probeOriginallyScheduled` | Probe flag from the randomised schedule, before missed choices are handled |
| `probeScheduled`, `confidenceRequested` | 1 if a confidence rating was actually requested (never after a missed choice) |
| `confidenceRating` | Confirmed rating, 1-6; empty when no rating was requested |
| `confidenceRT` | Seconds from the start of the rating screen to confirmation with SPACE |
| `confidenceFirstMoveT` | Seconds from the start of the rating screen to the first F/J press |
| `confidenceMade` | 1 if a rating was given |
| `confidence_resp.keys`, `.rt` *(Builder)* | Raw key log of the rating screen (all F/J/SPACE presses); use `confidenceRating` for analysis |

## Calibration
| Column | Meaning |
|---|---|
| `level` | Tilt shown on each calibration trial (QUEST) |
| `calibratedTiltDeg` | Threshold used for baseline and main trials (median of the last 10 levels, clamped to 1-15 degrees) |
| `calibrationAtBoundary` | 1 if the threshold sits on the 1 or 15 degree limit (review these participants) |
| `calibrationOmissions`, `questMean`, `questMode` *(Coder)* | Missed calibration trials and the QUEST posterior mean and mode |

## Notes
- Lagged variables (previous probe, previous accuracy, previous confidence) are not saved. Compute them in analysis after sorting by participant and `trialIndex`, within block where appropriate.
- Probe trials last longer than non-probe trials (self-paced rating). `confidenceRT` lets you model this.
