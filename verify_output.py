"""Check a wide-text CSV from confidence_probe against the plan's test matrix.
Usage: python verify_output.py data/<file>.csv   (needs pandas)"""
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
col = 'assignedCondition' if 'assignedCondition' in df else 'condition'
cond = str(df[col].dropna().iloc[0])
main = df[df['phase'] == 'main']
ok = True


def check(label, passed, detail=''):
    global ok
    ok &= bool(passed)
    print('%-52s %s %s' % (label, 'PASS' if passed else 'FAIL', detail))


print('condition:', cond)
for ph, n in [('practice', 12), ('calibration', 40), ('baseline', 40), ('main', 160)]:
    check('%s rows' % ph, (df['phase'] == ph).sum() == n, str((df['phase'] == ph).sum()))
check('4 blocks x 40', (main.groupby('blockIndex').size() == 40).all() and main['blockIndex'].nunique() == 4)
check('20 per orientation per block', (main.groupby(['blockIndex', 'tiltSignUsed']).size() == 20).all())
check('trialIndex 0..159', list(main['trialIndex'].astype(int)) == list(range(160)))
sched = main['probeOriginallyScheduled']
expected = {'no_probe': 0, 'sparse_probe': 40, 'full_probe': 160}[cond]
check('scheduled probes == %d' % expected, sched.sum() == expected, str(sched.sum()))
if cond == 'sparse_probe':
    check('10 scheduled per block', (main.groupby('blockIndex')['probeOriginallyScheduled'].sum() == 10).all())
for col_ in ('confidenceRating', 'confidenceRT'):  # absent when no rating was ever shown (no_probe)
    if col_ not in main:
        main = main.assign(**{col_: float('nan')})
conf = main['confidenceRating']
delivered = main['probeScheduled'] == 1
check('confidence only on delivered probe rows', conf[~delivered].isna().all())
check('every delivered probe has a rating', conf[delivered].notna().all())
check('no probe after a missed choice', (main.loc[main['choiceMade'] == 0, 'probeScheduled'] == 0).all())
check('confidence values in 1..6', conf.dropna().astype(int).between(1, 6).all())
check('confidence RT recorded on probes', main.loc[delivered, 'confidenceRT'].notna().all())
check('calibratedTiltDeg present', df['calibratedTiltDeg'].notna().any(),
      str(df['calibratedTiltDeg'].dropna().iloc[0]) if df['calibratedTiltDeg'].notna().any() else '')
check('tiltDegUsed constant in main', main['tiltDegUsed'].nunique() == 1)
corr = main.dropna(subset=['main_resp.keys'])
check('corr consistent with corrAns', ((corr['main_resp.keys'] == corr['corrAns']).astype(int)
                                        == corr['main_resp.corr']).all())
print('\nALL PASS' if ok else '\nSOME CHECKS FAILED')
