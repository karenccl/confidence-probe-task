#!/usr/bin/env python
"""Confidence-probe reactivity study (local PsychoPy / Coder version).

Between-participant conditions: no_probe, sparse_probe (40/160), full_probe (160/160).
Baseline and non-probe main trials have a fixed 1.5 s post-decision period. Probe trials use a
self-paced confidence rating (F/J move a marker along 1-6, SPACE confirms; no time limit).

Run:  python confidence_probe.py            (full session)
      python confidence_probe.py --quick    (short block sizes for technical testing)

Developed against PsychoPy 2026.1.3. Not yet run on hardware: do the Version 0.1-0.7
checks from the build plan and inspect the CSV before collecting data.
"""
import os
import sys
import random
from datetime import datetime

from psychopy import visual, core, data, gui, event, logging
from psychopy.hardware import keyboard

from helpers import (validate_condition, probe_for_trial, calibrated_tilt,
                     VALID_CONDITIONS)

QUICK = '--quick' in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

# ---------------------------------------------------------------- parameters
FIX_DUR = 0.5
ITI_DUR = 0.5
MAX_DECISION = 1.5
MIN_EXPOSURE = 0.15
POST_DUR = 1.5
FEEDBACK_DUR = 0.6
GABOR = dict(tex='sin', mask='gauss', size=0.18, sf=4, contrast=0.8, units='height')
PRACTICE_TILT = 12.0

if QUICK:
    N_PRACTICE_REPS, N_QUEST, N_BASELINE_REPS = 2, 10, 2
    N_BLOCKS, MAIN_REPS, PROBES_PER_BLOCK = 2, 5, 3
else:
    N_PRACTICE_REPS, N_QUEST, N_BASELINE_REPS = 6, 40, 20
    N_BLOCKS, MAIN_REPS, PROBES_PER_BLOCK = 4, 20, 10
TRIALS_PER_BLOCK = MAIN_REPS * 2

# ------------------------------------------------------------ session setup
expInfo = {'participant': 'test001', 'condition': 'sparse_probe'}
dlg = gui.DlgFromDict(expInfo, title='confidence_probe',
                      order=['participant', 'condition'],
                      fixed=[], tip={'condition': ', '.join(VALID_CONDITIONS)})
if not dlg.OK:
    core.quit()
condition = validate_condition(expInfo['condition'])
expInfo['date'] = datetime.now().strftime('%Y-%m-%d_%H%M%S')
expInfo['psychopyVersion'] = __import__('psychopy').__version__

os.makedirs('data', exist_ok=True)
fileName = 'data/%s_confidence_probe_%s' % (expInfo['participant'], expInfo['date'])
thisExp = data.ExperimentHandler(name='confidence_probe', extraInfo=expInfo,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=False, saveWideText=True,
                                 dataFileName=fileName)
logging.console.setLevel(logging.WARNING)
logging.LogFile(fileName + '.log', level=logging.EXP)

# Probe schedule: exactly PROBES_PER_BLOCK per block (used only by sparse_probe).
probeSchedule = []
for _ in range(N_BLOCKS):
    one = [1] * PROBES_PER_BLOCK + [0] * (TRIALS_PER_BLOCK - PROBES_PER_BLOCK)
    random.shuffle(one)
    probeSchedule.extend(one)
assert len(probeSchedule) == N_BLOCKS * TRIALS_PER_BLOCK
thisExp.addData('probeScheduleString', ''.join(str(p) for p in probeSchedule))

win = visual.Window(size=[1280, 720], fullscr=not QUICK, color=[0, 0, 0],
                    colorSpace='rgb', units='height', allowGUI=False)
win.mouseVisible = False
kb = keyboard.Keyboard()
trialClock = core.Clock()

fixation = visual.TextStim(win, text='+', height=0.05, color='white')
gabor = visual.GratingStim(win, pos=(0, 0), ori=0, **GABOR)
message = visual.TextStim(win, text='', height=0.035, wrapWidth=1.4, color='white')
feedbackStim = visual.TextStim(win, text='', height=0.06, color='white')
confidencePrompt = visual.TextStim(
    win, pos=(0, 0.22), height=0.04, wrapWidth=1.5, color='white',
    text='How confident are you that your choice was correct?')
confDigits = [visual.TextStim(win, text=str(i), pos=((i - 3.5) * 0.12, 0.02), height=0.06,
                              color='white') for i in range(1, 7)]
