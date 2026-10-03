"""Generate confidence_probe.psyexp (PsychoPy Builder) from the build plan.

Run with a Python that has PsychoPy installed, from this folder:
    "C:/Program Files/PsychoPy/python.exe" build_psyexp.py
Then open confidence_probe.psyexp in Builder. Builder remains the source of truth afterwards;
this script is only a reproducible generator.
"""
import os
from psychopy import data
from psychopy.experiment import Experiment
from psychopy.experiment.routines import Routine
from psychopy.experiment.loops import TrialHandler, MultiStairHandler
from psychopy.experiment.components.text import TextComponent
from psychopy.experiment.components.code import CodeComponent
from psychopy.experiment.components.keyboard import KeyboardComponent
from psychopy.experiment.components.grating import GratingComponent
from psychopy.experiment.components.slider import SliderComponent
from psychopy.experiment.components.textbox import TextboxComponent
from psychopy.experiment.components.button import ButtonComponent
from psychopy.experiment.components.polygon import PolygonComponent
from psychopy.experiment.routines.counterbalance import CounterbalanceRoutine

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
TWO = 'conditions/two_orientations.csv'
QUEST = 'conditions/quest_conditions.csv'

exp = Experiment()
exp.setExpName('confidence_probe')
S = exp.settings.params


def setp(obj, **kw):
    for k, v in kw.items():
        obj.params[k].val = v


def every_repeat(comp, *names):
    for n in names:
        comp.params[n].updates = 'set every repeat'


# ------------------------------------------------------------------ settings
S['Experiment info'].val = "{'participant': 'test001', 'condition': 'auto'}"
S['Units'].val = 'height'
S['color'].val = '$[0,0,0]'
S['colorSpace'].val = 'rgb'
S['Full-screen window'].val = True
S['Show mouse'].val = False
S['Enable Escape'].val = True
S['Save log file'].val = True
S['Save wide csv file'].val = True
S['Save csv file'].val = False  # per-loop saveAsText crashes in PsychoPy 2026.2.4 with nReps>1; wide csv is the main data file
S['Resources'].val = [TWO, QUEST]
S['End Message'].val = 'Thank you. You may close this window.'


# ---------------------------------------------------------------- helpers
from psychopy.experiment.params import Param
def new_routine(name, duration=None):
    r = Routine(name, exp)
    exp.addRoutine(name, r)
    exp.flow.addRoutine(r, len(exp.flow))
    if duration is not None:
        r.settings.params['stopType'].val = 'duration (s)'
        r.settings.params['stopVal'].val = duration
    return r


def add_text(r, name, text, start=0, dur=None, height=0.04, pos='(0, 0)',
             wrap=1.4, repeat=False):
    t = TextComponent(exp, r.name, name=name)
    setp(t, text=text, startVal=start, stopVal='' if dur is None else dur,
         letterHeight=height, pos=pos, wrapWidth=wrap, units='from exp settings')
    if dur is None:
        t.params['stopType'].val = 'duration (s)'
    if repeat:
        every_repeat(t, 'text')
    r.addComponent(t)
    return t


def add_keys(r, name, keys, start=0, dur=None, force_end=False, correct=None,
             cond=None):
    k = KeyboardComponent(exp, r.name, name=name)
    setp(k, allowedKeys=keys, forceEndRoutine=force_end, store='first key',
         storeCorrect=correct is not None, correctAns=correct or '')
    k.params['discard previous'].val = True
    k.params['startVal'].val = start
    k.params['stopVal'].val = '' if dur is None else dur
    k.params['stopType'].val = 'duration (s)'
    if cond:
        k.params['startType'].val = 'condition'
        k.params['startVal'].val = cond
    if correct is not None:
        k.params['correctAns'].updates = 'set every repeat'
    r.addComponent(k)
    return k


def add_code(r, name, **stages):
    """stages: py_<stage>=..., js_<stage>=..., stage in before/begin_exp/begin/frame/end."""
    c = CodeComponent(exp, r.name, name=name)
    c.params['Code Type'].val = 'Both'
    py = {'before': 'Before Experiment', 'begin_exp': 'Begin Experiment',
          'begin': 'Begin Routine', 'frame': 'Each Frame', 'end': 'End Routine'}
    js = {'before': 'Before JS Experiment', 'begin_exp': 'Begin JS Experiment',
          'begin': 'Begin JS Routine', 'frame': 'Each JS Frame', 'end': 'End JS Routine'}
    for key, val in stages.items():
        lang, stage = key.split('_', 1)
        c.params[(py if lang == 'py' else js)[stage]].val = val.strip('\n') + '\n'
    r.addComponent(c)
    return c


