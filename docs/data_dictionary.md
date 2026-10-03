# Data dictionary (one row per perceptual trial; )
| Column | Meaning |
|---|---|
| participant, condition | ID; no_probe / sparse_probe / full_probe |
| phase | practice, calibration, baseline, main |
| trialIndex / blockIndex / trialInBlock | main task only: 0-159 / 0-3 / 0-39 |
| tiltDegUsed, tiltSignUsed, corrAns | absolute tilt, -1/+1, correct key |
| `<phase>_resp.keys/.rt/.corr` | choice key, RT from stimulus onset, 0/1 (empty if missed) |
| choiceMade | 1 if a choice was made |
| probeOriginallyScheduled | randomised probe flag before omission handling |
| probeScheduled / confidenceRequested | probe actually delivered |
| confidence_resp.keys/.rt | rating 1-6 and RT (empty when not probed or no response) |
| confidenceMade | requested and answered |
| calibratedTiltDeg, calibrationAtBoundary, calibrationOmissions, questMean, questMode | calibration summary |
| probeScheduleString | full 160-flag schedule |
| sessionCompleted | 1 if the session finished, 0 if aborted with ESC |
Compute lagged variables (previous probe/accuracy/confidence) in analysis, sorted by participant and trialIndex.