confLabels = [visual.TextStim(win, text='Guessing', pos=(-2.5 * 0.12, -0.07), height=0.03,
                              color='white'),
              visual.TextStim(win, text='Certain', pos=(2.5 * 0.12, -0.07), height=0.03,
                              color='white')]
confHint = visual.TextStim(win, text='F = move left     J = move right     SPACE = confirm',
                           pos=(0, -0.22), height=0.028, color='white')
confMarker = visual.ShapeStim(win, vertices=[(-0.02, 0.02), (0.02, 0.02), (0, -0.02)],
                              fillColor='white', lineColor='white')


class Quit(Exception):
    pass


def check_escape():
    if event.getKeys(['escape']):
        raise Quit()


def show_message(text, keys=('space',), height=None):
    message.text = text
    message.height = height or 0.035
    kb.clearEvents()
    while True:
        message.draw()
        win.flip()
        pressed = kb.getKeys(list(keys) + ['escape'], waitRelease=False)
        for k in pressed:
            if k.name == 'escape':
                raise Quit()
            return k.name


def timed_fixation(duration):
    """Fixation for a fixed duration (frame-counted against the clock)."""
    win.callOnFlip(trialClock.reset)
    frameN = 0
    while True:
        t = 0 if frameN == 0 else trialClock.getTime()
        if t >= duration - 0.5 * win.monitorFramePeriod:
            break
        fixation.draw()
        win.flip()
        check_escape()
        frameN += 1


def decision(tiltSign, corrAns, tiltDeg):
    """Gabor 0-0.15 s, fixation to the end; response allowed from stimulus onset;
    ends at the first response made after 0.15 s, or at 1.5 s.
    Returns (key, rt, correct) with None/None/None when omitted."""
    gabor.ori = tiltSign * tiltDeg
    kb.clearEvents()
    kb.clock.reset()
    win.callOnFlip(trialClock.reset)
    win.callOnFlip(kb.clock.reset)
    key = rt = None
    frameN = 0
    half = 0.5 * win.monitorFramePeriod
    while True:
        t = 0 if frameN == 0 else trialClock.getTime()
        if t >= MAX_DECISION - half:
            break
        if t < MIN_EXPOSURE - half:
            gabor.draw()  # no fixation cross while the grating is shown
        else:
            fixation.draw()
        win.flip()
        for k in kb.getKeys(['f', 'j', 'escape'], waitRelease=False):
            if k.name == 'escape':
                raise Quit()
            if key is None:
                key, rt = k.name, k.rt
        if key is not None and trialClock.getTime() >= MIN_EXPOSURE:
            break
        frameN += 1
    corr = None if key is None else int(key == corrAns)
    return key, rt, corr


def post_period(probe):
    """Non-probe: fixation for POST_DUR. Probe: self-paced confidence rating (no time limit);
    F/J move a marker along 1-6, SPACE confirms once the marker has been placed.
    Returns (rating, first_move_t, submit_t); all None for non-probe trials."""
    if not probe:
        timed_fixation(POST_DUR)
        return None, None, None
    kb.clearEvents()
    win.callOnFlip(trialClock.reset)
    rating, firstT, submitT = None, None, None
    frameN = 0
    while submitT is None:
        t = 0 if frameN == 0 else trialClock.getTime()
        confidencePrompt.draw()
        for d in confDigits:
            d.draw()
        for lab in confLabels:
            lab.draw()
        confHint.draw()
        if rating is not None:
            confMarker.pos = ((rating - 3.5) * 0.12, 0.09)
            confMarker.draw()
        win.flip()
        for k in kb.getKeys(['f', 'j', 'space', 'escape'], waitRelease=False):
            kt = trialClock.getTime()
            if k.name == 'escape':
                raise Quit()
            if k.name in ('f', 'j'):
                if rating is None:
                    rating = 3 if k.name == 'f' else 4  # one step from the midpoint
                    firstT = kt
                elif k.name == 'f':
                    rating = max(1, rating - 1)
                else:
                    rating = min(6, rating + 1)
            elif k.name == 'space' and rating is not None:
                submitT = kt
        frameN += 1
    return rating, firstT, submitT


def iti():
    timed_fixation(ITI_DUR)


def add_decision_data(prefix, key, rt, corr):
    thisExp.addData(prefix + '_resp.keys', key if key is not None else '')
    thisExp.addData(prefix + '_resp.rt', rt if rt is not None else '')
    thisExp.addData(prefix + '_resp.corr', corr if corr is not None else '')