def add_fix(r, name, start=0, dur=0.5):
    return add_text(r, name, '+', start=start, dur=dur, height=0.05)


def add_gabor(r, name, ori, dur=0.15, start=0):
    g = GratingComponent(exp, r.name, name=name)
    setp(g, tex='sin', mask='gauss', size='(0.18, 0.18)', sf=4, contrast=0.8,
         ori=ori, pos='(0, 0)', units='from exp settings')
    every_repeat(g, 'ori')
    g.params['startVal'].val = start
    g.params['stopType'].val = 'duration (s)'  # exactly 150 ms from actual onset
    g.params['stopVal'].val = dur
    r.addComponent(g)
    return g


def space_screen(name, text, repeat=False, dur=None):
    r = new_routine(name)
    add_text(r, name + '_text', text, repeat=repeat)
    add_keys(r, name + '_key', "['space']", force_end=True)
    return r


PRE = 1.0  # leading cross inside the decision routine: 0.5 s ITI + 0.5 s fixation (fewer routine switches)


def timing_code(resp, mode):
    """Decision-end logic. decisionEnd = routine time at the first response made after the 150 ms
    minimum exposure, or at the end of the 1.5 s window if no response.
    mode 'none': routine ends at decisionEnd.
    mode 'tail': the cross stays for a further 1.5 s (post-decision period), then the routine ends.
    mode 'probe': like 'tail' unless a confidence probe will follow (probe trial with a choice), then ends at decisionEnd."""
    py_probe = {'none': 'True', 'tail': 'False',
                'probe': '(probeThisTrial == 1 and bool(%s.keys))' % resp}[mode]
    js_probe = {'none': 'true', 'tail': 'false',
                'probe': ('(probeThisTrial === 1 && %s.keys !== undefined && %s.keys !== null '
                          '&& %s.keys.length > 0)' % (resp, resp, resp))}[mode]
    py_frame = (
        "if decisionEnd < 0:\n"
        "    if %(r)s.keys and t >= %(P)s + 0.15:\n"
        "        decisionEnd = t\n"
        "    elif t >= %(P)s + 1.5:\n"
        "        decisionEnd = t\n"
        "if decisionEnd >= 0:\n"
        "    if %(pp)s:\n"
        "        continueRoutine = False\n"
        "    elif t >= decisionEnd + 1.5:\n"
        "        continueRoutine = False" % dict(r=resp, P=PRE, pp=py_probe))
    js_frame = (
        "if (decisionEnd < 0) {\n"
        "    if (%(r)s.keys !== undefined && %(r)s.keys !== null && %(r)s.keys.length > 0 "
        "&& t >= %(P)s + 0.15) {\n"
        "        decisionEnd = t;\n"
        "    } else if (t >= %(P)s + 1.5) {\n"
        "        decisionEnd = t;\n"
        "    }\n"
        "}\n"
        "if (decisionEnd >= 0) {\n"
        "    if (%(pp)s) {\n"
        "        continueRoutine = false;\n"
        "    } else if (t >= decisionEnd + 1.5) {\n"
        "        continueRoutine = false;\n"
        "    }\n"
        "}" % dict(r=resp, P=PRE, pp=js_probe))
    return dict(py_begin="decisionEnd = -1", js_begin="decisionEnd = -1;",
                py_frame=py_frame, js_frame=js_frame)


