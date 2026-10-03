"""Simulate a full session of confidence_probe.psyexp with fake keypresses and mouse clicks.

Usage (use the PsychoPy Python, from any folder):
    "C:/Program Files/PsychoPy/python.exe" simulate_session.py auto|no_probe|sparse_probe|full_probe [--trace]

--trace: record which stimuli are drawn on every flip, at exit print a summary plus every run with an empty frame
or several stimuli on screen at once (e.g. the first-frame run of the practice feedback). Use it to look for overlaps or gaps.

Compiles the .psyexp to _sim_lastrun.py (next to this file), then runs it in a small window.
Fake responses: ~80% correct, ~5% choice omissions, confidence random; Slider/Button are
auto-answered. Takes roughly 17-40 minutes of real time. Afterwards check the CSV with:
    "C:/Program Files/PsychoPy/python.exe" verify_output.py data/<file>.csv
Logic test only: it does not test real timing, real clicking, or the online (JS) version.
"""
import os
import random
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
COND = sys.argv[1]
if COND not in ('auto', 'no_probe', 'sparse_probe', 'full_probe'):
    raise SystemExit(__doc__)

from psychopy import gui, visual
from psychopy.experiment import Experiment
from psychopy.hardware import keyboard

exp = Experiment()
exp.loadFromXML('confidence_probe.psyexp')
script = 'sim_lastrun_%s.py' % COND
with open(script, 'w', encoding='utf-8') as f:
    f.write(exp.writeScript(target='PsychoPy'))


class FakeDlg:
    def __init__(self, dictionary, **kw):
        dictionary['participant'] = 'sim_%s_%d' % (COND, os.getpid())
        dictionary['condition'] = COND
        self.OK = True


class Key:
    def __init__(self, name, rt):
        self.name, self.rt, self.tDown, self.duration = name, rt, rt, None


state = {}


def get_keys(self, keyList=None, ignoreKeys=None, waitRelease=True, clear=True):
    if not keyList or keyList == ['escape']:
        return []
    t = self.clock.getTime()
    st = state.setdefault(id(self), {})
    if t < st.get('last_t', 1e9):  # clock was reset => new routine
        st['fired'] = False
        st['stage'] = 0
    st['last_t'] = t
    if keyList == ['f', 'j', 'space']:  # self-paced confidence rating: j, f, j, then space
        plan = [(0.5, 'j'), (0.8, 'f'), (1.1, 'j'), (1.4, 'space')]
        i = st.get('stage', 0)
        if i < len(plan) and t > plan[i][0]:
            st['stage'] = i + 1
            return [Key(plan[i][1], t)]
        return []
    if st.get('fired'):
        return []
    if keyList == ['space']:
        if t > 0.2:
            st['fired'] = True
            return [Key('space', t)]
        return []
    if keyList == ['f', 'j']:
        if t > 0.35:
            st['fired'] = True
            if random.random() < 0.05:
                return []  # omission
            ca = sys._getframe(1).f_locals.get('corrAns') or \
                sys._getframe(1).f_locals.get('calibCorrAns') or 'f'
            return [Key(ca if random.random() < 0.8 else ('j' if ca == 'f' else 'f'), t)]
        return []
    if t > 0.4:
        st['fired'] = True
        return [Key(random.choice(keyList), t)]
    return []


gui.DlgFromDict = FakeDlg
keyboard.Keyboard.getKeys = get_keys
visual.Slider.getRating = lambda self: 70
visual.ButtonStim.isClicked = property(lambda self: True)
_orig_init = visual.Window.__init__


def _win_init(self, *a, **k):
    k['fullscr'] = False
    k['size'] = (800, 500)
    _orig_init(self, *a, **k)


visual.Window.__init__ = _win_init
TRACE = '--trace' in sys.argv
if TRACE:
    import time
    _log = []
    _orig_flip = visual.Window.flip

    def _dump():
        out, prev, start, n = [], None, None, 0
        for tt, nm in _log:
            if nm != prev:
                if prev is not None:
                    out.append((round(start - _log[0][0], 3), n, prev))
                prev, start, n = nm, tt, 0
            n += 1
        out.append((round(start - _log[0][0], 3), n, prev))
        summary = [o for o in out if o[2] == () or len(o[2]) > 1]
        print('TRACE runs: %d; empty-frame runs: %d; multi-stimulus runs: %d'
              % (len(out), sum(1 for o in out if o[2] == ()), len(summary) - sum(1 for o in out if o[2] == ())), flush=True)
        for o in summary:
            print('ODD', o, flush=True)

    def _flip(self, *a, **k):
        names = tuple(getattr(x, 'name', type(x).__name__) for x in self._toDraw)
        r = _orig_flip(self, *a, **k)
        _log.append((time.perf_counter(), names))
        return r

    visual.Window.flip = _flip
    import atexit
    atexit.register(_dump)
sys.argv = [sys.argv[0]]
runpy.run_path(script, run_name='__main__')