def run_loop(handler_name, phase, nReps, tiltDeg, feedback=False, post=False):
    """Practice / baseline loop driven by conditions/two_orientations.csv."""
    conds = data.importConditions('conditions/two_orientations.csv')
    loop = data.TrialHandler(trialList=conds, nReps=nReps, method='random',
                             name=handler_name)
    thisExp.addLoop(loop)
    for trial in loop:
        timed_fixation(FIX_DUR)
        key, rt, corr = decision(trial['tiltSign'], trial['corrAns'], tiltDeg)
        if feedback:
            if key is None:
                feedbackStim.text, feedbackStim.color = '', 'white'  # no response: no message
            elif corr:
                feedbackStim.text, feedbackStim.color = 'Correct', '#2ecc40'
            else:
                feedbackStim.text, feedbackStim.color = 'Incorrect', '#ff4136'
            win.callOnFlip(trialClock.reset)
            fr = 0
            while fr == 0 or trialClock.getTime() < FEEDBACK_DUR:
                feedbackStim.draw()
                win.flip()
                check_escape()
                fr += 1
        if post:
            timed_fixation(POST_DUR)  # fixed, no confidence for anyone at baseline
        iti()
        thisExp.addData('phase', phase)
        thisExp.addData('condition', condition)
        thisExp.addData('tiltDegUsed', tiltDeg)
        thisExp.addData('tiltSignUsed', trial['tiltSign'])
        thisExp.addData('corrAns', trial['corrAns'])
        thisExp.addData('probeScheduled', 0)
        add_decision_data(phase, key, rt, corr)
        thisExp.nextEntry()


def run_calibration():
    q = data.importConditions('conditions/quest_conditions.csv')[0]
    staircase = data.QuestHandler(
        startVal=q['startVal'], startValSd=q['startValSd'], pThreshold=q['pThreshold'],
        nTrials=N_QUEST, minVal=q['minVal'], maxVal=q['maxVal'], beta=q['beta'],
        delta=q['delta'], gamma=q['gamma'], grain=q['grain'], method=q['method'],
        name='calibrationTrials')
    thisExp.addLoop(staircase)
    levels, omissions = [], 0
    for level in staircase:
        tiltSign = random.choice([-1, 1])
        corrAns = 'f' if tiltSign == -1 else 'j'
        timed_fixation(FIX_DUR)
        key, rt, corr = decision(tiltSign, corrAns, level)
        levels.append(float(level))
        if key is None:
            omissions += 1
        staircase.addResponse(corr if corr is not None else 0)  # omission = incorrect
        iti()
        thisExp.addData('phase', 'calibration')
        thisExp.addData('condition', condition)
        thisExp.addData('level', level)
        thisExp.addData('tiltSignUsed', tiltSign)
        thisExp.addData('corrAns', corrAns)
        add_decision_data('calibration', key, rt, corr)
        thisExp.nextEntry()
    tiltDeg, atBoundary = calibrated_tilt(levels)
    thisExp.addData('calibratedTiltDeg', tiltDeg)
    thisExp.addData('calibrationAtBoundary', atBoundary)
    thisExp.addData('calibrationOmissions', omissions)
    try:
        thisExp.addData('questMean', float(staircase.mean()))
        thisExp.addData('questMode', float(staircase.mode()))
    except Exception:
        pass
    thisExp.nextEntry()
    return tiltDeg


def run_main(tiltDeg):
    globalTrialN = 0
    for blockN in range(N_BLOCKS):
        show_message('Block %d of %d\n\nPress SPACE when you are ready.'
                     % (blockN + 1, N_BLOCKS))
        conds = data.importConditions('conditions/two_orientations.csv')
        loop = data.TrialHandler(trialList=conds, nReps=MAIN_REPS, method='random',
                                 name='mainTrials_block%d' % blockN)
        thisExp.addLoop(loop)
        for trial in loop:
            trialIndex = globalTrialN
            scheduled = probe_for_trial(condition, probeSchedule, trialIndex)
            timed_fixation(FIX_DUR)
            key, rt, corr = decision(trial['tiltSign'], trial['corrAns'], tiltDeg)
            choiceMade = int(key is not None)
            probeThisTrial = scheduled if choiceMade else 0  # no rating of a missed choice
            confRating, confFirstT, confSubmitT = post_period(probeThisTrial == 1)
            confidenceMade = int(confRating is not None)
            iti()
            thisExp.addData('phase', 'main')
            thisExp.addData('condition', condition)
            thisExp.addData('trialIndex', trialIndex)
            thisExp.addData('blockIndex', blockN)
            thisExp.addData('trialInBlock', loop.thisN)
            thisExp.addData('tiltDegUsed', tiltDeg)
            thisExp.addData('tiltSignUsed', trial['tiltSign'])
            thisExp.addData('corrAns', trial['corrAns'])
            add_decision_data('main', key, rt, corr)
            thisExp.addData('choiceMade', choiceMade)
            thisExp.addData('probeOriginallyScheduled', scheduled)
            thisExp.addData('probeScheduled', probeThisTrial)
            thisExp.addData('confidenceRequested', probeThisTrial)
            thisExp.addData('confidenceRating', confRating if confidenceMade else '')
            thisExp.addData('confidenceRT', confSubmitT if confidenceMade else '')
            thisExp.addData('confidenceFirstMoveT', confFirstT if confidenceMade else '')
            thisExp.addData('confidenceMade', confidenceMade)
            thisExp.nextEntry()
            globalTrialN += 1
        if blockN + 1 < N_BLOCKS:
            show_message('End of block %d of %d.\n\nTake a short break. '
                         'Press SPACE to continue.' % (blockN + 1, N_BLOCKS))
        else:
            show_message('The main task is complete. Press SPACE to continue.')