def decision_routine(prefix, ori, setup=None, end=None, correct='$corrAns', mode='none'):
    """One routine per trial: cross 0-PRE, grating 150 ms, cross until the end (see timing_code)."""
    r = new_routine(prefix + '_decision')
    if setup:
        add_code(r, prefix + '_setup', **setup)
    add_fix(r, prefix + '_pre_fix', start=0, dur=PRE)
    # grating and keyboard start on the same frame the leading cross finishes (no overlap, no gap)
    g = add_gabor(r, prefix + '_gabor', ori, start=PRE)
    g.params['startType'].val = 'condition'
    g.params['startVal'].val = prefix + '_pre_fix.status == FINISHED'
    wf = add_fix(r, prefix + '_wait_fix', start=PRE + 0.15, dur=1.5)
    # cross appears on the same frame the grating is removed (no gap, no overlap)
    wf.params['startType'].val = 'condition'
    wf.params['startVal'].val = prefix + '_gabor.status == FINISHED'
    if mode == 'none':
        wf.params['stopType'].val = 'time (s)'
        wf.params['stopVal'].val = PRE + 1.5
    else:  # stays on until the routine ends (post-decision period)
        wf.params['stopType'].val = 'duration (s)'
        wf.params['stopVal'].val = ''
    resp = prefix + '_resp'
    add_keys(r, resp, "['f', 'j']", start=PRE, dur=1.5, force_end=False, correct=correct,
             cond=prefix + '_pre_fix.status == FINISHED')
    add_code(r, prefix + '_minexposure', **timing_code(resp, mode))
    if end:
        add_code(r, prefix + '_end', **end)
    return r


def phase_end(phase, tilt='tiltDeg', probe=0):
    return dict(
        py_end="thisExp.addData('phase', '%s')\n\n"
               "thisExp.addData('tiltDegUsed', %s)\nthisExp.addData('probeScheduled', %d)"
               % (phase, tilt, probe),
        js_end="psychoJS.experiment.addData('phase', '%s');\n"
               "\n"
               "psychoJS.experiment.addData('tiltDegUsed', %s);\n"
               "psychoJS.experiment.addData('probeScheduled', %d);" % (phase, tilt, probe))


def fix_routine(name, dur=0.5):
    r = new_routine(name)
    add_fix(r, name + '_fix', dur=dur)
    return r


def wrap_loop(loop, first, last):
    if loop.type == 'MultiStairHandler':  # writer in this PsychoPy build reads plain 'conditionsFile'
        loop.params['conditionsFile'] = Param(QUEST, valType='file', inputType='conditions', updates=None)
    """Insert loop around flow entries first..last (Routine names or loop objects)."""
    def index_of(target, want_end=False):
        for i, e in enumerate(exp.flow):
            if getattr(e, 'name', None) == target and type(e).__name__ == 'Routine':
                return i
        raise KeyError(target)
    a, b = index_of(first), index_of(last)
    exp.flow.addLoop(loop, a, b + 1)
    exp.requirePsychopyLibs(['data'])


def two_cond_loop(name, nReps):
    return TrialHandler(exp, name=name, loopType='random', nReps=nReps,
                        conditionsFile=TWO, conditions=data.importConditions(TWO),
                        isTrials=True)


# --------------------------------------------------------------- init + intro
space_screen('welcome', 'Welcome.\n\nPress SPACE to begin.')
space_screen('consent',
             'INFORMATION AND CONSENT\n\nThis study asks you to judge the tilt of brief '
             'striped patches using the keyboard. It lasts about 20-30 minutes. '
             'Participation is voluntary and you may stop at any time by pressing ESCAPE. '
             'No identifying information is collected.\n\n[Replace with the ethics-approved '
             'participant information and consent text.]\n\nPress SPACE to give consent '
             'and continue.')
# Counterbalancing: 3 equally likely groups (0=no_probe, 1=sparse_probe, 2=full_probe).
# 30 participants per group = 2 slots x 15 repeats (small batches keep groups balanced as data come in).
# Online, the Pavlovia Shelf record decides the caps; keep it consistent with these numbers.
# Depletion is handled in the `initialize` routine (the built-in end-on-depletion would also end participant 90).
cbr = CounterbalanceRoutine(exp, name='conditionAllocation', specMode='uniform', nGroups=3,
                            nSlots=2, nReps=15, endExperimentOnDepletion=False,
                            saveData=True, saveRemaining=True)
exp.addStandaloneRoutine('conditionAllocation', cbr)
exp.flow.addRoutine(cbr, len(exp.flow))
space_screen('instructions',
             'On each trial, you will see a striped patch tilted in one of two directions.'
             '\n\nPress F for a left-tilted patch.\nPress J for a right-tilted patch.\n\n'
             'Respond as accurately as possible. If you are unsure, make your best guess.\n'
             'Keep your index fingers on F and J throughout the task.\n\nPress SPACE to continue.')

