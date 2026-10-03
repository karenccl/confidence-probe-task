"""Pure-Python helpers for the confidence-probe experiment (no PsychoPy imports,
so they can be unit-tested without a display)."""
import random

VALID_CONDITIONS = ('no_probe', 'sparse_probe', 'full_probe')
N_BLOCKS = 4
TRIALS_PER_BLOCK = 40
PROBES_PER_BLOCK = 10  # sparse_probe only


def median_value(values, default=8.0):
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        return float(default)
    mid = n // 2
    if n % 2 == 1:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2.0


def build_probe_schedule(rng=random):
    """160 flags: exactly PROBES_PER_BLOCK ones in each block of 40, shuffled within block."""
    schedule = []
    for _ in range(N_BLOCKS):
        block = [1] * PROBES_PER_BLOCK + [0] * (TRIALS_PER_BLOCK - PROBES_PER_BLOCK)
        rng.shuffle(block)
        schedule.extend(block)
    return schedule


def probe_for_trial(condition, schedule, trial_index):
    """Scheduled (pre-omission) probe flag for a main trial."""
    if condition == 'full_probe':
        return 1
    if condition == 'sparse_probe':
        return int(schedule[trial_index])
    return 0


def validate_condition(value):
    condition = str(value).strip().lower()
    if condition not in VALID_CONDITIONS:
        raise ValueError('condition must be one of %s' % (VALID_CONDITIONS,))
    return condition


def calibrated_tilt(levels, lo=1.0, hi=15.0):
    """Median of the last 10 QUEST levels, clamped. Returns (tilt, at_boundary_flag)."""
    raw = median_value(levels[-10:])
    tilt = min(max(raw, lo), hi)
    return tilt, int(tilt <= lo or tilt >= hi)


if __name__ == '__main__':
    # Self-test: python helpers.py
    for _ in range(1000):
        s = build_probe_schedule()
        assert len(s) == 160
        for b in range(N_BLOCKS):
            assert sum(s[b * 40:(b + 1) * 40]) == 10
    assert sum(probe_for_trial('full_probe', s, i) for i in range(160)) == 160
    assert sum(probe_for_trial('sparse_probe', s, i) for i in range(160)) == 40
    assert sum(probe_for_trial('no_probe', s, i) for i in range(160)) == 0
    assert median_value([]) == 8.0 and median_value([1, 3]) == 2.0 and median_value([5, 1, 3]) == 3.0
    assert calibrated_tilt([0.2] * 10) == (1.0, 1)
    assert calibrated_tilt([20] * 10) == (15.0, 1)
    assert calibrated_tilt([6, 7, 8] * 4) == (7.0, 0)
    try:
        validate_condition('x')
        raise SystemExit('validate_condition failed to reject')
    except ValueError:
        pass
    print('helpers self-test passed')