INSTRUCTIONS = (
    'On each trial, you will see a striped patch tilted in one of two directions.\n\n'
    'Press F for a left-tilted patch.\n'
    'Press J for a right-tilted patch.\n\n'
    'Respond as accurately as possible. If you are unsure, make your best guess.\n'
    'Keep your index fingers on F and J throughout the task.\n\n'
    'Press SPACE to continue.')
CONFIDENCE_INSTRUCTIONS = (
    'On some trials, you will also be asked how confident you are that your choice '
    'was correct.\n\nA scale from 1 to 6 will appear:\n1 means you were guessing, '
    '6 means you were very certain.\n\nPress F to move the marker left and J to move it '
    'right, then press SPACE to confirm. There is no time limit for the rating.\n\n'
    'Use the entire scale when appropriate. Confidence is about the choice you just '
    'made, not your general ability.\n\nPress SPACE to continue.')
NEUTRAL_INSTRUCTIONS = (
    'After each decision, a fixation cross may remain on the screen briefly. '
    'Keep looking at the cross until the next patch appears.\n\nPress SPACE to continue.')
CONSENT = (
    'INFORMATION AND CONSENT\n\n'
    'This study asks you to judge the tilt of brief striped patches using the keyboard. '
    'It lasts about 20-30 minutes. Participation is voluntary and you may stop at any '
    'time by pressing ESCAPE. No identifying information is collected.\n\n'
    '[Replace with the ethics-approved participant information and consent text.]\n\n'
    'Press SPACE to give consent and continue, or ESCAPE to withdraw.')
FINISHED = 'The experiment is finished. Thank you!'

# ------------------------------------------------------------------- session
completed = False
try:
    show_message('Welcome.\n\nPress SPACE to begin.')
    show_message(CONSENT)
    show_message(INSTRUCTIONS)
    show_message(NEUTRAL_INSTRUCTIONS if condition == 'no_probe'
                 else CONFIDENCE_INSTRUCTIONS)

    show_message('Practice: the patch is clearly tilted and you will get feedback.\n\n'
                 'Press SPACE to start.')
    run_loop('practiceTrials', 'practice', N_PRACTICE_REPS, PRACTICE_TILT, feedback=True)

    show_message('Calibration: the patch will get harder to see. No feedback now. '
                 'Keep responding as accurately as you can.\n\nPress SPACE to start.')
    tiltDeg = run_calibration()
    show_message('Calibration complete.\n\nPress SPACE to continue.')

    show_message('Next part. No confidence reports in this part.\n\n'
                 'Press SPACE to start.')
    run_loop('baselineTrials', 'baseline', N_BASELINE_REPS, tiltDeg, post=True)

    show_message('Main task. Remember: F = left tilt, J = right tilt.\n\n'
                 'Press SPACE to start.')
    run_main(tiltDeg)

    message.text = FINISHED
    message.height = 0.05
    win.callOnFlip(trialClock.reset)
    fr = 0
    while fr == 0 or trialClock.getTime() < 3.0:
        message.draw()
        win.flip()
        check_escape()
        fr += 1
    completed = True
except Quit:
    completed = False
finally:
    thisExp.addData('sessionCompleted', int(completed))
    thisExp.nextEntry()
    thisExp.saveAsWideText(fileName + '.csv', delim=',')
    win.close()
    core.quit()