PY_BEFORE = '''
def median_value(values):
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        return 8.0
    middle = n // 2
    if n % 2 == 1:
        return float(ordered[middle])
    return float((ordered[middle - 1] + ordered[middle]) / 2.0)
'''
PY_BEGIN_EXP = '''
probeCondition = ''
probeSchedule = []
for blockN in range(4):
    oneBlock = [1] * 10 + [0] * 30
    shuffle(oneBlock)
    probeSchedule.extend(oneBlock)

showConfInstr = 0
showNeutralInstr = 1
globalTrialN = 0
questLevels = []
tiltDeg = 8.0
probeThisTrial = 0
trialIndex = -1
choiceMade = 0
confidenceMade = 0
thisExp.addData('probeScheduleString', ''.join(str(p) for p in probeSchedule))
'''
JS_BEFORE = '''
var probeCondition = "";
var probeSchedule = [];
var globalTrialN = 0;
var questLevels = [];
var tiltDeg = 8.0;
var probeThisTrial = 0;
var trialIndex = -1;
var choiceMade = 0;
var confidenceMade = 0;
var showConfInstr = 0;
var showNeutralInstr = 1;
var feedbackText = "";
var feedbackColor = "white";
var blockText = "";
var breakText = "";
var FINISHED = PsychoJS.Status.FINISHED;  // used in the conditional start of *_wait_fix
var decisionEnd = -1;
var confRating = 0;
var confMoved = 0;
var confNKeysSeen = 0;
var confFirstT = '';
var confSubmitT = '';
var markerX = 0;
var markerOpacity = 0;
var calibTiltSign = 1;
var calibCorrAns = "j";

function shuffledCopy(values) {
    let output = values.slice();
    for (let i = output.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temporary = output[i];
        output[i] = output[j];
        output[j] = temporary;
    }
    return output;
}

function medianValue(values) {
    let ordered = values.slice().sort((a, b) => a - b);
    let n = ordered.length;
    if (n === 0) {
        return 8.0;
    }
    let middle = Math.floor(n / 2);
    if (n % 2 === 1) {
        return Number(ordered[middle]);
    }
    return Number((ordered[middle - 1] + ordered[middle]) / 2.0);
}
'''
JS_BEGIN_EXP = '''
probeSchedule = [];
for (let blockN = 0; blockN < 4; blockN++) {
    let oneBlock = Array(10).fill(1).concat(Array(30).fill(0));
    oneBlock = shuffledCopy(oneBlock);
    probeSchedule = probeSchedule.concat(oneBlock);
}

psychoJS.experiment.addData('probeScheduleString', probeSchedule.join(''));
'''
PY_RESOLVE = '''
requestedCondition = str(expInfo['condition']).strip().lower()
groupToCondition = {0: 'no_probe', 1: 'sparse_probe', 2: 'full_probe'}
if requestedCondition in ('', 'auto'):
    # PsychoPy flags `finished` when the LAST slot is handed out, so test for a missing group instead
    if conditionAllocation.group is None:
        print('No counterbalance slots remaining for this study.')
        quit(thisExp, win=win)
    probeCondition = groupToCondition[int(conditionAllocation.group)]
    conditionSource = 'counterbalance'
elif requestedCondition in groupToCondition.values():
    probeCondition = requestedCondition  # manual override (testing)
    conditionSource = 'manual'
else:
    raise ValueError('condition must be auto, no_probe, sparse_probe, or full_probe')
expInfo['condition'] = probeCondition
showConfInstr = int(probeCondition != 'no_probe')
showNeutralInstr = 1 - showConfInstr
thisExp.addData('assignedCondition', probeCondition)
thisExp.addData('conditionSource', conditionSource)
'''
JS_RESOLVE = '''
let requestedCondition = String(expInfo['condition']).trim().toLowerCase();
let groupToCondition = {0: 'no_probe', 1: 'sparse_probe', 2: 'full_probe'};
let conditionSource = '';
if (requestedCondition === '' || requestedCondition === 'auto') {
    if (conditionAllocation.group === undefined || conditionAllocation.group === null) {
        quitPsychoJS('No more slots remaining for this study.', true);
    }
    probeCondition = groupToCondition[Number(conditionAllocation.group)];
    conditionSource = 'counterbalance';
} else if (Object.values(groupToCondition).includes(requestedCondition)) {
    probeCondition = requestedCondition;  // manual override (testing)
    conditionSource = 'manual';
} else {
    throw new Error('condition must be auto, no_probe, sparse_probe, or full_probe');
}
expInfo['condition'] = probeCondition;
showConfInstr = (probeCondition !== 'no_probe') ? 1 : 0;
showNeutralInstr = 1 - showConfInstr;
psychoJS.experiment.addData('assignedCondition', probeCondition);
psychoJS.experiment.addData('conditionSource', conditionSource);
'''
r = new_routine('initialize', duration=0.05)
add_fix(r, 'init_fix', dur=0.05)
add_code(r, 'init_code', py_before=PY_BEFORE, py_begin_exp=PY_BEGIN_EXP, py_begin=PY_RESOLVE,
         js_before=JS_BEFORE, js_begin_exp=JS_BEGIN_EXP, js_begin=JS_RESOLVE)

