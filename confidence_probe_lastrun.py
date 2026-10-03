#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.4),
    on October 04, 2026, at 00:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from init_code
def median_value(values):
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        return 8.0
    middle = n // 2
    if n % 2 == 1:
        return float(ordered[middle])
    return float((ordered[middle - 1] + ordered[middle]) / 2.0)

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.4'
expName = 'confidence_probe'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': 'test001',
    'condition': 'auto',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = 'data/' + expInfo['participant'] + '_' + expName + '_' + expInfo['date']
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\chanc\\Downloads\\metaprobe\\confidence_probe_project\\confidence_probe_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='Welcome.\n\nPress SPACE to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    welcome_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "consent" ---
    consent_text = visual.TextStim(win=win, name='consent_text',
        text='INFORMATION AND CONSENT\n\nThis study asks you to judge the tilt of brief striped patches using the keyboard. It lasts about 20-30 minutes. Participation is voluntary and you may stop at any time by pressing ESCAPE. No identifying information is collected.\n\n[Replace with the ethics-approved participant information and consent text.]\n\nPress SPACE to give consent and continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    consent_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    expShelf = data.shelf.Shelf(scope='experiment', expPath=_thisDir)
    # create uniform conditions for conditionAllocation
    conditionAllocationConditions = []
    for n in range(3):
        conditionAllocationConditions.append({
            'group': n,
            'probability': 1/3,
            'cap': 2
        })
    
    # create counterbalance object for conditionAllocation 
    conditionAllocation = data.Counterbalancer(
        shelf=expShelf,
        entry='conditionAllocation',
        conditions=conditionAllocationConditions,
        nReps=15
    )
    
    # --- Initialize components for Routine "instructions" ---
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text='On each trial, you will see a striped patch tilted in one of two directions.\n\nPress F for a left-tilted patch.\nPress J for a right-tilted patch.\n\nRespond as accurately as possible. If you are unsure, make your best guess.\nKeep your index fingers on F and J throughout the task.\n\nPress SPACE to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instructions_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "initialize" ---
    init_fix = visual.TextStim(win=win, name='init_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from init_code
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
    
    
    # --- Initialize components for Routine "confidence_instructions" ---
    confidence_instructions_text = visual.TextStim(win=win, name='confidence_instructions_text',
        text='On some trials, you will also be asked how confident you are that your choice was correct.\n\nA scale from 1 to 6 will appear:\n1 means you were guessing, 6 means you were very certain.\n\nPress F to move the marker left and J to move it right, then press SPACE to confirm. There is no time limit for the rating.\n\nUse the entire scale when appropriate. Confidence is about the choice you just made, not your general ability.\n\nPress SPACE to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    confidence_instructions_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "neutral_instructions" ---
    neutral_instructions_text = visual.TextStim(win=win, name='neutral_instructions_text',
        text='After each decision, a fixation cross may remain on the screen briefly. Keep looking at the cross until the next patch appears.\n\nPress SPACE to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    neutral_instructions_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "practice_intro" ---
    practice_intro_text = visual.TextStim(win=win, name='practice_intro_text',
        text='Practice: the patch is clearly tilted and you will get feedback.\n\nPress SPACE to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_intro_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "practice_decision" ---
    practice_pre_fix = visual.TextStim(win=win, name='practice_pre_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_gabor = visual.GratingStim(
        win=win, name='practice_gabor',
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.18, 0.18), sf=4.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=0.8, blendmode='avg',
        texRes=128.0, interpolate=True, depth=-1.0)
    practice_wait_fix = visual.TextStim(win=win, name='practice_wait_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    practice_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "practice_feedback" ---
    practice_feedback_text = visual.TextStim(win=win, name='practice_feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "calibration_intro" ---
    calibration_intro_text = visual.TextStim(win=win, name='calibration_intro_text',
        text='Calibration: the patch will get harder to see. No feedback now. Keep responding as accurately as you can.\n\nPress SPACE to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    calibration_intro_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "calibration_decision" ---
    calibration_pre_fix = visual.TextStim(win=win, name='calibration_pre_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    calibration_gabor = visual.GratingStim(
        win=win, name='calibration_gabor',
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.18, 0.18), sf=4.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=0.8, blendmode='avg',
        texRes=128.0, interpolate=True, depth=-2.0)
    calibration_wait_fix = visual.TextStim(win=win, name='calibration_wait_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    calibration_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "calibration_summary" ---
    calibration_done_text = visual.TextStim(win=win, name='calibration_done_text',
        text='Calibration complete',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "baseline_intro" ---
    baseline_intro_text = visual.TextStim(win=win, name='baseline_intro_text',
        text='Next part. No confidence reports in this part.\n\nPress SPACE to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    baseline_intro_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "baseline_decision" ---
    baseline_pre_fix = visual.TextStim(win=win, name='baseline_pre_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    baseline_gabor = visual.GratingStim(
        win=win, name='baseline_gabor',
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.18, 0.18), sf=4.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=0.8, blendmode='avg',
        texRes=128.0, interpolate=True, depth=-1.0)
    baseline_wait_fix = visual.TextStim(win=win, name='baseline_wait_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    baseline_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "main_intro" ---
    main_intro_text = visual.TextStim(win=win, name='main_intro_text',
        text='Main task. Remember: F = left tilt, J = right tilt.\n\nPress SPACE to start.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_intro_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "block_intro" ---
    block_intro_text = visual.TextStim(win=win, name='block_intro_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    block_intro_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "main_decision" ---
    main_pre_fix = visual.TextStim(win=win, name='main_pre_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    main_gabor = visual.GratingStim(
        win=win, name='main_gabor',
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.18, 0.18), sf=4.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=0.8, blendmode='avg',
        texRes=128.0, interpolate=True, depth=-2.0)
    main_wait_fix = visual.TextStim(win=win, name='main_wait_fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    main_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "main_post_probe" ---
    confidence_prompt = visual.TextStim(win=win, name='confidence_prompt',
        text='How confident are you that your choice was correct?',
        font='Arial',
        pos=(0, 0.22), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    conf_n1 = visual.TextStim(win=win, name='conf_n1',
        text='1',
        font='Arial',
        pos=(-0.30, 0.02), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    conf_n2 = visual.TextStim(win=win, name='conf_n2',
        text='2',
        font='Arial',
        pos=(-0.18, 0.02), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    conf_n3 = visual.TextStim(win=win, name='conf_n3',
        text='3',
        font='Arial',
        pos=(-0.06, 0.02), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    conf_n4 = visual.TextStim(win=win, name='conf_n4',
        text='4',
        font='Arial',
        pos=(0.06, 0.02), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    conf_n5 = visual.TextStim(win=win, name='conf_n5',
        text='5',
        font='Arial',
        pos=(0.18, 0.02), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    conf_n6 = visual.TextStim(win=win, name='conf_n6',
        text='6',
        font='Arial',
        pos=(0.30, 0.02), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    conf_lab_lo = visual.TextStim(win=win, name='conf_lab_lo',
        text='Guessing',
        font='Arial',
        pos=(-0.30, -0.07), draggable=False, height=0.03, wrapWidth=0.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    conf_lab_hi = visual.TextStim(win=win, name='conf_lab_hi',
        text='Certain',
        font='Arial',
        pos=(0.30, -0.07), draggable=False, height=0.03, wrapWidth=0.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    conf_hint = visual.TextStim(win=win, name='conf_hint',
        text='F = move left     J = move right     SPACE = confirm',
        font='Arial',
        pos=(0, -0.22), draggable=False, height=0.028, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    conf_marker = visual.ShapeStim(
        win=win, name='conf_marker',
        size=(0.04, 0.04), vertices='triangle',
        ori=180.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-10.0, interpolate=True)
    confidence_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "block_break" ---
    block_break_text = visual.TextStim(win=win, name='block_break_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    block_break_key = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "thanks" ---
    thanks_text = visual.TextStim(win=win, name='thanks_text',
        text='The experiment is finished. Thank you!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[welcome_text, welcome_key],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for welcome_key
    welcome_key.keys = []
    welcome_key.rt = []
    _welcome_key_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    thisExp.currentRoutine = welcome
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text.started')
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *welcome_key* updates
        waitOnFlip = False
        
        # if welcome_key is starting this frame...
        if welcome_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            welcome_key.frameNStart = frameN  # exact frame index
            welcome_key.tStart = t  # local t and not account for scr refresh
            welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_key.started')
            # update status
            welcome_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_key.status == STARTED and not waitOnFlip:
            theseKeys = welcome_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcome_key_allKeys.extend(theseKeys)
            if len(_welcome_key_allKeys):
                welcome_key.keys = _welcome_key_allKeys[0].name  # just the first key pressed
                welcome_key.rt = _welcome_key_allKeys[0].rt
                welcome_key.duration = _welcome_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcome,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            welcome.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if welcome.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # check responses
    if welcome_key.keys in ['', [], None]:  # No response was made
        welcome_key.keys = None
    thisExp.addData('welcome_key.keys',welcome_key.keys)
    if welcome_key.keys != None:  # we had a response
        thisExp.addData('welcome_key.rt', welcome_key.rt)
        thisExp.addData('welcome_key.duration', welcome_key.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "consent" ---
    # create an object to store info about Routine consent
    consent = data.Routine(
        name='consent',
        components=[consent_text, consent_key],
    )
    consent.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for consent_key
    consent_key.keys = []
    consent_key.rt = []
    _consent_key_allKeys = []
    # store start times for consent
    consent.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    consent.tStart = globalClock.getTime(format='float')
    consent.status = STARTED
    thisExp.addData('consent.started', consent.tStart)
    consent.maxDuration = None
    # keep track of which components have finished
    consentComponents = consent.components
    for thisComponent in consent.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "consent" ---
    thisExp.currentRoutine = consent
    consent.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *consent_text* updates
        
        # if consent_text is starting this frame...
        if consent_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            consent_text.frameNStart = frameN  # exact frame index
            consent_text.tStart = t  # local t and not account for scr refresh
            consent_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent_text.started')
            # update status
            consent_text.status = STARTED
            consent_text.setAutoDraw(True)
        
        # if consent_text is active this frame...
        if consent_text.status == STARTED:
            # update params
            pass
        
        # *consent_key* updates
        waitOnFlip = False
        
        # if consent_key is starting this frame...
        if consent_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            consent_key.frameNStart = frameN  # exact frame index
            consent_key.tStart = t  # local t and not account for scr refresh
            consent_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent_key.started')
            # update status
            consent_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(consent_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(consent_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if consent_key.status == STARTED and not waitOnFlip:
            theseKeys = consent_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _consent_key_allKeys.extend(theseKeys)
            if len(_consent_key_allKeys):
                consent_key.keys = _consent_key_allKeys[0].name  # just the first key pressed
                consent_key.rt = _consent_key_allKeys[0].rt
                consent_key.duration = _consent_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=consent,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            consent.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if consent.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in consent.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent" ---
    for thisComponent in consent.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for consent
    consent.tStop = globalClock.getTime(format='float')
    consent.tStopRefresh = tThisFlipGlobal
    thisExp.addData('consent.stopped', consent.tStop)
    # check responses
    if consent_key.keys in ['', [], None]:  # No response was made
        consent_key.keys = None
    thisExp.addData('consent_key.keys',consent_key.keys)
    if consent_key.keys != None:  # we had a response
        thisExp.addData('consent_key.rt', consent_key.rt)
        thisExp.addData('consent_key.duration', consent_key.duration)
    thisExp.nextEntry()
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # get group from shelf
    conditionAllocation.allocateGroup()
    thisExp.addData('conditionAllocation.group', conditionAllocation.group)
    for _key, _val in conditionAllocation.params.items():
        thisExp.addData(f'conditionAllocation.{_key}', _val)
    thisExp.addData('conditionAllocation.remaining', conditionAllocation.remaining)
    thisExp.nextEntry()
    # the Routine "conditionAllocation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[instructions_text, instructions_key],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instructions_key
    instructions_key.keys = []
    instructions_key.rt = []
    _instructions_key_allKeys = []
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    thisExp.currentRoutine = instructions
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        
        # if instructions_text is starting this frame...
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_text.started')
            # update status
            instructions_text.status = STARTED
            instructions_text.setAutoDraw(True)
        
        # if instructions_text is active this frame...
        if instructions_text.status == STARTED:
            # update params
            pass
        
        # *instructions_key* updates
        waitOnFlip = False
        
        # if instructions_key is starting this frame...
        if instructions_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instructions_key.frameNStart = frameN  # exact frame index
            instructions_key.tStart = t  # local t and not account for scr refresh
            instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_key.started')
            # update status
            instructions_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructions_key.status == STARTED and not waitOnFlip:
            theseKeys = instructions_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instructions_key_allKeys.extend(theseKeys)
            if len(_instructions_key_allKeys):
                instructions_key.keys = _instructions_key_allKeys[0].name  # just the first key pressed
                instructions_key.rt = _instructions_key_allKeys[0].rt
                instructions_key.duration = _instructions_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # check responses
    if instructions_key.keys in ['', [], None]:  # No response was made
        instructions_key.keys = None
    thisExp.addData('instructions_key.keys',instructions_key.keys)
    if instructions_key.keys != None:  # we had a response
        thisExp.addData('instructions_key.rt', instructions_key.rt)
        thisExp.addData('instructions_key.duration', instructions_key.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "initialize" ---
    # create an object to store info about Routine initialize
    initialize = data.Routine(
        name='initialize',
        components=[init_fix],
    )
    initialize.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from init_code
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
    
    # store start times for initialize
    initialize.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    initialize.tStart = globalClock.getTime(format='float')
    initialize.status = STARTED
    thisExp.addData('initialize.started', initialize.tStart)
    initialize.maxDuration = 0.05
    # keep track of which components have finished
    initializeComponents = initialize.components
    for thisComponent in initialize.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "initialize" ---
    thisExp.currentRoutine = initialize
    initialize.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.05:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > initialize.maxDuration-frameTolerance:
            initialize.maxDurationReached = True
            continueRoutine = False
        
        # *init_fix* updates
        
        # if init_fix is starting this frame...
        if init_fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            init_fix.frameNStart = frameN  # exact frame index
            init_fix.tStart = t  # local t and not account for scr refresh
            init_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(init_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'init_fix.started')
            # update status
            init_fix.status = STARTED
            init_fix.setAutoDraw(True)
        
        # if init_fix is active this frame...
        if init_fix.status == STARTED:
            # update params
            pass
        
        # if init_fix is stopping this frame...
        if init_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > init_fix.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                init_fix.tStop = t  # not accounting for scr refresh
                init_fix.tStopRefresh = tThisFlipGlobal  # on global time
                init_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'init_fix.stopped')
                # update status
                init_fix.status = FINISHED
                init_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=initialize,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            initialize.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if initialize.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in initialize.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "initialize" ---
    for thisComponent in initialize.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for initialize
    initialize.tStop = globalClock.getTime(format='float')
    initialize.tStopRefresh = tThisFlipGlobal
    thisExp.addData('initialize.stopped', initialize.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if initialize.maxDurationReached:
        routineTimer.addTime(-initialize.maxDuration)
    elif initialize.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.050000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    confidenceInstructionLoop = data.TrialHandler2(
        name='confidenceInstructionLoop',
        nReps=showConfInstr, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=False, 
    )
    thisExp.addLoop(confidenceInstructionLoop)  # add the loop to the experiment
    thisConfidenceInstructionLoop = confidenceInstructionLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisConfidenceInstructionLoop.rgb)
    if thisConfidenceInstructionLoop != None:
        for paramName in thisConfidenceInstructionLoop:
            globals()[paramName] = thisConfidenceInstructionLoop[paramName]
    
    for thisConfidenceInstructionLoop in confidenceInstructionLoop:
        confidenceInstructionLoop.status = STARTED
        if hasattr(thisConfidenceInstructionLoop, 'status'):
            thisConfidenceInstructionLoop.status = STARTED
        currentLoop = confidenceInstructionLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisConfidenceInstructionLoop.rgb)
        if thisConfidenceInstructionLoop != None:
            for paramName in thisConfidenceInstructionLoop:
                globals()[paramName] = thisConfidenceInstructionLoop[paramName]
        
        # --- Prepare to start Routine "confidence_instructions" ---
        # create an object to store info about Routine confidence_instructions
        confidence_instructions = data.Routine(
            name='confidence_instructions',
            components=[confidence_instructions_text, confidence_instructions_key],
        )
        confidence_instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for confidence_instructions_key
        confidence_instructions_key.keys = []
        confidence_instructions_key.rt = []
        _confidence_instructions_key_allKeys = []
        # store start times for confidence_instructions
        confidence_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        confidence_instructions.tStart = globalClock.getTime(format='float')
        confidence_instructions.status = STARTED
        thisExp.addData('confidence_instructions.started', confidence_instructions.tStart)
        confidence_instructions.maxDuration = None
        # keep track of which components have finished
        confidence_instructionsComponents = confidence_instructions.components
        for thisComponent in confidence_instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "confidence_instructions" ---
        thisExp.currentRoutine = confidence_instructions
        confidence_instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisConfidenceInstructionLoop, 'status') and thisConfidenceInstructionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *confidence_instructions_text* updates
            
            # if confidence_instructions_text is starting this frame...
            if confidence_instructions_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                confidence_instructions_text.frameNStart = frameN  # exact frame index
                confidence_instructions_text.tStart = t  # local t and not account for scr refresh
                confidence_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_instructions_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidence_instructions_text.started')
                # update status
                confidence_instructions_text.status = STARTED
                confidence_instructions_text.setAutoDraw(True)
            
            # if confidence_instructions_text is active this frame...
            if confidence_instructions_text.status == STARTED:
                # update params
                pass
            
            # *confidence_instructions_key* updates
            waitOnFlip = False
            
            # if confidence_instructions_key is starting this frame...
            if confidence_instructions_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                confidence_instructions_key.frameNStart = frameN  # exact frame index
                confidence_instructions_key.tStart = t  # local t and not account for scr refresh
                confidence_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_instructions_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidence_instructions_key.started')
                # update status
                confidence_instructions_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(confidence_instructions_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(confidence_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if confidence_instructions_key.status == STARTED and not waitOnFlip:
                theseKeys = confidence_instructions_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _confidence_instructions_key_allKeys.extend(theseKeys)
                if len(_confidence_instructions_key_allKeys):
                    confidence_instructions_key.keys = _confidence_instructions_key_allKeys[0].name  # just the first key pressed
                    confidence_instructions_key.rt = _confidence_instructions_key_allKeys[0].rt
                    confidence_instructions_key.duration = _confidence_instructions_key_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=confidence_instructions,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                confidence_instructions.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if confidence_instructions.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in confidence_instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "confidence_instructions" ---
        for thisComponent in confidence_instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for confidence_instructions
        confidence_instructions.tStop = globalClock.getTime(format='float')
        confidence_instructions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('confidence_instructions.stopped', confidence_instructions.tStop)
        # check responses
        if confidence_instructions_key.keys in ['', [], None]:  # No response was made
            confidence_instructions_key.keys = None
        confidenceInstructionLoop.addData('confidence_instructions_key.keys',confidence_instructions_key.keys)
        if confidence_instructions_key.keys != None:  # we had a response
            confidenceInstructionLoop.addData('confidence_instructions_key.rt', confidence_instructions_key.rt)
            confidenceInstructionLoop.addData('confidence_instructions_key.duration', confidence_instructions_key.duration)
        # the Routine "confidence_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisConfidenceInstructionLoop as finished
        if hasattr(thisConfidenceInstructionLoop, 'status'):
            thisConfidenceInstructionLoop.status = FINISHED
        # if awaiting a pause, pause now
        if confidenceInstructionLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            confidenceInstructionLoop.status = STARTED
    # completed showConfInstr repeats of 'confidenceInstructionLoop'
    confidenceInstructionLoop.status = FINISHED
    
    
    # set up handler to look after randomisation of conditions etc
    neutralInstructionLoop = data.TrialHandler2(
        name='neutralInstructionLoop',
        nReps=showNeutralInstr, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=False, 
    )
    thisExp.addLoop(neutralInstructionLoop)  # add the loop to the experiment
    thisNeutralInstructionLoop = neutralInstructionLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNeutralInstructionLoop.rgb)
    if thisNeutralInstructionLoop != None:
        for paramName in thisNeutralInstructionLoop:
            globals()[paramName] = thisNeutralInstructionLoop[paramName]
    
    for thisNeutralInstructionLoop in neutralInstructionLoop:
        neutralInstructionLoop.status = STARTED
        if hasattr(thisNeutralInstructionLoop, 'status'):
            thisNeutralInstructionLoop.status = STARTED
        currentLoop = neutralInstructionLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisNeutralInstructionLoop.rgb)
        if thisNeutralInstructionLoop != None:
            for paramName in thisNeutralInstructionLoop:
                globals()[paramName] = thisNeutralInstructionLoop[paramName]
        
        # --- Prepare to start Routine "neutral_instructions" ---
        # create an object to store info about Routine neutral_instructions
        neutral_instructions = data.Routine(
            name='neutral_instructions',
            components=[neutral_instructions_text, neutral_instructions_key],
        )
        neutral_instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for neutral_instructions_key
        neutral_instructions_key.keys = []
        neutral_instructions_key.rt = []
        _neutral_instructions_key_allKeys = []
        # store start times for neutral_instructions
        neutral_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        neutral_instructions.tStart = globalClock.getTime(format='float')
        neutral_instructions.status = STARTED
        thisExp.addData('neutral_instructions.started', neutral_instructions.tStart)
        neutral_instructions.maxDuration = None
        # keep track of which components have finished
        neutral_instructionsComponents = neutral_instructions.components
        for thisComponent in neutral_instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "neutral_instructions" ---
        thisExp.currentRoutine = neutral_instructions
        neutral_instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisNeutralInstructionLoop, 'status') and thisNeutralInstructionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *neutral_instructions_text* updates
            
            # if neutral_instructions_text is starting this frame...
            if neutral_instructions_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                neutral_instructions_text.frameNStart = frameN  # exact frame index
                neutral_instructions_text.tStart = t  # local t and not account for scr refresh
                neutral_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(neutral_instructions_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'neutral_instructions_text.started')
                # update status
                neutral_instructions_text.status = STARTED
                neutral_instructions_text.setAutoDraw(True)
            
            # if neutral_instructions_text is active this frame...
            if neutral_instructions_text.status == STARTED:
                # update params
                pass
            
            # *neutral_instructions_key* updates
            waitOnFlip = False
            
            # if neutral_instructions_key is starting this frame...
            if neutral_instructions_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                neutral_instructions_key.frameNStart = frameN  # exact frame index
                neutral_instructions_key.tStart = t  # local t and not account for scr refresh
                neutral_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(neutral_instructions_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'neutral_instructions_key.started')
                # update status
                neutral_instructions_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(neutral_instructions_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(neutral_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if neutral_instructions_key.status == STARTED and not waitOnFlip:
                theseKeys = neutral_instructions_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _neutral_instructions_key_allKeys.extend(theseKeys)
                if len(_neutral_instructions_key_allKeys):
                    neutral_instructions_key.keys = _neutral_instructions_key_allKeys[0].name  # just the first key pressed
                    neutral_instructions_key.rt = _neutral_instructions_key_allKeys[0].rt
                    neutral_instructions_key.duration = _neutral_instructions_key_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=neutral_instructions,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                neutral_instructions.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if neutral_instructions.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in neutral_instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "neutral_instructions" ---
        for thisComponent in neutral_instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for neutral_instructions
        neutral_instructions.tStop = globalClock.getTime(format='float')
        neutral_instructions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('neutral_instructions.stopped', neutral_instructions.tStop)
        # check responses
        if neutral_instructions_key.keys in ['', [], None]:  # No response was made
            neutral_instructions_key.keys = None
        neutralInstructionLoop.addData('neutral_instructions_key.keys',neutral_instructions_key.keys)
        if neutral_instructions_key.keys != None:  # we had a response
            neutralInstructionLoop.addData('neutral_instructions_key.rt', neutral_instructions_key.rt)
            neutralInstructionLoop.addData('neutral_instructions_key.duration', neutral_instructions_key.duration)
        # the Routine "neutral_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisNeutralInstructionLoop as finished
        if hasattr(thisNeutralInstructionLoop, 'status'):
            thisNeutralInstructionLoop.status = FINISHED
        # if awaiting a pause, pause now
        if neutralInstructionLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            neutralInstructionLoop.status = STARTED
    # completed showNeutralInstr repeats of 'neutralInstructionLoop'
    neutralInstructionLoop.status = FINISHED
    
    
    # --- Prepare to start Routine "practice_intro" ---
    # create an object to store info about Routine practice_intro
    practice_intro = data.Routine(
        name='practice_intro',
        components=[practice_intro_text, practice_intro_key],
    )
    practice_intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for practice_intro_key
    practice_intro_key.keys = []
    practice_intro_key.rt = []
    _practice_intro_key_allKeys = []
    # store start times for practice_intro
    practice_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice_intro.tStart = globalClock.getTime(format='float')
    practice_intro.status = STARTED
    thisExp.addData('practice_intro.started', practice_intro.tStart)
    practice_intro.maxDuration = None
    # keep track of which components have finished
    practice_introComponents = practice_intro.components
    for thisComponent in practice_intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice_intro" ---
    thisExp.currentRoutine = practice_intro
    practice_intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_intro_text* updates
        
        # if practice_intro_text is starting this frame...
        if practice_intro_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_intro_text.frameNStart = frameN  # exact frame index
            practice_intro_text.tStart = t  # local t and not account for scr refresh
            practice_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_intro_text.started')
            # update status
            practice_intro_text.status = STARTED
            practice_intro_text.setAutoDraw(True)
        
        # if practice_intro_text is active this frame...
        if practice_intro_text.status == STARTED:
            # update params
            pass
        
        # *practice_intro_key* updates
        waitOnFlip = False
        
        # if practice_intro_key is starting this frame...
        if practice_intro_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_intro_key.frameNStart = frameN  # exact frame index
            practice_intro_key.tStart = t  # local t and not account for scr refresh
            practice_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_intro_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_intro_key.started')
            # update status
            practice_intro_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_intro_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_intro_key.status == STARTED and not waitOnFlip:
            theseKeys = practice_intro_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _practice_intro_key_allKeys.extend(theseKeys)
            if len(_practice_intro_key_allKeys):
                practice_intro_key.keys = _practice_intro_key_allKeys[0].name  # just the first key pressed
                practice_intro_key.rt = _practice_intro_key_allKeys[0].rt
                practice_intro_key.duration = _practice_intro_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=practice_intro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            practice_intro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if practice_intro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in practice_intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_intro" ---
    for thisComponent in practice_intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice_intro
    practice_intro.tStop = globalClock.getTime(format='float')
    practice_intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice_intro.stopped', practice_intro.tStop)
    # check responses
    if practice_intro_key.keys in ['', [], None]:  # No response was made
        practice_intro_key.keys = None
    thisExp.addData('practice_intro_key.keys',practice_intro_key.keys)
    if practice_intro_key.keys != None:  # we had a response
        thisExp.addData('practice_intro_key.rt', practice_intro_key.rt)
        thisExp.addData('practice_intro_key.duration', practice_intro_key.duration)
    thisExp.nextEntry()
    # the Routine "practice_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceTrials = data.TrialHandler2(
        name='practiceTrials',
        nReps=6, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions/two_orientations.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(practiceTrials)  # add the loop to the experiment
    thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            globals()[paramName] = thisPracticeTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeTrial in practiceTrials:
        practiceTrials.status = STARTED
        if hasattr(thisPracticeTrial, 'status'):
            thisPracticeTrial.status = STARTED
        currentLoop = practiceTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                globals()[paramName] = thisPracticeTrial[paramName]
        
        # --- Prepare to start Routine "practice_decision" ---
        # create an object to store info about Routine practice_decision
        practice_decision = data.Routine(
            name='practice_decision',
            components=[practice_pre_fix, practice_gabor, practice_wait_fix, practice_resp],
        )
        practice_decision.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        practice_gabor.setOri(tiltSign * 12)
        # create starting attributes for practice_resp
        practice_resp.keys = []
        practice_resp.rt = []
        _practice_resp_allKeys = []
        # Run 'Begin Routine' code from practice_minexposure
        decisionEnd = -1
        
        # store start times for practice_decision
        practice_decision.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_decision.tStart = globalClock.getTime(format='float')
        practice_decision.status = STARTED
        thisExp.addData('practice_decision.started', practice_decision.tStart)
        practice_decision.maxDuration = None
        # keep track of which components have finished
        practice_decisionComponents = practice_decision.components
        for thisComponent in practice_decision.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_decision" ---
        thisExp.currentRoutine = practice_decision
        practice_decision.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeTrial, 'status') and thisPracticeTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_pre_fix* updates
            
            # if practice_pre_fix is starting this frame...
            if practice_pre_fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                practice_pre_fix.frameNStart = frameN  # exact frame index
                practice_pre_fix.tStart = t  # local t and not account for scr refresh
                practice_pre_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_pre_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_pre_fix.started')
                # update status
                practice_pre_fix.status = STARTED
                practice_pre_fix.setAutoDraw(True)
            
            # if practice_pre_fix is active this frame...
            if practice_pre_fix.status == STARTED:
                # update params
                pass
            
            # if practice_pre_fix is stopping this frame...
            if practice_pre_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_pre_fix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_pre_fix.tStop = t  # not accounting for scr refresh
                    practice_pre_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_pre_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_pre_fix.stopped')
                    # update status
                    practice_pre_fix.status = FINISHED
                    practice_pre_fix.setAutoDraw(False)
            
            # *practice_gabor* updates
            
            # if practice_gabor is starting this frame...
            if practice_gabor.status == NOT_STARTED and practice_pre_fix.status == FINISHED:
                # keep track of start time/frame for later
                practice_gabor.frameNStart = frameN  # exact frame index
                practice_gabor.tStart = t  # local t and not account for scr refresh
                practice_gabor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_gabor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_gabor.started')
                # update status
                practice_gabor.status = STARTED
                practice_gabor.setAutoDraw(True)
            
            # if practice_gabor is active this frame...
            if practice_gabor.status == STARTED:
                # update params
                pass
            
            # if practice_gabor is stopping this frame...
            if practice_gabor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_gabor.tStartRefresh + 0.15-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_gabor.tStop = t  # not accounting for scr refresh
                    practice_gabor.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_gabor.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_gabor.stopped')
                    # update status
                    practice_gabor.status = FINISHED
                    practice_gabor.setAutoDraw(False)
            
            # *practice_wait_fix* updates
            
            # if practice_wait_fix is starting this frame...
            if practice_wait_fix.status == NOT_STARTED and practice_gabor.status == FINISHED:
                # keep track of start time/frame for later
                practice_wait_fix.frameNStart = frameN  # exact frame index
                practice_wait_fix.tStart = t  # local t and not account for scr refresh
                practice_wait_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_wait_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_wait_fix.started')
                # update status
                practice_wait_fix.status = STARTED
                practice_wait_fix.setAutoDraw(True)
            
            # if practice_wait_fix is active this frame...
            if practice_wait_fix.status == STARTED:
                # update params
                pass
            
            # if practice_wait_fix is stopping this frame...
            if practice_wait_fix.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_wait_fix.tStop = t  # not accounting for scr refresh
                    practice_wait_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_wait_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_wait_fix.stopped')
                    # update status
                    practice_wait_fix.status = FINISHED
                    practice_wait_fix.setAutoDraw(False)
            
            # *practice_resp* updates
            waitOnFlip = False
            
            # if practice_resp is starting this frame...
            if practice_resp.status == NOT_STARTED and practice_pre_fix.status == FINISHED:
                # keep track of start time/frame for later
                practice_resp.frameNStart = frameN  # exact frame index
                practice_resp.tStart = t  # local t and not account for scr refresh
                practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_resp.started')
                # update status
                practice_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if practice_resp is stopping this frame...
            if practice_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_resp.tStop = t  # not accounting for scr refresh
                    practice_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_resp.stopped')
                    # update status
                    practice_resp.status = FINISHED
                    practice_resp.status = FINISHED
            if practice_resp.status == STARTED and not waitOnFlip:
                theseKeys = practice_resp.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _practice_resp_allKeys.extend(theseKeys)
                if len(_practice_resp_allKeys):
                    practice_resp.keys = _practice_resp_allKeys[0].name  # just the first key pressed
                    practice_resp.rt = _practice_resp_allKeys[0].rt
                    practice_resp.duration = _practice_resp_allKeys[0].duration
                    # was this correct?
                    if (practice_resp.keys == str(corrAns)) or (practice_resp.keys == corrAns):
                        practice_resp.corr = 1
                    else:
                        practice_resp.corr = 0
            # Run 'Each Frame' code from practice_minexposure
            if decisionEnd < 0:
                if practice_resp.keys and t >= 1.0 + 0.15:
                    decisionEnd = t
                elif t >= 1.0 + 1.5:
                    decisionEnd = t
            if decisionEnd >= 0:
                if True:
                    continueRoutine = False
                elif t >= decisionEnd + 1.5:
                    continueRoutine = False
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practice_decision,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                practice_decision.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if practice_decision.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in practice_decision.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_decision" ---
        for thisComponent in practice_decision.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_decision
        practice_decision.tStop = globalClock.getTime(format='float')
        practice_decision.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_decision.stopped', practice_decision.tStop)
        # check responses
        if practice_resp.keys in ['', [], None]:  # No response was made
            practice_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               practice_resp.corr = 1;  # correct non-response
            else:
               practice_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceTrials (TrialHandler)
        practiceTrials.addData('practice_resp.keys',practice_resp.keys)
        practiceTrials.addData('practice_resp.corr', practice_resp.corr)
        if practice_resp.keys != None:  # we had a response
            practiceTrials.addData('practice_resp.rt', practice_resp.rt)
            practiceTrials.addData('practice_resp.duration', practice_resp.duration)
        # Run 'End Routine' code from practice_end
        thisExp.addData('phase', 'practice')
        
        # the Routine "practice_decision" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_feedback" ---
        # create an object to store info about Routine practice_feedback
        practice_feedback = data.Routine(
            name='practice_feedback',
            components=[practice_feedback_text],
        )
        practice_feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from practice_feedback_code
        if not practice_resp.keys:
            feedbackText = ''  # no response: no feedback message
            feedbackColor = 'white'
        elif practice_resp.corr == 1:
            feedbackText = 'Correct'
            feedbackColor = '#2ecc40'
        else:
            feedbackText = 'Incorrect'
            feedbackColor = '#ff4136'
        
        practice_feedback_text.setColor(feedbackColor, colorSpace='rgb')
        practice_feedback_text.setText(feedbackText)
        # store start times for practice_feedback
        practice_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_feedback.tStart = globalClock.getTime(format='float')
        practice_feedback.status = STARTED
        thisExp.addData('practice_feedback.started', practice_feedback.tStart)
        practice_feedback.maxDuration = None
        # keep track of which components have finished
        practice_feedbackComponents = practice_feedback.components
        for thisComponent in practice_feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_feedback" ---
        thisExp.currentRoutine = practice_feedback
        practice_feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.6:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeTrial, 'status') and thisPracticeTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_feedback_text* updates
            
            # if practice_feedback_text is starting this frame...
            if practice_feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                practice_feedback_text.frameNStart = frameN  # exact frame index
                practice_feedback_text.tStart = t  # local t and not account for scr refresh
                practice_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_feedback_text.started')
                # update status
                practice_feedback_text.status = STARTED
                practice_feedback_text.setAutoDraw(True)
            
            # if practice_feedback_text is active this frame...
            if practice_feedback_text.status == STARTED:
                # update params
                pass
            
            # if practice_feedback_text is stopping this frame...
            if practice_feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_feedback_text.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_feedback_text.tStop = t  # not accounting for scr refresh
                    practice_feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_feedback_text.stopped')
                    # update status
                    practice_feedback_text.status = FINISHED
                    practice_feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practice_feedback,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                practice_feedback.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if practice_feedback.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in practice_feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_feedback" ---
        for thisComponent in practice_feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_feedback
        practice_feedback.tStop = globalClock.getTime(format='float')
        practice_feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_feedback.stopped', practice_feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if practice_feedback.maxDurationReached:
            routineTimer.addTime(-practice_feedback.maxDuration)
        elif practice_feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.600000)
        # mark thisPracticeTrial as finished
        if hasattr(thisPracticeTrial, 'status'):
            thisPracticeTrial.status = FINISHED
        # if awaiting a pause, pause now
        if practiceTrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceTrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 6 repeats of 'practiceTrials'
    practiceTrials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "calibration_intro" ---
    # create an object to store info about Routine calibration_intro
    calibration_intro = data.Routine(
        name='calibration_intro',
        components=[calibration_intro_text, calibration_intro_key],
    )
    calibration_intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for calibration_intro_key
    calibration_intro_key.keys = []
    calibration_intro_key.rt = []
    _calibration_intro_key_allKeys = []
    # store start times for calibration_intro
    calibration_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    calibration_intro.tStart = globalClock.getTime(format='float')
    calibration_intro.status = STARTED
    thisExp.addData('calibration_intro.started', calibration_intro.tStart)
    calibration_intro.maxDuration = None
    # keep track of which components have finished
    calibration_introComponents = calibration_intro.components
    for thisComponent in calibration_intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "calibration_intro" ---
    thisExp.currentRoutine = calibration_intro
    calibration_intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *calibration_intro_text* updates
        
        # if calibration_intro_text is starting this frame...
        if calibration_intro_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            calibration_intro_text.frameNStart = frameN  # exact frame index
            calibration_intro_text.tStart = t  # local t and not account for scr refresh
            calibration_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calibration_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calibration_intro_text.started')
            # update status
            calibration_intro_text.status = STARTED
            calibration_intro_text.setAutoDraw(True)
        
        # if calibration_intro_text is active this frame...
        if calibration_intro_text.status == STARTED:
            # update params
            pass
        
        # *calibration_intro_key* updates
        waitOnFlip = False
        
        # if calibration_intro_key is starting this frame...
        if calibration_intro_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            calibration_intro_key.frameNStart = frameN  # exact frame index
            calibration_intro_key.tStart = t  # local t and not account for scr refresh
            calibration_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calibration_intro_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calibration_intro_key.started')
            # update status
            calibration_intro_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(calibration_intro_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(calibration_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if calibration_intro_key.status == STARTED and not waitOnFlip:
            theseKeys = calibration_intro_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _calibration_intro_key_allKeys.extend(theseKeys)
            if len(_calibration_intro_key_allKeys):
                calibration_intro_key.keys = _calibration_intro_key_allKeys[0].name  # just the first key pressed
                calibration_intro_key.rt = _calibration_intro_key_allKeys[0].rt
                calibration_intro_key.duration = _calibration_intro_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=calibration_intro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            calibration_intro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if calibration_intro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in calibration_intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calibration_intro" ---
    for thisComponent in calibration_intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for calibration_intro
    calibration_intro.tStop = globalClock.getTime(format='float')
    calibration_intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('calibration_intro.stopped', calibration_intro.tStop)
    # check responses
    if calibration_intro_key.keys in ['', [], None]:  # No response was made
        calibration_intro_key.keys = None
    thisExp.addData('calibration_intro_key.keys',calibration_intro_key.keys)
    if calibration_intro_key.keys != None:  # we had a response
        thisExp.addData('calibration_intro_key.rt', calibration_intro_key.rt)
        thisExp.addData('calibration_intro_key.duration', calibration_intro_key.duration)
    thisExp.nextEntry()
    # the Routine "calibration_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of trials etc
    conditions = data.importConditions('conditions/quest_conditions.csv')
    calibrationTrials = data.MultiStairHandler(
        stairType='QUEST',     name='calibrationTrials',
        nTrials=40.0,
        conditions=conditions,
        method='sequential',
        originPath=-1,
        isTrials=True)
    thisExp.addLoop(calibrationTrials)  # add the loop to the experiment
    # initialise values for first condition
    level = calibrationTrials._nextIntensity  # initialise some vals
    condition = calibrationTrials.currentStaircase.condition
    
    for level, condition in calibrationTrials:
        currentLoop = calibrationTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
        for paramName in condition:
            globals()[paramName] = condition[paramName]
        
        # --- Prepare to start Routine "calibration_decision" ---
        # create an object to store info about Routine calibration_decision
        calibration_decision = data.Routine(
            name='calibration_decision',
            components=[calibration_pre_fix, calibration_gabor, calibration_wait_fix, calibration_resp],
        )
        calibration_decision.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from calibration_setup
        if random() < 0.5:
            calibTiltSign = -1
            calibCorrAns = 'f'
        else:
            calibTiltSign = 1
            calibCorrAns = 'j'
        
        calibration_gabor.setOri(calibTiltSign * level)
        # create starting attributes for calibration_resp
        calibration_resp.keys = []
        calibration_resp.rt = []
        _calibration_resp_allKeys = []
        # Run 'Begin Routine' code from calibration_minexposure
        decisionEnd = -1
        
        # store start times for calibration_decision
        calibration_decision.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        calibration_decision.tStart = globalClock.getTime(format='float')
        calibration_decision.status = STARTED
        thisExp.addData('calibration_decision.started', calibration_decision.tStart)
        calibration_decision.maxDuration = None
        # keep track of which components have finished
        calibration_decisionComponents = calibration_decision.components
        for thisComponent in calibration_decision.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "calibration_decision" ---
        thisExp.currentRoutine = calibration_decision
        calibration_decision.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(condition, 'status') and condition.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *calibration_pre_fix* updates
            
            # if calibration_pre_fix is starting this frame...
            if calibration_pre_fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                calibration_pre_fix.frameNStart = frameN  # exact frame index
                calibration_pre_fix.tStart = t  # local t and not account for scr refresh
                calibration_pre_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(calibration_pre_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'calibration_pre_fix.started')
                # update status
                calibration_pre_fix.status = STARTED
                calibration_pre_fix.setAutoDraw(True)
            
            # if calibration_pre_fix is active this frame...
            if calibration_pre_fix.status == STARTED:
                # update params
                pass
            
            # if calibration_pre_fix is stopping this frame...
            if calibration_pre_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > calibration_pre_fix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    calibration_pre_fix.tStop = t  # not accounting for scr refresh
                    calibration_pre_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    calibration_pre_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'calibration_pre_fix.stopped')
                    # update status
                    calibration_pre_fix.status = FINISHED
                    calibration_pre_fix.setAutoDraw(False)
            
            # *calibration_gabor* updates
            
            # if calibration_gabor is starting this frame...
            if calibration_gabor.status == NOT_STARTED and calibration_pre_fix.status == FINISHED:
                # keep track of start time/frame for later
                calibration_gabor.frameNStart = frameN  # exact frame index
                calibration_gabor.tStart = t  # local t and not account for scr refresh
                calibration_gabor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(calibration_gabor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'calibration_gabor.started')
                # update status
                calibration_gabor.status = STARTED
                calibration_gabor.setAutoDraw(True)
            
            # if calibration_gabor is active this frame...
            if calibration_gabor.status == STARTED:
                # update params
                pass
            
            # if calibration_gabor is stopping this frame...
            if calibration_gabor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > calibration_gabor.tStartRefresh + 0.15-frameTolerance:
                    # keep track of stop time/frame for later
                    calibration_gabor.tStop = t  # not accounting for scr refresh
                    calibration_gabor.tStopRefresh = tThisFlipGlobal  # on global time
                    calibration_gabor.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'calibration_gabor.stopped')
                    # update status
                    calibration_gabor.status = FINISHED
                    calibration_gabor.setAutoDraw(False)
            
            # *calibration_wait_fix* updates
            
            # if calibration_wait_fix is starting this frame...
            if calibration_wait_fix.status == NOT_STARTED and calibration_gabor.status == FINISHED:
                # keep track of start time/frame for later
                calibration_wait_fix.frameNStart = frameN  # exact frame index
                calibration_wait_fix.tStart = t  # local t and not account for scr refresh
                calibration_wait_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(calibration_wait_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'calibration_wait_fix.started')
                # update status
                calibration_wait_fix.status = STARTED
                calibration_wait_fix.setAutoDraw(True)
            
            # if calibration_wait_fix is active this frame...
            if calibration_wait_fix.status == STARTED:
                # update params
                pass
            
            # if calibration_wait_fix is stopping this frame...
            if calibration_wait_fix.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    calibration_wait_fix.tStop = t  # not accounting for scr refresh
                    calibration_wait_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    calibration_wait_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'calibration_wait_fix.stopped')
                    # update status
                    calibration_wait_fix.status = FINISHED
                    calibration_wait_fix.setAutoDraw(False)
            
            # *calibration_resp* updates
            waitOnFlip = False
            
            # if calibration_resp is starting this frame...
            if calibration_resp.status == NOT_STARTED and calibration_pre_fix.status == FINISHED:
                # keep track of start time/frame for later
                calibration_resp.frameNStart = frameN  # exact frame index
                calibration_resp.tStart = t  # local t and not account for scr refresh
                calibration_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(calibration_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'calibration_resp.started')
                # update status
                calibration_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(calibration_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(calibration_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if calibration_resp is stopping this frame...
            if calibration_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > calibration_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    calibration_resp.tStop = t  # not accounting for scr refresh
                    calibration_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    calibration_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'calibration_resp.stopped')
                    # update status
                    calibration_resp.status = FINISHED
                    calibration_resp.status = FINISHED
            if calibration_resp.status == STARTED and not waitOnFlip:
                theseKeys = calibration_resp.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _calibration_resp_allKeys.extend(theseKeys)
                if len(_calibration_resp_allKeys):
                    calibration_resp.keys = _calibration_resp_allKeys[0].name  # just the first key pressed
                    calibration_resp.rt = _calibration_resp_allKeys[0].rt
                    calibration_resp.duration = _calibration_resp_allKeys[0].duration
                    # was this correct?
                    if (calibration_resp.keys == str(calibCorrAns)) or (calibration_resp.keys == calibCorrAns):
                        calibration_resp.corr = 1
                    else:
                        calibration_resp.corr = 0
            # Run 'Each Frame' code from calibration_minexposure
            if decisionEnd < 0:
                if calibration_resp.keys and t >= 1.0 + 0.15:
                    decisionEnd = t
                elif t >= 1.0 + 1.5:
                    decisionEnd = t
            if decisionEnd >= 0:
                if True:
                    continueRoutine = False
                elif t >= decisionEnd + 1.5:
                    continueRoutine = False
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=calibration_decision,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                calibration_decision.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if calibration_decision.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in calibration_decision.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "calibration_decision" ---
        for thisComponent in calibration_decision.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for calibration_decision
        calibration_decision.tStop = globalClock.getTime(format='float')
        calibration_decision.tStopRefresh = tThisFlipGlobal
        thisExp.addData('calibration_decision.stopped', calibration_decision.tStop)
        # check responses
        if calibration_resp.keys in ['', [], None]:  # No response was made
            calibration_resp.keys = None
            # was no response the correct answer?!
            if str(calibCorrAns).lower() == 'none':
               calibration_resp.corr = 1;  # correct non-response
            else:
               calibration_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for calibrationTrials (MultiStairHandler)
        calibrationTrials.addResponse(calibration_resp.corr, level)
        calibrationTrials.addOtherData('calibration_resp.rt', calibration_resp.rt)
        # Run 'End Routine' code from calibration_end
        questLevels.append(float(level))
        thisExp.addData('phase', 'calibration')
        thisExp.addData('tiltSignUsed', calibTiltSign)
        thisExp.addData('corrAns', calibCorrAns)
        
        # the Routine "calibration_decision" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # all staircases completed
    
    
    # --- Prepare to start Routine "calibration_summary" ---
    # create an object to store info about Routine calibration_summary
    calibration_summary = data.Routine(
        name='calibration_summary',
        components=[calibration_done_text],
    )
    calibration_summary.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from calibration_summary_code
    lastLevels = questLevels[-10:]
    tiltDeg = median_value(lastLevels)
    tiltDeg = min(max(tiltDeg, 1.0), 15.0)
    thisExp.addData('calibratedTiltDeg', tiltDeg)
    thisExp.addData('calibrationAtBoundary', int(tiltDeg <= 1.0 or tiltDeg >= 15.0))
    
    # store start times for calibration_summary
    calibration_summary.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    calibration_summary.tStart = globalClock.getTime(format='float')
    calibration_summary.status = STARTED
    thisExp.addData('calibration_summary.started', calibration_summary.tStart)
    calibration_summary.maxDuration = 0.5
    # keep track of which components have finished
    calibration_summaryComponents = calibration_summary.components
    for thisComponent in calibration_summary.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "calibration_summary" ---
    thisExp.currentRoutine = calibration_summary
    calibration_summary.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > calibration_summary.maxDuration-frameTolerance:
            calibration_summary.maxDurationReached = True
            continueRoutine = False
        
        # *calibration_done_text* updates
        
        # if calibration_done_text is starting this frame...
        if calibration_done_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            calibration_done_text.frameNStart = frameN  # exact frame index
            calibration_done_text.tStart = t  # local t and not account for scr refresh
            calibration_done_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calibration_done_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calibration_done_text.started')
            # update status
            calibration_done_text.status = STARTED
            calibration_done_text.setAutoDraw(True)
        
        # if calibration_done_text is active this frame...
        if calibration_done_text.status == STARTED:
            # update params
            pass
        
        # if calibration_done_text is stopping this frame...
        if calibration_done_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > calibration_done_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                calibration_done_text.tStop = t  # not accounting for scr refresh
                calibration_done_text.tStopRefresh = tThisFlipGlobal  # on global time
                calibration_done_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'calibration_done_text.stopped')
                # update status
                calibration_done_text.status = FINISHED
                calibration_done_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=calibration_summary,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            calibration_summary.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if calibration_summary.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in calibration_summary.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calibration_summary" ---
    for thisComponent in calibration_summary.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for calibration_summary
    calibration_summary.tStop = globalClock.getTime(format='float')
    calibration_summary.tStopRefresh = tThisFlipGlobal
    thisExp.addData('calibration_summary.stopped', calibration_summary.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if calibration_summary.maxDurationReached:
        routineTimer.addTime(-calibration_summary.maxDuration)
    elif calibration_summary.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "baseline_intro" ---
    # create an object to store info about Routine baseline_intro
    baseline_intro = data.Routine(
        name='baseline_intro',
        components=[baseline_intro_text, baseline_intro_key],
    )
    baseline_intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for baseline_intro_key
    baseline_intro_key.keys = []
    baseline_intro_key.rt = []
    _baseline_intro_key_allKeys = []
    # store start times for baseline_intro
    baseline_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    baseline_intro.tStart = globalClock.getTime(format='float')
    baseline_intro.status = STARTED
    thisExp.addData('baseline_intro.started', baseline_intro.tStart)
    baseline_intro.maxDuration = None
    # keep track of which components have finished
    baseline_introComponents = baseline_intro.components
    for thisComponent in baseline_intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "baseline_intro" ---
    thisExp.currentRoutine = baseline_intro
    baseline_intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_intro_text* updates
        
        # if baseline_intro_text is starting this frame...
        if baseline_intro_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            baseline_intro_text.frameNStart = frameN  # exact frame index
            baseline_intro_text.tStart = t  # local t and not account for scr refresh
            baseline_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline_intro_text.started')
            # update status
            baseline_intro_text.status = STARTED
            baseline_intro_text.setAutoDraw(True)
        
        # if baseline_intro_text is active this frame...
        if baseline_intro_text.status == STARTED:
            # update params
            pass
        
        # *baseline_intro_key* updates
        waitOnFlip = False
        
        # if baseline_intro_key is starting this frame...
        if baseline_intro_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            baseline_intro_key.frameNStart = frameN  # exact frame index
            baseline_intro_key.tStart = t  # local t and not account for scr refresh
            baseline_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_intro_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline_intro_key.started')
            # update status
            baseline_intro_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(baseline_intro_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(baseline_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if baseline_intro_key.status == STARTED and not waitOnFlip:
            theseKeys = baseline_intro_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _baseline_intro_key_allKeys.extend(theseKeys)
            if len(_baseline_intro_key_allKeys):
                baseline_intro_key.keys = _baseline_intro_key_allKeys[0].name  # just the first key pressed
                baseline_intro_key.rt = _baseline_intro_key_allKeys[0].rt
                baseline_intro_key.duration = _baseline_intro_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=baseline_intro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            baseline_intro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if baseline_intro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in baseline_intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "baseline_intro" ---
    for thisComponent in baseline_intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for baseline_intro
    baseline_intro.tStop = globalClock.getTime(format='float')
    baseline_intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('baseline_intro.stopped', baseline_intro.tStop)
    # check responses
    if baseline_intro_key.keys in ['', [], None]:  # No response was made
        baseline_intro_key.keys = None
    thisExp.addData('baseline_intro_key.keys',baseline_intro_key.keys)
    if baseline_intro_key.keys != None:  # we had a response
        thisExp.addData('baseline_intro_key.rt', baseline_intro_key.rt)
        thisExp.addData('baseline_intro_key.duration', baseline_intro_key.duration)
    thisExp.nextEntry()
    # the Routine "baseline_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    baselineTrials = data.TrialHandler2(
        name='baselineTrials',
        nReps=20, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions/two_orientations.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(baselineTrials)  # add the loop to the experiment
    thisBaselineTrial = baselineTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBaselineTrial.rgb)
    if thisBaselineTrial != None:
        for paramName in thisBaselineTrial:
            globals()[paramName] = thisBaselineTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBaselineTrial in baselineTrials:
        baselineTrials.status = STARTED
        if hasattr(thisBaselineTrial, 'status'):
            thisBaselineTrial.status = STARTED
        currentLoop = baselineTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBaselineTrial.rgb)
        if thisBaselineTrial != None:
            for paramName in thisBaselineTrial:
                globals()[paramName] = thisBaselineTrial[paramName]
        
        # --- Prepare to start Routine "baseline_decision" ---
        # create an object to store info about Routine baseline_decision
        baseline_decision = data.Routine(
            name='baseline_decision',
            components=[baseline_pre_fix, baseline_gabor, baseline_wait_fix, baseline_resp],
        )
        baseline_decision.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        baseline_gabor.setOri(tiltSign * tiltDeg)
        # create starting attributes for baseline_resp
        baseline_resp.keys = []
        baseline_resp.rt = []
        _baseline_resp_allKeys = []
        # Run 'Begin Routine' code from baseline_minexposure
        decisionEnd = -1
        
        # store start times for baseline_decision
        baseline_decision.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        baseline_decision.tStart = globalClock.getTime(format='float')
        baseline_decision.status = STARTED
        thisExp.addData('baseline_decision.started', baseline_decision.tStart)
        baseline_decision.maxDuration = None
        # keep track of which components have finished
        baseline_decisionComponents = baseline_decision.components
        for thisComponent in baseline_decision.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "baseline_decision" ---
        thisExp.currentRoutine = baseline_decision
        baseline_decision.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBaselineTrial, 'status') and thisBaselineTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *baseline_pre_fix* updates
            
            # if baseline_pre_fix is starting this frame...
            if baseline_pre_fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                baseline_pre_fix.frameNStart = frameN  # exact frame index
                baseline_pre_fix.tStart = t  # local t and not account for scr refresh
                baseline_pre_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(baseline_pre_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_pre_fix.started')
                # update status
                baseline_pre_fix.status = STARTED
                baseline_pre_fix.setAutoDraw(True)
            
            # if baseline_pre_fix is active this frame...
            if baseline_pre_fix.status == STARTED:
                # update params
                pass
            
            # if baseline_pre_fix is stopping this frame...
            if baseline_pre_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > baseline_pre_fix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    baseline_pre_fix.tStop = t  # not accounting for scr refresh
                    baseline_pre_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    baseline_pre_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'baseline_pre_fix.stopped')
                    # update status
                    baseline_pre_fix.status = FINISHED
                    baseline_pre_fix.setAutoDraw(False)
            
            # *baseline_gabor* updates
            
            # if baseline_gabor is starting this frame...
            if baseline_gabor.status == NOT_STARTED and baseline_pre_fix.status == FINISHED:
                # keep track of start time/frame for later
                baseline_gabor.frameNStart = frameN  # exact frame index
                baseline_gabor.tStart = t  # local t and not account for scr refresh
                baseline_gabor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(baseline_gabor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_gabor.started')
                # update status
                baseline_gabor.status = STARTED
                baseline_gabor.setAutoDraw(True)
            
            # if baseline_gabor is active this frame...
            if baseline_gabor.status == STARTED:
                # update params
                pass
            
            # if baseline_gabor is stopping this frame...
            if baseline_gabor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > baseline_gabor.tStartRefresh + 0.15-frameTolerance:
                    # keep track of stop time/frame for later
                    baseline_gabor.tStop = t  # not accounting for scr refresh
                    baseline_gabor.tStopRefresh = tThisFlipGlobal  # on global time
                    baseline_gabor.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'baseline_gabor.stopped')
                    # update status
                    baseline_gabor.status = FINISHED
                    baseline_gabor.setAutoDraw(False)
            
            # *baseline_wait_fix* updates
            
            # if baseline_wait_fix is starting this frame...
            if baseline_wait_fix.status == NOT_STARTED and baseline_gabor.status == FINISHED:
                # keep track of start time/frame for later
                baseline_wait_fix.frameNStart = frameN  # exact frame index
                baseline_wait_fix.tStart = t  # local t and not account for scr refresh
                baseline_wait_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(baseline_wait_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_wait_fix.started')
                # update status
                baseline_wait_fix.status = STARTED
                baseline_wait_fix.setAutoDraw(True)
            
            # if baseline_wait_fix is active this frame...
            if baseline_wait_fix.status == STARTED:
                # update params
                pass
            
            # *baseline_resp* updates
            waitOnFlip = False
            
            # if baseline_resp is starting this frame...
            if baseline_resp.status == NOT_STARTED and baseline_pre_fix.status == FINISHED:
                # keep track of start time/frame for later
                baseline_resp.frameNStart = frameN  # exact frame index
                baseline_resp.tStart = t  # local t and not account for scr refresh
                baseline_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(baseline_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_resp.started')
                # update status
                baseline_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(baseline_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(baseline_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if baseline_resp is stopping this frame...
            if baseline_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > baseline_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    baseline_resp.tStop = t  # not accounting for scr refresh
                    baseline_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    baseline_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'baseline_resp.stopped')
                    # update status
                    baseline_resp.status = FINISHED
                    baseline_resp.status = FINISHED
            if baseline_resp.status == STARTED and not waitOnFlip:
                theseKeys = baseline_resp.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _baseline_resp_allKeys.extend(theseKeys)
                if len(_baseline_resp_allKeys):
                    baseline_resp.keys = _baseline_resp_allKeys[0].name  # just the first key pressed
                    baseline_resp.rt = _baseline_resp_allKeys[0].rt
                    baseline_resp.duration = _baseline_resp_allKeys[0].duration
                    # was this correct?
                    if (baseline_resp.keys == str(corrAns)) or (baseline_resp.keys == corrAns):
                        baseline_resp.corr = 1
                    else:
                        baseline_resp.corr = 0
            # Run 'Each Frame' code from baseline_minexposure
            if decisionEnd < 0:
                if baseline_resp.keys and t >= 1.0 + 0.15:
                    decisionEnd = t
                elif t >= 1.0 + 1.5:
                    decisionEnd = t
            if decisionEnd >= 0:
                if False:
                    continueRoutine = False
                elif t >= decisionEnd + 1.5:
                    continueRoutine = False
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=baseline_decision,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                baseline_decision.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if baseline_decision.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in baseline_decision.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "baseline_decision" ---
        for thisComponent in baseline_decision.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for baseline_decision
        baseline_decision.tStop = globalClock.getTime(format='float')
        baseline_decision.tStopRefresh = tThisFlipGlobal
        thisExp.addData('baseline_decision.stopped', baseline_decision.tStop)
        # check responses
        if baseline_resp.keys in ['', [], None]:  # No response was made
            baseline_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               baseline_resp.corr = 1;  # correct non-response
            else:
               baseline_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for baselineTrials (TrialHandler)
        baselineTrials.addData('baseline_resp.keys',baseline_resp.keys)
        baselineTrials.addData('baseline_resp.corr', baseline_resp.corr)
        if baseline_resp.keys != None:  # we had a response
            baselineTrials.addData('baseline_resp.rt', baseline_resp.rt)
            baselineTrials.addData('baseline_resp.duration', baseline_resp.duration)
        # Run 'End Routine' code from baseline_end
        thisExp.addData('phase', 'baseline')
        
        thisExp.addData('tiltDegUsed', tiltDeg)
        thisExp.addData('probeScheduled', 0)
        
        # the Routine "baseline_decision" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisBaselineTrial as finished
        if hasattr(thisBaselineTrial, 'status'):
            thisBaselineTrial.status = FINISHED
        # if awaiting a pause, pause now
        if baselineTrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            baselineTrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 20 repeats of 'baselineTrials'
    baselineTrials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "main_intro" ---
    # create an object to store info about Routine main_intro
    main_intro = data.Routine(
        name='main_intro',
        components=[main_intro_text, main_intro_key],
    )
    main_intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for main_intro_key
    main_intro_key.keys = []
    main_intro_key.rt = []
    _main_intro_key_allKeys = []
    # store start times for main_intro
    main_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    main_intro.tStart = globalClock.getTime(format='float')
    main_intro.status = STARTED
    thisExp.addData('main_intro.started', main_intro.tStart)
    main_intro.maxDuration = None
    # keep track of which components have finished
    main_introComponents = main_intro.components
    for thisComponent in main_intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "main_intro" ---
    thisExp.currentRoutine = main_intro
    main_intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_intro_text* updates
        
        # if main_intro_text is starting this frame...
        if main_intro_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            main_intro_text.frameNStart = frameN  # exact frame index
            main_intro_text.tStart = t  # local t and not account for scr refresh
            main_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_intro_text.started')
            # update status
            main_intro_text.status = STARTED
            main_intro_text.setAutoDraw(True)
        
        # if main_intro_text is active this frame...
        if main_intro_text.status == STARTED:
            # update params
            pass
        
        # *main_intro_key* updates
        waitOnFlip = False
        
        # if main_intro_key is starting this frame...
        if main_intro_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            main_intro_key.frameNStart = frameN  # exact frame index
            main_intro_key.tStart = t  # local t and not account for scr refresh
            main_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_intro_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_intro_key.started')
            # update status
            main_intro_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(main_intro_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(main_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if main_intro_key.status == STARTED and not waitOnFlip:
            theseKeys = main_intro_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _main_intro_key_allKeys.extend(theseKeys)
            if len(_main_intro_key_allKeys):
                main_intro_key.keys = _main_intro_key_allKeys[0].name  # just the first key pressed
                main_intro_key.rt = _main_intro_key_allKeys[0].rt
                main_intro_key.duration = _main_intro_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=main_intro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            main_intro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if main_intro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in main_intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "main_intro" ---
    for thisComponent in main_intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for main_intro
    main_intro.tStop = globalClock.getTime(format='float')
    main_intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('main_intro.stopped', main_intro.tStop)
    # check responses
    if main_intro_key.keys in ['', [], None]:  # No response was made
        main_intro_key.keys = None
    thisExp.addData('main_intro_key.keys',main_intro_key.keys)
    if main_intro_key.keys != None:  # we had a response
        thisExp.addData('main_intro_key.rt', main_intro_key.rt)
        thisExp.addData('main_intro_key.duration', main_intro_key.duration)
    thisExp.nextEntry()
    # the Routine "main_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mainBlocks = data.TrialHandler2(
        name='mainBlocks',
        nReps=4, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=False, 
    )
    thisExp.addLoop(mainBlocks)  # add the loop to the experiment
    thisMainBlock = mainBlocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMainBlock.rgb)
    if thisMainBlock != None:
        for paramName in thisMainBlock:
            globals()[paramName] = thisMainBlock[paramName]
    
    for thisMainBlock in mainBlocks:
        mainBlocks.status = STARTED
        if hasattr(thisMainBlock, 'status'):
            thisMainBlock.status = STARTED
        currentLoop = mainBlocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisMainBlock.rgb)
        if thisMainBlock != None:
            for paramName in thisMainBlock:
                globals()[paramName] = thisMainBlock[paramName]
        
        # --- Prepare to start Routine "block_intro" ---
        # create an object to store info about Routine block_intro
        block_intro = data.Routine(
            name='block_intro',
            components=[block_intro_text, block_intro_key],
        )
        block_intro.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from block_intro_code
        blockText = 'Block ' + str(mainBlocks.thisN + 1) + ' of 4\n\nPress SPACE when you are ready.'
        
        block_intro_text.setText(blockText)
        # create starting attributes for block_intro_key
        block_intro_key.keys = []
        block_intro_key.rt = []
        _block_intro_key_allKeys = []
        # store start times for block_intro
        block_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_intro.tStart = globalClock.getTime(format='float')
        block_intro.status = STARTED
        thisExp.addData('block_intro.started', block_intro.tStart)
        block_intro.maxDuration = None
        # keep track of which components have finished
        block_introComponents = block_intro.components
        for thisComponent in block_intro.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block_intro" ---
        thisExp.currentRoutine = block_intro
        block_intro.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMainBlock, 'status') and thisMainBlock.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block_intro_text* updates
            
            # if block_intro_text is starting this frame...
            if block_intro_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                block_intro_text.frameNStart = frameN  # exact frame index
                block_intro_text.tStart = t  # local t and not account for scr refresh
                block_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_intro_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_intro_text.started')
                # update status
                block_intro_text.status = STARTED
                block_intro_text.setAutoDraw(True)
            
            # if block_intro_text is active this frame...
            if block_intro_text.status == STARTED:
                # update params
                pass
            
            # *block_intro_key* updates
            waitOnFlip = False
            
            # if block_intro_key is starting this frame...
            if block_intro_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                block_intro_key.frameNStart = frameN  # exact frame index
                block_intro_key.tStart = t  # local t and not account for scr refresh
                block_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_intro_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_intro_key.started')
                # update status
                block_intro_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(block_intro_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(block_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if block_intro_key.status == STARTED and not waitOnFlip:
                theseKeys = block_intro_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _block_intro_key_allKeys.extend(theseKeys)
                if len(_block_intro_key_allKeys):
                    block_intro_key.keys = _block_intro_key_allKeys[0].name  # just the first key pressed
                    block_intro_key.rt = _block_intro_key_allKeys[0].rt
                    block_intro_key.duration = _block_intro_key_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=block_intro,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                block_intro.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if block_intro.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in block_intro.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_intro" ---
        for thisComponent in block_intro.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_intro
        block_intro.tStop = globalClock.getTime(format='float')
        block_intro.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_intro.stopped', block_intro.tStop)
        # check responses
        if block_intro_key.keys in ['', [], None]:  # No response was made
            block_intro_key.keys = None
        mainBlocks.addData('block_intro_key.keys',block_intro_key.keys)
        if block_intro_key.keys != None:  # we had a response
            mainBlocks.addData('block_intro_key.rt', block_intro_key.rt)
            mainBlocks.addData('block_intro_key.duration', block_intro_key.duration)
        # the Routine "block_intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        mainTrials = data.TrialHandler2(
            name='mainTrials',
            nReps=20, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('conditions/two_orientations.csv'), 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(mainTrials)  # add the loop to the experiment
        thisMainTrial = mainTrials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
        if thisMainTrial != None:
            for paramName in thisMainTrial:
                globals()[paramName] = thisMainTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisMainTrial in mainTrials:
            mainTrials.status = STARTED
            if hasattr(thisMainTrial, 'status'):
                thisMainTrial.status = STARTED
            currentLoop = mainTrials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
            if thisMainTrial != None:
                for paramName in thisMainTrial:
                    globals()[paramName] = thisMainTrial[paramName]
            
            # --- Prepare to start Routine "main_decision" ---
            # create an object to store info about Routine main_decision
            main_decision = data.Routine(
                name='main_decision',
                components=[main_pre_fix, main_gabor, main_wait_fix, main_resp],
            )
            main_decision.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from main_setup
            trialIndex = globalTrialN
            
            if probeCondition == 'full_probe':
                probeThisTrial = 1
            elif probeCondition == 'sparse_probe':
                probeThisTrial = int(probeSchedule[trialIndex])
            else:
                probeThisTrial = 0
            
            main_gabor.setOri(tiltSign * tiltDeg)
            # create starting attributes for main_resp
            main_resp.keys = []
            main_resp.rt = []
            _main_resp_allKeys = []
            # Run 'Begin Routine' code from main_minexposure
            decisionEnd = -1
            
            # store start times for main_decision
            main_decision.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            main_decision.tStart = globalClock.getTime(format='float')
            main_decision.status = STARTED
            thisExp.addData('main_decision.started', main_decision.tStart)
            main_decision.maxDuration = None
            # keep track of which components have finished
            main_decisionComponents = main_decision.components
            for thisComponent in main_decision.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "main_decision" ---
            thisExp.currentRoutine = main_decision
            main_decision.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisMainTrial, 'status') and thisMainTrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *main_pre_fix* updates
                
                # if main_pre_fix is starting this frame...
                if main_pre_fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    main_pre_fix.frameNStart = frameN  # exact frame index
                    main_pre_fix.tStart = t  # local t and not account for scr refresh
                    main_pre_fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(main_pre_fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_pre_fix.started')
                    # update status
                    main_pre_fix.status = STARTED
                    main_pre_fix.setAutoDraw(True)
                
                # if main_pre_fix is active this frame...
                if main_pre_fix.status == STARTED:
                    # update params
                    pass
                
                # if main_pre_fix is stopping this frame...
                if main_pre_fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > main_pre_fix.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        main_pre_fix.tStop = t  # not accounting for scr refresh
                        main_pre_fix.tStopRefresh = tThisFlipGlobal  # on global time
                        main_pre_fix.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'main_pre_fix.stopped')
                        # update status
                        main_pre_fix.status = FINISHED
                        main_pre_fix.setAutoDraw(False)
                
                # *main_gabor* updates
                
                # if main_gabor is starting this frame...
                if main_gabor.status == NOT_STARTED and main_pre_fix.status == FINISHED:
                    # keep track of start time/frame for later
                    main_gabor.frameNStart = frameN  # exact frame index
                    main_gabor.tStart = t  # local t and not account for scr refresh
                    main_gabor.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(main_gabor, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_gabor.started')
                    # update status
                    main_gabor.status = STARTED
                    main_gabor.setAutoDraw(True)
                
                # if main_gabor is active this frame...
                if main_gabor.status == STARTED:
                    # update params
                    pass
                
                # if main_gabor is stopping this frame...
                if main_gabor.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > main_gabor.tStartRefresh + 0.15-frameTolerance:
                        # keep track of stop time/frame for later
                        main_gabor.tStop = t  # not accounting for scr refresh
                        main_gabor.tStopRefresh = tThisFlipGlobal  # on global time
                        main_gabor.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'main_gabor.stopped')
                        # update status
                        main_gabor.status = FINISHED
                        main_gabor.setAutoDraw(False)
                
                # *main_wait_fix* updates
                
                # if main_wait_fix is starting this frame...
                if main_wait_fix.status == NOT_STARTED and main_gabor.status == FINISHED:
                    # keep track of start time/frame for later
                    main_wait_fix.frameNStart = frameN  # exact frame index
                    main_wait_fix.tStart = t  # local t and not account for scr refresh
                    main_wait_fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(main_wait_fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_wait_fix.started')
                    # update status
                    main_wait_fix.status = STARTED
                    main_wait_fix.setAutoDraw(True)
                
                # if main_wait_fix is active this frame...
                if main_wait_fix.status == STARTED:
                    # update params
                    pass
                
                # *main_resp* updates
                waitOnFlip = False
                
                # if main_resp is starting this frame...
                if main_resp.status == NOT_STARTED and main_pre_fix.status == FINISHED:
                    # keep track of start time/frame for later
                    main_resp.frameNStart = frameN  # exact frame index
                    main_resp.tStart = t  # local t and not account for scr refresh
                    main_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(main_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_resp.started')
                    # update status
                    main_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(main_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(main_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if main_resp is stopping this frame...
                if main_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > main_resp.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        main_resp.tStop = t  # not accounting for scr refresh
                        main_resp.tStopRefresh = tThisFlipGlobal  # on global time
                        main_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'main_resp.stopped')
                        # update status
                        main_resp.status = FINISHED
                        main_resp.status = FINISHED
                if main_resp.status == STARTED and not waitOnFlip:
                    theseKeys = main_resp.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                    _main_resp_allKeys.extend(theseKeys)
                    if len(_main_resp_allKeys):
                        main_resp.keys = _main_resp_allKeys[0].name  # just the first key pressed
                        main_resp.rt = _main_resp_allKeys[0].rt
                        main_resp.duration = _main_resp_allKeys[0].duration
                        # was this correct?
                        if (main_resp.keys == str(corrAns)) or (main_resp.keys == corrAns):
                            main_resp.corr = 1
                        else:
                            main_resp.corr = 0
                # Run 'Each Frame' code from main_minexposure
                if decisionEnd < 0:
                    if main_resp.keys and t >= 1.0 + 0.15:
                        decisionEnd = t
                    elif t >= 1.0 + 1.5:
                        decisionEnd = t
                if decisionEnd >= 0:
                    if (probeThisTrial == 1 and bool(main_resp.keys)):
                        continueRoutine = False
                    elif t >= decisionEnd + 1.5:
                        continueRoutine = False
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=main_decision,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    main_decision.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if main_decision.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in main_decision.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "main_decision" ---
            for thisComponent in main_decision.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for main_decision
            main_decision.tStop = globalClock.getTime(format='float')
            main_decision.tStopRefresh = tThisFlipGlobal
            thisExp.addData('main_decision.stopped', main_decision.tStop)
            # check responses
            if main_resp.keys in ['', [], None]:  # No response was made
                main_resp.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   main_resp.corr = 1;  # correct non-response
                else:
                   main_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for mainTrials (TrialHandler)
            mainTrials.addData('main_resp.keys',main_resp.keys)
            mainTrials.addData('main_resp.corr', main_resp.corr)
            if main_resp.keys != None:  # we had a response
                mainTrials.addData('main_resp.rt', main_resp.rt)
                mainTrials.addData('main_resp.duration', main_resp.duration)
            # Run 'End Routine' code from main_end
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
            
            # the Routine "main_decision" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            confidenceProbeLoop = data.TrialHandler2(
                name='confidenceProbeLoop',
                nReps=probeThisTrial, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
                isTrials=False, 
            )
            thisExp.addLoop(confidenceProbeLoop)  # add the loop to the experiment
            thisConfidenceProbeLoop = confidenceProbeLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisConfidenceProbeLoop.rgb)
            if thisConfidenceProbeLoop != None:
                for paramName in thisConfidenceProbeLoop:
                    globals()[paramName] = thisConfidenceProbeLoop[paramName]
            
            for thisConfidenceProbeLoop in confidenceProbeLoop:
                confidenceProbeLoop.status = STARTED
                if hasattr(thisConfidenceProbeLoop, 'status'):
                    thisConfidenceProbeLoop.status = STARTED
                currentLoop = confidenceProbeLoop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # abbreviate parameter names if possible (e.g. rgb = thisConfidenceProbeLoop.rgb)
                if thisConfidenceProbeLoop != None:
                    for paramName in thisConfidenceProbeLoop:
                        globals()[paramName] = thisConfidenceProbeLoop[paramName]
                
                # --- Prepare to start Routine "main_post_probe" ---
                # create an object to store info about Routine main_post_probe
                main_post_probe = data.Routine(
                    name='main_post_probe',
                    components=[confidence_prompt, conf_n1, conf_n2, conf_n3, conf_n4, conf_n5, conf_n6, conf_lab_lo, conf_lab_hi, conf_hint, conf_marker, confidence_resp],
                )
                main_post_probe.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # create starting attributes for confidence_resp
                confidence_resp.keys = []
                confidence_resp.rt = []
                _confidence_resp_allKeys = []
                # Run 'Begin Routine' code from confidence_logic
                confRating = 0
                confMoved = 0
                confNKeysSeen = 0
                confFirstT = ''
                confSubmitT = ''
                markerX = 0
                markerOpacity = 0
                
                # store start times for main_post_probe
                main_post_probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                main_post_probe.tStart = globalClock.getTime(format='float')
                main_post_probe.status = STARTED
                thisExp.addData('main_post_probe.started', main_post_probe.tStart)
                main_post_probe.maxDuration = None
                # keep track of which components have finished
                main_post_probeComponents = main_post_probe.components
                for thisComponent in main_post_probe.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "main_post_probe" ---
                thisExp.currentRoutine = main_post_probe
                main_post_probe.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisConfidenceProbeLoop, 'status') and thisConfidenceProbeLoop.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *confidence_prompt* updates
                    
                    # if confidence_prompt is starting this frame...
                    if confidence_prompt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        confidence_prompt.frameNStart = frameN  # exact frame index
                        confidence_prompt.tStart = t  # local t and not account for scr refresh
                        confidence_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(confidence_prompt, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'confidence_prompt.started')
                        # update status
                        confidence_prompt.status = STARTED
                        confidence_prompt.setAutoDraw(True)
                    
                    # if confidence_prompt is active this frame...
                    if confidence_prompt.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_n1* updates
                    
                    # if conf_n1 is starting this frame...
                    if conf_n1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_n1.frameNStart = frameN  # exact frame index
                        conf_n1.tStart = t  # local t and not account for scr refresh
                        conf_n1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_n1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_n1.started')
                        # update status
                        conf_n1.status = STARTED
                        conf_n1.setAutoDraw(True)
                    
                    # if conf_n1 is active this frame...
                    if conf_n1.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_n2* updates
                    
                    # if conf_n2 is starting this frame...
                    if conf_n2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_n2.frameNStart = frameN  # exact frame index
                        conf_n2.tStart = t  # local t and not account for scr refresh
                        conf_n2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_n2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_n2.started')
                        # update status
                        conf_n2.status = STARTED
                        conf_n2.setAutoDraw(True)
                    
                    # if conf_n2 is active this frame...
                    if conf_n2.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_n3* updates
                    
                    # if conf_n3 is starting this frame...
                    if conf_n3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_n3.frameNStart = frameN  # exact frame index
                        conf_n3.tStart = t  # local t and not account for scr refresh
                        conf_n3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_n3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_n3.started')
                        # update status
                        conf_n3.status = STARTED
                        conf_n3.setAutoDraw(True)
                    
                    # if conf_n3 is active this frame...
                    if conf_n3.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_n4* updates
                    
                    # if conf_n4 is starting this frame...
                    if conf_n4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_n4.frameNStart = frameN  # exact frame index
                        conf_n4.tStart = t  # local t and not account for scr refresh
                        conf_n4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_n4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_n4.started')
                        # update status
                        conf_n4.status = STARTED
                        conf_n4.setAutoDraw(True)
                    
                    # if conf_n4 is active this frame...
                    if conf_n4.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_n5* updates
                    
                    # if conf_n5 is starting this frame...
                    if conf_n5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_n5.frameNStart = frameN  # exact frame index
                        conf_n5.tStart = t  # local t and not account for scr refresh
                        conf_n5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_n5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_n5.started')
                        # update status
                        conf_n5.status = STARTED
                        conf_n5.setAutoDraw(True)
                    
                    # if conf_n5 is active this frame...
                    if conf_n5.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_n6* updates
                    
                    # if conf_n6 is starting this frame...
                    if conf_n6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_n6.frameNStart = frameN  # exact frame index
                        conf_n6.tStart = t  # local t and not account for scr refresh
                        conf_n6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_n6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_n6.started')
                        # update status
                        conf_n6.status = STARTED
                        conf_n6.setAutoDraw(True)
                    
                    # if conf_n6 is active this frame...
                    if conf_n6.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_lab_lo* updates
                    
                    # if conf_lab_lo is starting this frame...
                    if conf_lab_lo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_lab_lo.frameNStart = frameN  # exact frame index
                        conf_lab_lo.tStart = t  # local t and not account for scr refresh
                        conf_lab_lo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_lab_lo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_lab_lo.started')
                        # update status
                        conf_lab_lo.status = STARTED
                        conf_lab_lo.setAutoDraw(True)
                    
                    # if conf_lab_lo is active this frame...
                    if conf_lab_lo.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_lab_hi* updates
                    
                    # if conf_lab_hi is starting this frame...
                    if conf_lab_hi.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_lab_hi.frameNStart = frameN  # exact frame index
                        conf_lab_hi.tStart = t  # local t and not account for scr refresh
                        conf_lab_hi.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_lab_hi, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_lab_hi.started')
                        # update status
                        conf_lab_hi.status = STARTED
                        conf_lab_hi.setAutoDraw(True)
                    
                    # if conf_lab_hi is active this frame...
                    if conf_lab_hi.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_hint* updates
                    
                    # if conf_hint is starting this frame...
                    if conf_hint.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_hint.frameNStart = frameN  # exact frame index
                        conf_hint.tStart = t  # local t and not account for scr refresh
                        conf_hint.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_hint, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_hint.started')
                        # update status
                        conf_hint.status = STARTED
                        conf_hint.setAutoDraw(True)
                    
                    # if conf_hint is active this frame...
                    if conf_hint.status == STARTED:
                        # update params
                        pass
                    
                    # *conf_marker* updates
                    
                    # if conf_marker is starting this frame...
                    if conf_marker.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        conf_marker.frameNStart = frameN  # exact frame index
                        conf_marker.tStart = t  # local t and not account for scr refresh
                        conf_marker.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(conf_marker, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_marker.started')
                        # update status
                        conf_marker.status = STARTED
                        conf_marker.setAutoDraw(True)
                    
                    # if conf_marker is active this frame...
                    if conf_marker.status == STARTED:
                        # update params
                        conf_marker.setOpacity(markerOpacity, log=False)
                        conf_marker.setPos((markerX, 0.09), log=False)
                    
                    # *confidence_resp* updates
                    waitOnFlip = False
                    
                    # if confidence_resp is starting this frame...
                    if confidence_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        confidence_resp.frameNStart = frameN  # exact frame index
                        confidence_resp.tStart = t  # local t and not account for scr refresh
                        confidence_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(confidence_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'confidence_resp.started')
                        # update status
                        confidence_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(confidence_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(confidence_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if confidence_resp.status == STARTED and not waitOnFlip:
                        theseKeys = confidence_resp.getKeys(keyList=['f', 'j', 'space'], ignoreKeys=["escape"], waitRelease=False)
                        _confidence_resp_allKeys.extend(theseKeys)
                        if len(_confidence_resp_allKeys):
                            confidence_resp.keys = [key.name for key in _confidence_resp_allKeys]  # storing all keys
                            confidence_resp.rt = [key.rt for key in _confidence_resp_allKeys]
                            confidence_resp.duration = [key.duration for key in _confidence_resp_allKeys]
                    # Run 'Each Frame' code from confidence_logic
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
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=main_post_probe,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # has a Component requested the Routine to end?
                    if not continueRoutine:
                        main_post_probe.forceEnded = routineForceEnded = True
                    # has the Routine been forcibly ended?
                    if main_post_probe.forceEnded or routineForceEnded:
                        break
                    # has every Component finished?
                    continueRoutine = False
                    for thisComponent in main_post_probe.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "main_post_probe" ---
                for thisComponent in main_post_probe.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for main_post_probe
                main_post_probe.tStop = globalClock.getTime(format='float')
                main_post_probe.tStopRefresh = tThisFlipGlobal
                thisExp.addData('main_post_probe.stopped', main_post_probe.tStop)
                # check responses
                if confidence_resp.keys in ['', [], None]:  # No response was made
                    confidence_resp.keys = None
                confidenceProbeLoop.addData('confidence_resp.keys',confidence_resp.keys)
                if confidence_resp.keys != None:  # we had a response
                    confidenceProbeLoop.addData('confidence_resp.rt', confidence_resp.rt)
                    confidenceProbeLoop.addData('confidence_resp.duration', confidence_resp.duration)
                # Run 'End Routine' code from confidence_logic
                thisExp.addData('confidenceRating', confRating if confMoved == 1 else '')
                thisExp.addData('confidenceRT', confSubmitT)
                thisExp.addData('confidenceFirstMoveT', confFirstT)
                thisExp.addData('confidenceMade', confMoved)
                
                # the Routine "main_post_probe" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                # mark thisConfidenceProbeLoop as finished
                if hasattr(thisConfidenceProbeLoop, 'status'):
                    thisConfidenceProbeLoop.status = FINISHED
                # if awaiting a pause, pause now
                if confidenceProbeLoop.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    confidenceProbeLoop.status = STARTED
            # completed probeThisTrial repeats of 'confidenceProbeLoop'
            confidenceProbeLoop.status = FINISHED
            
            # mark thisMainTrial as finished
            if hasattr(thisMainTrial, 'status'):
                thisMainTrial.status = FINISHED
            # if awaiting a pause, pause now
            if mainTrials.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                mainTrials.status = STARTED
            thisExp.nextEntry()
            
        # completed 20 repeats of 'mainTrials'
        mainTrials.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "block_break" ---
        # create an object to store info about Routine block_break
        block_break = data.Routine(
            name='block_break',
            components=[block_break_text, block_break_key],
        )
        block_break.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from block_break_code
        blockNumber = mainBlocks.thisN + 1
        if blockNumber < 4:
            breakText = ('End of block ' + str(blockNumber) + ' of 4.\n\n'
                         'Take a short break. Press SPACE to continue.')
        else:
            breakText = 'The main task is complete. Press SPACE to continue.'
        
        block_break_text.setText(breakText)
        # create starting attributes for block_break_key
        block_break_key.keys = []
        block_break_key.rt = []
        _block_break_key_allKeys = []
        # store start times for block_break
        block_break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_break.tStart = globalClock.getTime(format='float')
        block_break.status = STARTED
        thisExp.addData('block_break.started', block_break.tStart)
        block_break.maxDuration = None
        # keep track of which components have finished
        block_breakComponents = block_break.components
        for thisComponent in block_break.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block_break" ---
        thisExp.currentRoutine = block_break
        block_break.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMainBlock, 'status') and thisMainBlock.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block_break_text* updates
            
            # if block_break_text is starting this frame...
            if block_break_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                block_break_text.frameNStart = frameN  # exact frame index
                block_break_text.tStart = t  # local t and not account for scr refresh
                block_break_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_break_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_break_text.started')
                # update status
                block_break_text.status = STARTED
                block_break_text.setAutoDraw(True)
            
            # if block_break_text is active this frame...
            if block_break_text.status == STARTED:
                # update params
                pass
            
            # *block_break_key* updates
            waitOnFlip = False
            
            # if block_break_key is starting this frame...
            if block_break_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                block_break_key.frameNStart = frameN  # exact frame index
                block_break_key.tStart = t  # local t and not account for scr refresh
                block_break_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_break_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_break_key.started')
                # update status
                block_break_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(block_break_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(block_break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if block_break_key.status == STARTED and not waitOnFlip:
                theseKeys = block_break_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _block_break_key_allKeys.extend(theseKeys)
                if len(_block_break_key_allKeys):
                    block_break_key.keys = _block_break_key_allKeys[0].name  # just the first key pressed
                    block_break_key.rt = _block_break_key_allKeys[0].rt
                    block_break_key.duration = _block_break_key_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=block_break,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                block_break.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if block_break.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in block_break.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_break" ---
        for thisComponent in block_break.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_break
        block_break.tStop = globalClock.getTime(format='float')
        block_break.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_break.stopped', block_break.tStop)
        # check responses
        if block_break_key.keys in ['', [], None]:  # No response was made
            block_break_key.keys = None
        mainBlocks.addData('block_break_key.keys',block_break_key.keys)
        if block_break_key.keys != None:  # we had a response
            mainBlocks.addData('block_break_key.rt', block_break_key.rt)
            mainBlocks.addData('block_break_key.duration', block_break_key.duration)
        # the Routine "block_break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisMainBlock as finished
        if hasattr(thisMainBlock, 'status'):
            thisMainBlock.status = FINISHED
        # if awaiting a pause, pause now
        if mainBlocks.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            mainBlocks.status = STARTED
    # completed 4 repeats of 'mainBlocks'
    mainBlocks.status = FINISHED
    
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[thanks_text],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = 3
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks" ---
    thisExp.currentRoutine = thanks
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > thanks.maxDuration-frameTolerance:
            thanks.maxDurationReached = True
            continueRoutine = False
        
        # *thanks_text* updates
        
        # if thanks_text is starting this frame...
        if thanks_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thanks_text.frameNStart = frameN  # exact frame index
            thanks_text.tStart = t  # local t and not account for scr refresh
            thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_text.started')
            # update status
            thanks_text.status = STARTED
            thanks_text.setAutoDraw(True)
        
        # if thanks_text is active this frame...
        if thanks_text.status == STARTED:
            # update params
            pass
        
        # if thanks_text is stopping this frame...
        if thanks_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thanks_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                thanks_text.tStop = t  # not accounting for scr refresh
                thanks_text.tStopRefresh = tThisFlipGlobal  # on global time
                thanks_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thanks_text.stopped')
                # update status
                thanks_text.status = FINISHED
                thanks_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            thanks.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if thanks.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thanks.maxDurationReached:
        routineTimer.addTime(-thanks.maxDuration)
    elif thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