# Condition-specific instructions via 0/1-rep loops
space_screen('confidence_instructions',
             'On some trials, you will also be asked how confident you are that your '
             'choice was correct.\n\nA scale from 1 to 6 will appear:\n1 means you were guessing, '
             '6 means you were very certain.\n\nPress F to move the marker left and J to move it '
             'right, then press SPACE to confirm. There is no time limit for the rating.\n\n'
             'Use the entire scale when appropriate. Confidence is about the choice you just '
             'made, not your general ability.\n\nPress SPACE to continue.')
wrap_loop(TrialHandler(exp, name='confidenceInstructionLoop', loopType='sequential',
                       nReps='showConfInstr', isTrials=False),
          'confidence_instructions', 'confidence_instructions')
space_screen('neutral_instructions',
             'After each decision, a fixation cross may remain on the screen briefly. '
             'Keep looking at the cross until the next patch appears.\n\nPress SPACE to continue.')
wrap_loop(TrialHandler(exp, name='neutralInstructionLoop', loopType='sequential',
                       nReps='showNeutralInstr', isTrials=False),
          'neutral_instructions', 'neutral_instructions')

# ----------------------------------------------------------------- practice
space_screen('practice_intro',
             'Practice: the patch is clearly tilted and you will get feedback.\n\n'
             'Press SPACE to start.')
decision_routine('practice', 'tiltSign * 12',
                 end=dict(py_end="thisExp.addData('phase', 'practice')\n"
                                 "",
                          js_end="psychoJS.experiment.addData('phase', 'practice');\n"
                                 ""))
r = new_routine('practice_feedback')
add_code(r, 'practice_feedback_code',
         py_begin="""
if not practice_resp.keys:
    feedbackText = ''  # no response: no feedback message
    feedbackColor = 'white'
elif practice_resp.corr == 1:
    feedbackText = 'Correct'
    feedbackColor = '#2ecc40'
else:
    feedbackText = 'Incorrect'
    feedbackColor = '#ff4136'
""",
         js_begin="""
if (practice_resp.keys === undefined || practice_resp.keys === null || practice_resp.keys.length === 0) {
    feedbackText = '';  // no response: no feedback message
    feedbackColor = 'white';
} else if (practice_resp.corr === 1) {
    feedbackText = 'Correct';
    feedbackColor = '#2ecc40';
} else {
    feedbackText = 'Incorrect';
    feedbackColor = '#ff4136';
}
""")
ft = add_text(r, 'practice_feedback_text', '$feedbackText', dur=0.6, height=0.06, repeat=True)
setp(ft, color='$feedbackColor')
every_repeat(ft, 'color')
wrap_loop(two_cond_loop('practiceTrials', 6), 'practice_decision', 'practice_feedback')

# -------------------------------------------------------------- calibration
space_screen('calibration_intro',
             'Calibration: the patch will get harder to see. No feedback now. Keep '
             'responding as accurately as you can.\n\nPress SPACE to start.')
# Distinct names: conditions-file variables (tiltSign, corrAns) are injected into globals by
# the loop machinery, and assigning them in run() would shadow them as locals.
SIGN_PY = """
if random() < 0.5:
    calibTiltSign = -1
    calibCorrAns = 'f'
else:
    calibTiltSign = 1
    calibCorrAns = 'j'
"""
SIGN_JS = """
if (Math.random() < 0.5) {
    calibTiltSign = -1;
    calibCorrAns = 'f';
} else {
    calibTiltSign = 1;
    calibCorrAns = 'j';
}
"""
CALIB_END_PY = """
questLevels.append(float(level))
thisExp.addData('phase', 'calibration')
thisExp.addData('tiltSignUsed', calibTiltSign)
thisExp.addData('corrAns', calibCorrAns)
"""
CALIB_END_JS = """
questLevels.push(Number(level));
psychoJS.experiment.addData('phase', 'calibration');
psychoJS.experiment.addData('tiltSignUsed', calibTiltSign);
psychoJS.experiment.addData('corrAns', calibCorrAns);
"""
decision_routine(
    'calibration', 'calibTiltSign * level', correct='$calibCorrAns',
    setup=dict(py_begin=SIGN_PY, js_begin=SIGN_JS),
    end=dict(py_end=CALIB_END_PY, js_end=CALIB_END_JS))
wrap_loop(MultiStairHandler(exp, name='calibrationTrials', nReps=40, stairType='QUEST',
                            switchStairs='sequential', conditionsFile=QUEST,
                            conditions=[], isTrials=True),
          'calibration_decision', 'calibration_decision')
r = new_routine('calibration_summary', duration=0.5)
add_code(r, 'calibration_summary_code',
         py_begin="lastLevels = questLevels[-10:]\ntiltDeg = median_value(lastLevels)\n"
                  "tiltDeg = min(max(tiltDeg, 1.0), 15.0)\n"
                  "thisExp.addData('calibratedTiltDeg', tiltDeg)\n"
                  "thisExp.addData('calibrationAtBoundary', int(tiltDeg <= 1.0 or tiltDeg >= 15.0))",
         js_begin="let lastLevels = questLevels.slice(-10);\ntiltDeg = medianValue(lastLevels);\n"
                  "tiltDeg = Math.min(Math.max(tiltDeg, 1.0), 15.0);\n"
                  "psychoJS.experiment.addData('calibratedTiltDeg', tiltDeg);\n"
                  "psychoJS.experiment.addData('calibrationAtBoundary', "
                  "(tiltDeg <= 1.0 || tiltDeg >= 15.0) ? 1 : 0);")
add_text(r, 'calibration_done_text', 'Calibration complete', dur=0.5, height=0.05)

# ----------------------------------------------------------------- baseline
space_screen('baseline_intro',
             'Next part. No confidence reports in this part.\n\nPress SPACE to start.')
decision_routine('baseline', 'tiltSign * tiltDeg', end=phase_end('baseline'), mode='tail')
wrap_loop(two_cond_loop('baselineTrials', 20), 'baseline_decision', 'baseline_decision')

# --------------------------------------------------------------------- main
space_screen('main_intro', 'Main task. Remember: F = left tilt, J = right tilt.\n\n'
                           'Press SPACE to start.')
r = new_routine('block_intro')
add_code(r, 'block_intro_code',
         py_begin="blockText = 'Block ' + str(mainBlocks.thisN + 1) + ' of 4\\n\\n"
                  "Press SPACE when you are ready.'",
         js_begin="blockText = 'Block ' + String(mainBlocks.thisN + 1) + ' of 4\\n\\n"
                  "Press SPACE when you are ready.';")
add_text(r, 'block_intro_text', '$blockText', repeat=True)
add_keys(r, 'block_intro_key', "['space']", force_end=True)

MAIN_SETUP_PY = ("trialIndex = globalTrialN\n\nif probeCondition == 'full_probe':\n    probeThisTrial = 1\n"
                 "elif probeCondition == 'sparse_probe':\n    probeThisTrial = int(probeSchedule[trialIndex])\n"
                 "else:\n    probeThisTrial = 0")
MAIN_SETUP_JS = ("trialIndex = globalTrialN;\n\nif (probeCondition === 'full_probe') {\n    probeThisTrial = 1;\n"
                 "} else if (probeCondition === 'sparse_probe') {\n    probeThisTrial = Number(probeSchedule[trialIndex]);\n"
                 "} else {\n    probeThisTrial = 0;\n}")
MAIN_END_PY = '''
choiceMade = 1 if main_resp.keys else 0
probeOriginallyScheduled = probeThisTrial
if choiceMade == 0:
    probeThisTrial = 0

thisExp.addData('phase', 'main')
thisExp.addData('trialIndex', trialIndex)
thisExp.addData('blockIndex', mainBlocks.thisN)
thisExp.addData('trialInBlock', mainTrials.thisN)
thisExp.addData('tiltDegUsed', tiltDeg)
thisExp.addData('tiltSignUsed', tiltSign)
thisExp.addData('probeOriginallyScheduled', probeOriginallyScheduled)
thisExp.addData('probeScheduled', probeThisTrial)
thisExp.addData('choiceMade', choiceMade)
thisExp.addData('confidenceRequested', probeThisTrial)
thisExp.addData('confidenceMade', 0)

globalTrialN += 1
'''
MAIN_END_JS = '''
choiceMade = (
    main_resp.keys !== undefined &&
    main_resp.keys !== null &&
    main_resp.keys.length > 0
) ? 1 : 0;
let probeOriginallyScheduled = probeThisTrial;
if (choiceMade === 0) {
    probeThisTrial = 0;
}

psychoJS.experiment.addData('phase', 'main');
psychoJS.experiment.addData('trialIndex', trialIndex);
psychoJS.experiment.addData('blockIndex', mainBlocks.thisN);
psychoJS.experiment.addData('trialInBlock', mainTrials.thisN);
psychoJS.experiment.addData('tiltDegUsed', tiltDeg);
psychoJS.experiment.addData('tiltSignUsed', tiltSign);
psychoJS.experiment.addData('probeOriginallyScheduled', probeOriginallyScheduled);
psychoJS.experiment.addData('probeScheduled', probeThisTrial);
psychoJS.experiment.addData('choiceMade', choiceMade);
psychoJS.experiment.addData('confidenceRequested', probeThisTrial);
psychoJS.experiment.addData('confidenceMade', 0);

globalTrialN += 1;
'''
decision_routine('main', 'tiltSign * tiltDeg',
                 setup=dict(py_begin=MAIN_SETUP_PY, js_begin=MAIN_SETUP_JS),
                 end=dict(py_end=MAIN_END_PY, js_end=MAIN_END_JS), mode='probe')

# Post-decision period.
#  * probe trial: self-paced confidence rating (F/J move a marker along 1-6, SPACE confirms, no time limit)
#  * non-probe trial: fixation cross for 1.5 s
# Two routines, each wrapped in a 0/1-rep loop driven by probeThisTrial.
r = new_routine('main_post_probe')
add_text(r, 'confidence_prompt', 'How confident are you that your choice was correct?',
         height=0.04, pos='(0, 0.22)')
for i in range(1, 7):
    add_text(r, 'conf_n%d' % i, str(i), height=0.06, pos='(%.2f, 0.02)' % ((i - 3.5) * 0.12))
add_text(r, 'conf_lab_lo', 'Guessing', height=0.03, pos='(%.2f, -0.07)' % (-2.5 * 0.12), wrap=0.3)
add_text(r, 'conf_lab_hi', 'Certain', height=0.03, pos='(%.2f, -0.07)' % (2.5 * 0.12), wrap=0.3)
add_text(r, 'conf_hint', 'F = move left     J = move right     SPACE = confirm',
         height=0.028, pos='(0, -0.22)')
mk = PolygonComponent(exp, r.name, name='conf_marker')
setp(mk, shape='triangle', size='(0.04, 0.04)', pos='(markerX, 0.09)', ori=180,
     opacity='markerOpacity', units='from exp settings')
mk.params['fillColor'].val = 'white'
mk.params['lineColor'].val = 'white'
mk.params['startVal'].val = 0
mk.params['stopType'].val = 'duration (s)'
mk.params['stopVal'].val = ''
every_frame = lambda c, *names: [setattr(c.params[n], 'updates', 'set every frame') for n in names]
every_frame(mk, 'pos', 'opacity')
r.addComponent(mk)
k = add_keys(r, 'confidence_resp', "['f', 'j', 'space']", force_end=False)
k.params['store'].val = 'all keys'
add_code(r, 'confidence_logic',
         py_begin="""
confRating = 0
confMoved = 0
confNKeysSeen = 0
confFirstT = ''
confSubmitT = ''
markerX = 0
markerOpacity = 0
""",
         js_begin="""
confRating = 0;
confMoved = 0;
confNKeysSeen = 0;
confFirstT = '';
confSubmitT = '';
markerX = 0;
markerOpacity = 0;
""",
         py_frame="""
allConfKeys = confidence_resp.keys if confidence_resp.keys else []
if isinstance(allConfKeys, str):
    allConfKeys = [allConfKeys]
for k in allConfKeys[confNKeysSeen:]:
    if k == 'f' or k == 'j':
        if confMoved == 0:
            confRating = 3 if k == 'f' else 4  # first press: one step from the midpoint
            confMoved = 1
            confFirstT = t
        elif k == 'f':
            confRating = max(1, confRating - 1)
        else:
            confRating = min(6, confRating + 1)
    elif k == 'space' and confMoved == 1:
        confSubmitT = t
        continueRoutine = False
confNKeysSeen = len(allConfKeys)
if confMoved == 1:
    markerX = (confRating - 3.5) * 0.12
    markerOpacity = 1
""",
         js_frame="""
let allConfKeys = (confidence_resp.keys === undefined || confidence_resp.keys === null) ? [] : confidence_resp.keys;
if (typeof allConfKeys === 'string') {
    allConfKeys = [allConfKeys];
}
for (let k of allConfKeys.slice(confNKeysSeen)) {
    if (k === 'f' || k === 'j') {
        if (confMoved === 0) {
            confRating = (k === 'f') ? 3 : 4;
            confMoved = 1;
            confFirstT = t;
        } else if (k === 'f') {
            confRating = Math.max(1, confRating - 1);
        } else {
            confRating = Math.min(6, confRating + 1);
        }
    } else if (k === 'space' && confMoved === 1) {
        confSubmitT = t;
        continueRoutine = false;
    }
}
confNKeysSeen = allConfKeys.length;
if (confMoved === 1) {
    markerX = (confRating - 3.5) * 0.12;
    markerOpacity = 1;
}
""",
         py_end="""
thisExp.addData('confidenceRating', confRating if confMoved == 1 else '')
thisExp.addData('confidenceRT', confSubmitT)
thisExp.addData('confidenceFirstMoveT', confFirstT)
thisExp.addData('confidenceMade', confMoved)
""",
         js_end="""
psychoJS.experiment.addData('confidenceRating', (confMoved === 1) ? confRating : '');
psychoJS.experiment.addData('confidenceRT', confSubmitT);
psychoJS.experiment.addData('confidenceFirstMoveT', confFirstT);
psychoJS.experiment.addData('confidenceMade', confMoved);
""")

wrap_loop(two_cond_loop('mainTrials', 20), 'main_decision', 'main_post_probe')
wrap_loop(TrialHandler(exp, name='confidenceProbeLoop', loopType='sequential',
                       nReps='probeThisTrial', isTrials=False), 'main_post_probe', 'main_post_probe')

r = new_routine('block_break')
add_code(r, 'block_break_code',
         py_begin="blockNumber = mainBlocks.thisN + 1\nif blockNumber < 4:\n"
                  "    breakText = ('End of block ' + str(blockNumber) + ' of 4.\\n\\n'\n"
                  "                 'Take a short break. Press SPACE to continue.')\nelse:\n"
                  "    breakText = 'The main task is complete. Press SPACE to continue.'",
         js_begin="let blockNumber = mainBlocks.thisN + 1;\nif (blockNumber < 4) {\n"
                  "    breakText = 'End of block ' + String(blockNumber) +\n"
                  "        ' of 4.\\n\\nTake a short break. Press SPACE to continue.';\n} else {\n"
                  "    breakText = 'The main task is complete. Press SPACE to continue.';\n}")
add_text(r, 'block_break_text', '$breakText', repeat=True)
add_keys(r, 'block_break_key', "['space']", force_end=True)
wrap_loop(TrialHandler(exp, name='mainBlocks', loopType='sequential', nReps=4,
                       isTrials=False), 'block_intro', 'block_break')

# ----------------------------------------------------------------- finish
# No post-task questions or debrief: the session ends with a timed message (auto-exit).
r = new_routine('thanks', duration=3)
add_text(r, 'thanks_text', 'The experiment is finished. Thank you!', dur=3, height=0.05)

exp.saveToXML('confidence_probe.psyexp')
print('wrote confidence_probe.psyexp')
