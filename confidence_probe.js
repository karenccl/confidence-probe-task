/************************* 
 * Confidence_Probe *
 *************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'confidence_probe';  // from the Builder filename that created this script
let expInfo = {
    'participant': 'test001',
    'condition': 'sparse_probe',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from init_code
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
var feedbackColor = "#ffdc00";
var blockText = "";
var breakText = "";
var FINISHED = PsychoJS.Status.FINISHED;  // used in the conditional start of *_wait_fix
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

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(initializeRoutineBegin());
flowScheduler.add(initializeRoutineEachFrame());
flowScheduler.add(initializeRoutineEnd());
const confidenceInstructionLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(confidenceInstructionLoopLoopBegin(confidenceInstructionLoopLoopScheduler));
flowScheduler.add(confidenceInstructionLoopLoopScheduler);
flowScheduler.add(confidenceInstructionLoopLoopEnd);


const neutralInstructionLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(neutralInstructionLoopLoopBegin(neutralInstructionLoopLoopScheduler));
flowScheduler.add(neutralInstructionLoopLoopScheduler);
flowScheduler.add(neutralInstructionLoopLoopEnd);


flowScheduler.add(practice_introRoutineBegin());
flowScheduler.add(practice_introRoutineEachFrame());
flowScheduler.add(practice_introRoutineEnd());
const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceTrialsLoopBegin(practiceTrialsLoopScheduler));
flowScheduler.add(practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopEnd);





flowScheduler.add(calibration_introRoutineBegin());
flowScheduler.add(calibration_introRoutineEachFrame());
flowScheduler.add(calibration_introRoutineEnd());
const calibrationTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(calibrationTrialsLoopBegin(calibrationTrialsLoopScheduler));
flowScheduler.add(calibrationTrialsLoopScheduler);
flowScheduler.add(calibrationTrialsLoopEnd);




flowScheduler.add(calibration_summaryRoutineBegin());
flowScheduler.add(calibration_summaryRoutineEachFrame());
flowScheduler.add(calibration_summaryRoutineEnd());
flowScheduler.add(baseline_introRoutineBegin());
flowScheduler.add(baseline_introRoutineEachFrame());
flowScheduler.add(baseline_introRoutineEnd());
const baselineTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(baselineTrialsLoopBegin(baselineTrialsLoopScheduler));
flowScheduler.add(baselineTrialsLoopScheduler);
flowScheduler.add(baselineTrialsLoopEnd);





flowScheduler.add(main_introRoutineBegin());
flowScheduler.add(main_introRoutineEachFrame());
flowScheduler.add(main_introRoutineEnd());
const mainBlocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mainBlocksLoopBegin(mainBlocksLoopScheduler));
flowScheduler.add(mainBlocksLoopScheduler);
flowScheduler.add(mainBlocksLoopEnd);









flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you. You may close this window.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you. You may close this window.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'conditions/two_orientations.csv', 'path': 'conditions/two_orientations.csv'},
    {'name': 'conditions/quest_conditions.csv', 'path': 'conditions/quest_conditions.csv'},
    {'name': 'conditions/two_orientations.csv', 'path': 'conditions/two_orientations.csv'},
    {'name': 'conditions/two_orientations.csv', 'path': 'conditions/two_orientations.csv'},
    {'name': 'https://lib.pavlovia.org/vendors/jsQUEST.min.js', 'path': 'https://lib.pavlovia.org/vendors/jsQUEST.min.js'},
    {'name': 'conditions/two_orientations.csv', 'path': 'conditions/two_orientations.csv'},
    {'name': 'conditions/quest_conditions.csv', 'path': 'conditions/quest_conditions.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + ((((("data/" + expInfo["participant"]) + "_") + expName) + "_") + expInfo["date"]));
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var welcome_text;
var welcome_key;
var consentClock;
var consent_text;
var consent_key;
var instructionsClock;
var instructions_text;
var instructions_key;
var initializeClock;
var init_fix;
var probeCondition;
var probeSchedule;
var showConfInstr;
var showNeutralInstr;
var confidence_instructionsClock;
var confidence_instructions_text;
var confidence_instructions_key;
var neutral_instructionsClock;
var neutral_instructions_text;
var neutral_instructions_key;
var practice_introClock;
var practice_intro_text;
var practice_intro_key;
var practice_fixationClock;
var practice_fixation_fix;
var practice_decisionClock;
var practice_gabor;
var practice_wait_fix;
var practice_resp;
var practice_feedbackClock;
var practice_feedback_text;
var practice_itiClock;
var practice_iti_fix;
var calibration_introClock;
var calibration_intro_text;
var calibration_intro_key;
var calibration_fixationClock;
var calibration_fixation_fix;
var calibration_decisionClock;
var calibration_gabor;
var calibration_wait_fix;
var calibration_resp;
var calibration_itiClock;
var calibration_iti_fix;
var calibration_summaryClock;
var calibration_done_text;
var baseline_introClock;
var baseline_intro_text;
var baseline_intro_key;
var baseline_fixationClock;
var baseline_fixation_fix;
var baseline_decisionClock;
var baseline_gabor;
var baseline_wait_fix;
var baseline_resp;
var baseline_postClock;
var baseline_post_fix;
var baseline_itiClock;
var baseline_iti_fix;
var main_introClock;
var main_intro_text;
var main_intro_key;
var block_introClock;
var block_intro_text;
var block_intro_key;
var main_fixationClock;
var main_fixation_fix;
var main_decisionClock;
var main_gabor;
var main_wait_fix;
var main_resp;
var main_postClock;
var post_fix;
var confidence_prompt;
var confidence_resp;
var main_itiClock;
var main_iti_fix;
var block_breakClock;
var block_break_text;
var block_break_key;
var thanksClock;
var thanks_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Welcome.\n\nPress SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  welcome_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  consent_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'consent_text',
    text: 'INFORMATION AND CONSENT\n\nThis study asks you to judge the tilt of brief striped patches using the keyboard. It lasts about 20-30 minutes. Participation is voluntary and you may stop at any time by pressing ESCAPE. No identifying information is collected.\n\n[Replace with the ethics-approved participant information and consent text.]\n\nPress SPACE to give consent and continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  consent_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'On each trial, you will see a striped patch tilted in one of two directions.\n\nPress F for a left-tilted patch.\nPress J for a right-tilted patch.\n\nRespond as accurately as possible. If you are unsure, make your best guess.\nKeep your index fingers on F and J throughout the task.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "initialize"
  initializeClock = new util.Clock();
  init_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'init_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from init_code
  probeCondition = String(expInfo['condition']).trim().toLowerCase();
  let validConditions = ['no_probe', 'sparse_probe', 'full_probe'];
  if (!validConditions.includes(probeCondition)) {
      throw new Error('condition must be no_probe, sparse_probe, or full_probe');
  }
  
  probeSchedule = [];
  for (let blockN = 0; blockN < 4; blockN++) {
      let oneBlock = Array(10).fill(1).concat(Array(30).fill(0));
      oneBlock = shuffledCopy(oneBlock);
      probeSchedule = probeSchedule.concat(oneBlock);
  }
  
  showConfInstr = (probeCondition !== 'no_probe') ? 1 : 0;
  showNeutralInstr = 1 - showConfInstr;
  psychoJS.experiment.addData('probeScheduleString', probeSchedule.join(''));
  
  // Initialize components for Routine "confidence_instructions"
  confidence_instructionsClock = new util.Clock();
  confidence_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidence_instructions_text',
    text: 'On some trials, you will also be asked how confident you are that your choice was correct.\n\nUse keys 1-6:\n1 means you were guessing.\n6 means you were very certain.\n\nUse the entire scale when appropriate. Confidence is about the choice you just made, not your general ability.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  confidence_instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "neutral_instructions"
  neutral_instructionsClock = new util.Clock();
  neutral_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'neutral_instructions_text',
    text: 'After each decision, a fixation cross may remain on the screen briefly. Keep looking at the cross until the next patch appears.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  neutral_instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_intro"
  practice_introClock = new util.Clock();
  practice_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_intro_text',
    text: 'Practice: the patch is clearly tilted and you will get feedback.\n\nPress SPACE to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  practice_intro_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_fixation"
  practice_fixationClock = new util.Clock();
  practice_fixation_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_fixation_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_decision"
  practice_decisionClock = new util.Clock();
  practice_gabor = new visual.GratingStim({
    win : psychoJS.window,
    name : 'practice_gabor', units : undefined, 
    tex : undefined, mask : 'gauss',
    ori : 1.0, 
    pos : [0, 0],
    draggable: false,
    anchor : 'center',
    sf : 4.0, phase : 0.0,
    size : [0.18, 0.18],
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 0.8, blendmode : 'avg',
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  practice_wait_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_wait_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  practice_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_feedback"
  practice_feedbackClock = new util.Clock();
  practice_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_feedback_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.06,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "practice_iti"
  practice_itiClock = new util.Clock();
  practice_iti_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_iti_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "calibration_intro"
  calibration_introClock = new util.Clock();
  calibration_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_intro_text',
    text: 'Calibration: the patch will get harder to see. No feedback now. Keep responding as accurately as you can.\n\nPress SPACE to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  calibration_intro_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "calibration_fixation"
  calibration_fixationClock = new util.Clock();
  calibration_fixation_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_fixation_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "calibration_decision"
  calibration_decisionClock = new util.Clock();
  calibration_gabor = new visual.GratingStim({
    win : psychoJS.window,
    name : 'calibration_gabor', units : undefined, 
    tex : undefined, mask : 'gauss',
    ori : 1.0, 
    pos : [0, 0],
    draggable: false,
    anchor : 'center',
    sf : 4.0, phase : 0.0,
    size : [0.18, 0.18],
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 0.8, blendmode : 'avg',
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  calibration_wait_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_wait_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  calibration_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "calibration_iti"
  calibration_itiClock = new util.Clock();
  calibration_iti_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_iti_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "calibration_summary"
  calibration_summaryClock = new util.Clock();
  calibration_done_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_done_text',
    text: 'Calibration complete',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "baseline_intro"
  baseline_introClock = new util.Clock();
  baseline_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_intro_text',
    text: 'Next part. No confidence reports in this part.\n\nPress SPACE to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  baseline_intro_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "baseline_fixation"
  baseline_fixationClock = new util.Clock();
  baseline_fixation_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_fixation_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "baseline_decision"
  baseline_decisionClock = new util.Clock();
  baseline_gabor = new visual.GratingStim({
    win : psychoJS.window,
    name : 'baseline_gabor', units : undefined, 
    tex : undefined, mask : 'gauss',
    ori : 1.0, 
    pos : [0, 0],
    draggable: false,
    anchor : 'center',
    sf : 4.0, phase : 0.0,
    size : [0.18, 0.18],
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 0.8, blendmode : 'avg',
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  baseline_wait_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_wait_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  baseline_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "baseline_post"
  baseline_postClock = new util.Clock();
  baseline_post_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_post_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "baseline_iti"
  baseline_itiClock = new util.Clock();
  baseline_iti_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_iti_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "main_intro"
  main_introClock = new util.Clock();
  main_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_intro_text',
    text: 'Main task. Remember: F = left tilt, J = right tilt.\n\nPress SPACE to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  main_intro_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "block_intro"
  block_introClock = new util.Clock();
  block_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'block_intro_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  block_intro_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "main_fixation"
  main_fixationClock = new util.Clock();
  main_fixation_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_fixation_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "main_decision"
  main_decisionClock = new util.Clock();
  main_gabor = new visual.GratingStim({
    win : psychoJS.window,
    name : 'main_gabor', units : undefined, 
    tex : undefined, mask : 'gauss',
    ori : 1.0, 
    pos : [0, 0],
    draggable: false,
    anchor : 'center',
    sf : 4.0, phase : 0.0,
    size : [0.18, 0.18],
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 0.8, blendmode : 'avg',
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  main_wait_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_wait_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  main_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "main_post"
  main_postClock = new util.Clock();
  post_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  confidence_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidence_prompt',
    text: 'How confident are you that your choice was correct?\n\n1       2       3       4       5       6\nGuessing                                  Certain',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  confidence_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "main_iti"
  main_itiClock = new util.Clock();
  main_iti_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_iti_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "block_break"
  block_breakClock = new util.Clock();
  block_break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'block_break_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  block_break_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  thanks_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks_text',
    text: 'The experiment is finished. Thank you!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var welcomeMaxDurationReached;
var _welcome_key_allKeys;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    welcomeClock.reset();
    routineTimer.reset();
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    welcome_key.keys = undefined;
    welcome_key.rt = undefined;
    _welcome_key_allKeys = [];
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_text);
    welcomeComponents.push(welcome_key);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }
    
    
    // if welcome_text is active this frame...
    if (welcome_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *welcome_key* updates
    if (t >= 0 && welcome_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_key.tStart = t;  // (not accounting for frame time here)
      welcome_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.clearEvents(); });
    }
    
    // if welcome_key is active this frame...
    if (welcome_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_key.getKeys({
        keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
        waitRelease: false
      });
      _welcome_key_allKeys = _welcome_key_allKeys.concat(theseKeys);
      if (_welcome_key_allKeys.length > 0) {
        welcome_key.keys = _welcome_key_allKeys[0].name;  // just the first key pressed
        welcome_key.rt = _welcome_key_allKeys[0].rt;
        welcome_key.duration = _welcome_key_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(welcome_key.corr, level);
    }
    psychoJS.experiment.addData('welcome_key.keys', welcome_key.keys);
    if (typeof welcome_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_key.rt', welcome_key.rt);
        psychoJS.experiment.addData('welcome_key.duration', welcome_key.duration);
        routineTimer.reset();
        }
    
    welcome_key.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var consentMaxDurationReached;
var _consent_key_allKeys;
var consentMaxDuration;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    consentClock.reset();
    routineTimer.reset();
    consentMaxDurationReached = false;
    // update component parameters for each repeat
    consent_key.keys = undefined;
    consent_key.rt = undefined;
    _consent_key_allKeys = [];
    psychoJS.experiment.addData('consent.started', globalClock.getTime());
    consentMaxDuration = null
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(consent_text);
    consentComponents.push(consent_key);
    
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent' ---
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consent_text* updates
    if (t >= 0 && consent_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_text.tStart = t;  // (not accounting for frame time here)
      consent_text.frameNStart = frameN;  // exact frame index
      
      consent_text.setAutoDraw(true);
    }
    
    
    // if consent_text is active this frame...
    if (consent_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *consent_key* updates
    if (t >= 0 && consent_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_key.tStart = t;  // (not accounting for frame time here)
      consent_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consent_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consent_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consent_key.clearEvents(); });
    }
    
    // if consent_key is active this frame...
    if (consent_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = consent_key.getKeys({
        keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
        waitRelease: false
      });
      _consent_key_allKeys = _consent_key_allKeys.concat(theseKeys);
      if (_consent_key_allKeys.length > 0) {
        consent_key.keys = _consent_key_allKeys[0].name;  // just the first key pressed
        consent_key.rt = _consent_key_allKeys[0].rt;
        consent_key.duration = _consent_key_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent' ---
    for (const thisComponent of consentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('consent.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(consent_key.corr, level);
    }
    psychoJS.experiment.addData('consent_key.keys', consent_key.keys);
    if (typeof consent_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent_key.rt', consent_key.rt);
        psychoJS.experiment.addData('consent_key.duration', consent_key.duration);
        routineTimer.reset();
        }
    
    consent_key.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructionsMaxDurationReached;
var _instructions_key_allKeys;
var instructionsMaxDuration;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionsClock.reset();
    routineTimer.reset();
    instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    instructions_key.keys = undefined;
    instructions_key.rt = undefined;
    _instructions_key_allKeys = [];
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    instructionsMaxDuration = null
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instructions_text);
    instructionsComponents.push(instructions_key);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }
    
    
    // if instructions_text is active this frame...
    if (instructions_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *instructions_key* updates
    if (t >= 0 && instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key.tStart = t;  // (not accounting for frame time here)
      instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key.clearEvents(); });
    }
    
    // if instructions_key is active this frame...
    if (instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key.getKeys({
        keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
        waitRelease: false
      });
      _instructions_key_allKeys = _instructions_key_allKeys.concat(theseKeys);
      if (_instructions_key_allKeys.length > 0) {
        instructions_key.keys = _instructions_key_allKeys[0].name;  // just the first key pressed
        instructions_key.rt = _instructions_key_allKeys[0].rt;
        instructions_key.duration = _instructions_key_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_key.corr, level);
    }
    psychoJS.experiment.addData('instructions_key.keys', instructions_key.keys);
    if (typeof instructions_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_key.rt', instructions_key.rt);
        psychoJS.experiment.addData('instructions_key.duration', instructions_key.duration);
        routineTimer.reset();
        }
    
    instructions_key.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var initializeMaxDurationReached;
var initializeMaxDuration;
var initializeComponents;
function initializeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'initialize' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    initializeClock.reset(routineTimer.getTime());
    routineTimer.add(0.050000);
    initializeMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('initialize.started', globalClock.getTime());
    initializeMaxDuration = 0.05
    // keep track of which components have finished
    initializeComponents = [];
    initializeComponents.push(init_fix);
    
    for (const thisComponent of initializeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function initializeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'initialize' ---
    // get current time
    t = initializeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > initializeMaxDuration) {
        initializeMaxDurationReached = true
        continueRoutine = false
    }
    
    // *init_fix* updates
    if (t >= 0 && init_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      init_fix.tStart = t;  // (not accounting for frame time here)
      init_fix.frameNStart = frameN;  // exact frame index
      
      init_fix.setAutoDraw(true);
    }
    
    
    // if init_fix is active this frame...
    if (init_fix.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0 + 0.05 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (init_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      init_fix.tStop = t;  // not accounting for scr refresh
      init_fix.frameNStop = frameN;  // exact frame index
      // update status
      init_fix.status = PsychoJS.Status.FINISHED;
      init_fix.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of initializeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initializeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'initialize' ---
    for (const thisComponent of initializeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('initialize.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (initializeMaxDurationReached) {
        initializeClock.add(initializeMaxDuration);
    } else {
        initializeClock.add(0.050000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var confidenceInstructionLoop;
function confidenceInstructionLoopLoopBegin(confidenceInstructionLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    confidenceInstructionLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: showConfInstr, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'confidenceInstructionLoop'
    });
    psychoJS.experiment.addLoop(confidenceInstructionLoop); // add the loop to the experiment
    currentLoop = confidenceInstructionLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisConfidenceInstructionLoop of confidenceInstructionLoop) {
      snapshot = confidenceInstructionLoop.getSnapshot();
      confidenceInstructionLoopLoopScheduler.add(importConditions(snapshot));
      confidenceInstructionLoopLoopScheduler.add(confidence_instructionsRoutineBegin(snapshot));
      confidenceInstructionLoopLoopScheduler.add(confidence_instructionsRoutineEachFrame());
      confidenceInstructionLoopLoopScheduler.add(confidence_instructionsRoutineEnd(snapshot));
      confidenceInstructionLoopLoopScheduler.add(confidenceInstructionLoopLoopEndIteration(confidenceInstructionLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function confidenceInstructionLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(confidenceInstructionLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function confidenceInstructionLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var neutralInstructionLoop;
function neutralInstructionLoopLoopBegin(neutralInstructionLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    neutralInstructionLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: showNeutralInstr, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'neutralInstructionLoop'
    });
    psychoJS.experiment.addLoop(neutralInstructionLoop); // add the loop to the experiment
    currentLoop = neutralInstructionLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNeutralInstructionLoop of neutralInstructionLoop) {
      snapshot = neutralInstructionLoop.getSnapshot();
      neutralInstructionLoopLoopScheduler.add(importConditions(snapshot));
      neutralInstructionLoopLoopScheduler.add(neutral_instructionsRoutineBegin(snapshot));
      neutralInstructionLoopLoopScheduler.add(neutral_instructionsRoutineEachFrame());
      neutralInstructionLoopLoopScheduler.add(neutral_instructionsRoutineEnd(snapshot));
      neutralInstructionLoopLoopScheduler.add(neutralInstructionLoopLoopEndIteration(neutralInstructionLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function neutralInstructionLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(neutralInstructionLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function neutralInstructionLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceTrials;
function practiceTrialsLoopBegin(practiceTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/two_orientations.csv',
      seed: undefined, name: 'practiceTrials'
    });
    psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
    currentLoop = practiceTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracticeTrial of practiceTrials) {
      snapshot = practiceTrials.getSnapshot();
      practiceTrialsLoopScheduler.add(importConditions(snapshot));
      practiceTrialsLoopScheduler.add(practice_fixationRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practice_fixationRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practice_fixationRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practice_decisionRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practice_decisionRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practice_decisionRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practice_feedbackRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practice_feedbackRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practice_feedbackRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practice_itiRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practice_itiRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practice_itiRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialsLoopEndIteration(practiceTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var calibrationTrialsConditions;
var calibrationTrials;
function calibrationTrialsLoopBegin(calibrationTrialsLoopScheduler, snapshot) {
  return async function() {
    // setup a MultiStairTrialHandler
    calibrationTrialsConditions = TrialHandler.importConditions(psychoJS.serverManager, 'conditions/quest_conditions.csv');
    calibrationTrials = new data.MultiStairHandler({stairType:MultiStairHandler.StaircaseType.QUEST, 
      psychoJS: psychoJS,
      name: 'calibrationTrials',
      varName: 'intensity',
      nTrials: 40.0,
      conditions: calibrationTrialsConditions,
      method: TrialHandler.Method.SEQUENTIAL
    });
    psychoJS.experiment.addLoop(calibrationTrials); // add the loop to the experiment
    currentLoop = calibrationTrials;  // we're now the current loop
    // Schedule all the trials in the trialList:
    for (const thisQuestLoop of calibrationTrials) {
      calibrationTrialsLoopScheduler.add(calibrationTrialsLoopBeginIteration(snapshot));
      snapshot = calibrationTrials.getSnapshot();
      calibrationTrialsLoopScheduler.add(importConditions(snapshot));
      calibrationTrialsLoopScheduler.add(calibration_fixationRoutineBegin(snapshot));
      calibrationTrialsLoopScheduler.add(calibration_fixationRoutineEachFrame());
      calibrationTrialsLoopScheduler.add(calibration_fixationRoutineEnd());
      snapshot = calibrationTrials.getSnapshot();
      calibrationTrialsLoopScheduler.add(importConditions(snapshot));
      calibrationTrialsLoopScheduler.add(calibration_decisionRoutineBegin(snapshot));
      calibrationTrialsLoopScheduler.add(calibration_decisionRoutineEachFrame());
      calibrationTrialsLoopScheduler.add(calibration_decisionRoutineEnd());
      snapshot = calibrationTrials.getSnapshot();
      calibrationTrialsLoopScheduler.add(importConditions(snapshot));
      calibrationTrialsLoopScheduler.add(calibration_itiRoutineBegin(snapshot));
      calibrationTrialsLoopScheduler.add(calibration_itiRoutineEachFrame());
      calibrationTrialsLoopScheduler.add(calibration_itiRoutineEnd());
    // then iterate over this loop (calibrationTrials)
    calibrationTrialsLoopScheduler.add(calibrationTrialsLoopEndIteration(calibrationTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var level;
function calibrationTrialsLoopBeginIteration(snapshot) {
  return async function() {
    // ------Prepare for next entry------
    level = calibrationTrials.intensity;

    return Scheduler.Event.NEXT;
  }
}


async function calibrationTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(calibrationTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function calibrationTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var baselineTrials;
function baselineTrialsLoopBegin(baselineTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    baselineTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/two_orientations.csv',
      seed: undefined, name: 'baselineTrials'
    });
    psychoJS.experiment.addLoop(baselineTrials); // add the loop to the experiment
    currentLoop = baselineTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBaselineTrial of baselineTrials) {
      snapshot = baselineTrials.getSnapshot();
      baselineTrialsLoopScheduler.add(importConditions(snapshot));
      baselineTrialsLoopScheduler.add(baseline_fixationRoutineBegin(snapshot));
      baselineTrialsLoopScheduler.add(baseline_fixationRoutineEachFrame());
      baselineTrialsLoopScheduler.add(baseline_fixationRoutineEnd(snapshot));
      baselineTrialsLoopScheduler.add(baseline_decisionRoutineBegin(snapshot));
      baselineTrialsLoopScheduler.add(baseline_decisionRoutineEachFrame());
      baselineTrialsLoopScheduler.add(baseline_decisionRoutineEnd(snapshot));
      baselineTrialsLoopScheduler.add(baseline_postRoutineBegin(snapshot));
      baselineTrialsLoopScheduler.add(baseline_postRoutineEachFrame());
      baselineTrialsLoopScheduler.add(baseline_postRoutineEnd(snapshot));
      baselineTrialsLoopScheduler.add(baseline_itiRoutineBegin(snapshot));
      baselineTrialsLoopScheduler.add(baseline_itiRoutineEachFrame());
      baselineTrialsLoopScheduler.add(baseline_itiRoutineEnd(snapshot));
      baselineTrialsLoopScheduler.add(baselineTrialsLoopEndIteration(baselineTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function baselineTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(baselineTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function baselineTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var mainBlocks;
function mainBlocksLoopBegin(mainBlocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mainBlocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'mainBlocks'
    });
    psychoJS.experiment.addLoop(mainBlocks); // add the loop to the experiment
    currentLoop = mainBlocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMainBlock of mainBlocks) {
      snapshot = mainBlocks.getSnapshot();
      mainBlocksLoopScheduler.add(importConditions(snapshot));
      mainBlocksLoopScheduler.add(block_introRoutineBegin(snapshot));
      mainBlocksLoopScheduler.add(block_introRoutineEachFrame());
      mainBlocksLoopScheduler.add(block_introRoutineEnd(snapshot));
      const mainTrialsLoopScheduler = new Scheduler(psychoJS);
      mainBlocksLoopScheduler.add(mainTrialsLoopBegin(mainTrialsLoopScheduler, snapshot));
      mainBlocksLoopScheduler.add(mainTrialsLoopScheduler);
      mainBlocksLoopScheduler.add(mainTrialsLoopEnd);
      mainBlocksLoopScheduler.add(block_breakRoutineBegin(snapshot));
      mainBlocksLoopScheduler.add(block_breakRoutineEachFrame());
      mainBlocksLoopScheduler.add(block_breakRoutineEnd(snapshot));
      mainBlocksLoopScheduler.add(mainBlocksLoopEndIteration(mainBlocksLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var mainTrials;
function mainTrialsLoopBegin(mainTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mainTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/two_orientations.csv',
      seed: undefined, name: 'mainTrials'
    });
    psychoJS.experiment.addLoop(mainTrials); // add the loop to the experiment
    currentLoop = mainTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMainTrial of mainTrials) {
      snapshot = mainTrials.getSnapshot();
      mainTrialsLoopScheduler.add(importConditions(snapshot));
      mainTrialsLoopScheduler.add(main_fixationRoutineBegin(snapshot));
      mainTrialsLoopScheduler.add(main_fixationRoutineEachFrame());
      mainTrialsLoopScheduler.add(main_fixationRoutineEnd(snapshot));
      mainTrialsLoopScheduler.add(main_decisionRoutineBegin(snapshot));
      mainTrialsLoopScheduler.add(main_decisionRoutineEachFrame());
      mainTrialsLoopScheduler.add(main_decisionRoutineEnd(snapshot));
      mainTrialsLoopScheduler.add(main_postRoutineBegin(snapshot));
      mainTrialsLoopScheduler.add(main_postRoutineEachFrame());
      mainTrialsLoopScheduler.add(main_postRoutineEnd(snapshot));
      mainTrialsLoopScheduler.add(main_itiRoutineBegin(snapshot));
      mainTrialsLoopScheduler.add(main_itiRoutineEachFrame());
      mainTrialsLoopScheduler.add(main_itiRoutineEnd(snapshot));
      mainTrialsLoopScheduler.add(mainTrialsLoopEndIteration(mainTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function mainTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mainTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mainTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function mainBlocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mainBlocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mainBlocksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var confidence_instructionsMaxDurationReached;
var _confidence_instructions_key_allKeys;
var confidence_instructionsMaxDuration;
var confidence_instructionsComponents;
function confidence_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'confidence_instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    confidence_instructionsClock.reset();
    routineTimer.reset();
    confidence_instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    confidence_instructions_key.keys = undefined;
    confidence_instructions_key.rt = undefined;
    _confidence_instructions_key_allKeys = [];
    psychoJS.experiment.addData('confidence_instructions.started', globalClock.getTime());
    confidence_instructionsMaxDuration = null
    // keep track of which components have finished
    confidence_instructionsComponents = [];
    confidence_instructionsComponents.push(confidence_instructions_text);
    confidence_instructionsComponents.push(confidence_instructions_key);
    
    for (const thisComponent of confidence_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function confidence_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'confidence_instructions' ---
    // get current time
    t = confidence_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *confidence_instructions_text* updates
    if (t >= 0 && confidence_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidence_instructions_text.tStart = t;  // (not accounting for frame time here)
      confidence_instructions_text.frameNStart = frameN;  // exact frame index
      
      confidence_instructions_text.setAutoDraw(true);
    }
    
    
    // if confidence_instructions_text is active this frame...
    if (confidence_instructions_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *confidence_instructions_key* updates
    if (t >= 0 && confidence_instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidence_instructions_key.tStart = t;  // (not accounting for frame time here)
      confidence_instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { confidence_instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { confidence_instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { confidence_instructions_key.clearEvents(); });
    }
    
    // if confidence_instructions_key is active this frame...
    if (confidence_instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = confidence_instructions_key.getKeys({
        keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
        waitRelease: false
      });
      _confidence_instructions_key_allKeys = _confidence_instructions_key_allKeys.concat(theseKeys);
      if (_confidence_instructions_key_allKeys.length > 0) {
        confidence_instructions_key.keys = _confidence_instructions_key_allKeys[0].name;  // just the first key pressed
        confidence_instructions_key.rt = _confidence_instructions_key_allKeys[0].rt;
        confidence_instructions_key.duration = _confidence_instructions_key_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of confidence_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function confidence_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'confidence_instructions' ---
    for (const thisComponent of confidence_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('confidence_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(confidence_instructions_key.corr, level);
    }
    psychoJS.experiment.addData('confidence_instructions_key.keys', confidence_instructions_key.keys);
    if (typeof confidence_instructions_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('confidence_instructions_key.rt', confidence_instructions_key.rt);
        psychoJS.experiment.addData('confidence_instructions_key.duration', confidence_instructions_key.duration);
        routineTimer.reset();
        }
    
    confidence_instructions_key.stop();
    // the Routine "confidence_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var neutral_instructionsMaxDurationReached;
var _neutral_instructions_key_allKeys;
var neutral_instructionsMaxDuration;
var neutral_instructionsComponents;
function neutral_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'neutral_instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    neutral_instructionsClock.reset();
    routineTimer.reset();
    neutral_instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    neutral_instructions_key.keys = undefined;
    neutral_instructions_key.rt = undefined;
    _neutral_instructions_key_allKeys = [];
    psychoJS.experiment.addData('neutral_instructions.started', globalClock.getTime());
    neutral_instructionsMaxDuration = null
    // keep track of which components have finished
    neutral_instructionsComponents = [];
    neutral_instructionsComponents.push(neutral_instructions_text);
    neutral_instructionsComponents.push(neutral_instructions_key);
    
    for (const thisComponent of neutral_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function neutral_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'neutral_instructions' ---
    // get current time
    t = neutral_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *neutral_instructions_text* updates
    if (t >= 0 && neutral_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      neutral_instructions_text.tStart = t;  // (not accounting for frame time here)
      neutral_instructions_text.frameNStart = frameN;  // exact frame index
      
      neutral_instructions_text.setAutoDraw(true);
    }
    
    
    // if neutral_instructions_text is active this frame...
    if (neutral_instructions_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *neutral_instructions_key* updates
    if (t >= 0 && neutral_instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      neutral_instructions_key.tStart = t;  // (not accounting for frame time here)
      neutral_instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { neutral_instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { neutral_instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { neutral_instructions_key.clearEvents(); });
    }
    
    // if neutral_instructions_key is active this frame...
    if (neutral_instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = neutral_instructions_key.getKeys({
        keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
        waitRelease: false
      });
      _neutral_instructions_key_allKeys = _neutral_instructions_key_allKeys.concat(theseKeys);
      if (_neutral_instructions_key_allKeys.length > 0) {
        neutral_instructions_key.keys = _neutral_instructions_key_allKeys[0].name;  // just the first key pressed
        neutral_instructions_key.rt = _neutral_instructions_key_allKeys[0].rt;
        neutral_instructions_key.duration = _neutral_instructions_key_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of neutral_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function neutral_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'neutral_instructions' ---
    for (const thisComponent of neutral_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('neutral_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(neutral_instructions_key.corr, level);
    }
    psychoJS.experiment.addData('neutral_instructions_key.keys', neutral_instructions_key.keys);
    if (typeof neutral_instructions_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('neutral_instructions_key.rt', neutral_instructions_key.rt);
        psychoJS.experiment.addData('neutral_instructions_key.duration', neutral_instructions_key.duration);
        routineTimer.reset();
        }
    
    neutral_instructions_key.stop();
    // the Routine "neutral_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_introMaxDurationReached;
var _practice_intro_key_allKeys;
var practice_introMaxDuration;
var practice_introComponents;
function practice_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_intro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practice_introClock.reset();
    routineTimer.reset();
    practice_introMaxDurationReached = false;
    // update component parameters for each repeat
    practice_intro_key.keys = undefined;
    practice_intro_key.rt = undefined;
    _practice_intro_key_allKeys = [];
    psychoJS.experiment.addData('practice_intro.started', globalClock.getTime());
    practice_introMaxDuration = null
    // keep track of which components have finished
    practice_introComponents = [];
    practice_introComponents.push(practice_intro_text);
    practice_introComponents.push(practice_intro_key);
    
    for (const thisComponent of practice_introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_intro' ---
    // get current time
    t = practice_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_intro_text* updates
    if (t >= 0 && practice_intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_intro_text.tStart = t;  // (not accounting for frame time here)
      practice_intro_text.frameNStart = frameN;  // exact frame index
      
      practice_intro_text.setAutoDraw(true);
    }
    
    
    // if practice_intro_text is active this frame...
    if (practice_intro_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *practice_intro_key* updates
    if (t >= 0 && practice_intro_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_intro_key.tStart = t;  // (not accounting for frame time here)
      practice_intro_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_intro_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_intro_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_intro_key.clearEvents(); });
    }
    
    // if practice_intro_key is active this frame...
    if (practice_intro_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_intro_key.getKeys({
        keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
        waitRelease: false
      });
      _practice_intro_key_allKeys = _practice_intro_key_allKeys.concat(theseKeys);
      if (_practice_intro_key_allKeys.length > 0) {
        practice_intro_key.keys = _practice_intro_key_allKeys[0].name;  // just the first key pressed
        practice_intro_key.rt = _practice_intro_key_allKeys[0].rt;
        practice_intro_key.duration = _practice_intro_key_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_intro' ---
    for (const thisComponent of practice_introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_intro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practice_intro_key.corr, level);
    }
    psychoJS.experiment.addData('practice_intro_key.keys', practice_intro_key.keys);
    if (typeof practice_intro_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_intro_key.rt', practice_intro_key.rt);
        psychoJS.experiment.addData('practice_intro_key.duration', practice_intro_key.duration);
        routineTimer.reset();
        }
    
    practice_intro_key.stop();
    // the Routine "practice_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_fixationMaxDurationReached;
var practice_fixationMaxDuration;
var practice_fixationComponents;
function practice_fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practice_fixationClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    practice_fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_fixation.started', globalClock.getTime());
    practice_fixationMaxDuration = null
    // keep track of which components have finished
    practice_fixationComponents = [];
    practice_fixationComponents.push(practice_fixation_fix);
    
    for (const thisComponent of practice_fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_fixation' ---
    // get current time
    t = practice_fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_fixation_fix* updates
    if (t >= 0 && practice_fixation_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_fixation_fix.tStart = t;  // (not accounting for frame time here)
      practice_fixation_fix.frameNStart = frameN;  // exact frame index
      
      practice_fixation_fix.setAutoDraw(true);
    }
    
    
    // if practice_fixation_fix is active this frame...
    if (practice_fixation_fix.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (practice_fixation_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      practice_fixation_fix.tStop = t;  // not accounting for scr refresh
      practice_fixation_fix.frameNStop = frameN;  // exact frame index
      // update status
      practice_fixation_fix.status = PsychoJS.Status.FINISHED;
      practice_fixation_fix.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_fixation' ---
    for (const thisComponent of practice_fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_fixation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (practice_fixationMaxDurationReached) {
        practice_fixationClock.add(practice_fixationMaxDuration);
    } else {
        practice_fixationClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_decisionMaxDurationReached;
var _practice_resp_allKeys;
var practice_decisionMaxDuration;
var practice_decisionComponents;
function practice_decisionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_decision' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practice_decisionClock.reset(routineTimer.getTime());
    routineTimer.add(1.500000);
    practice_decisionMaxDurationReached = false;
    // update component parameters for each repeat
    practice_gabor.setOri(tiltSign * 12);
    practice_resp.keys = undefined;
    practice_resp.rt = undefined;
    _practice_resp_allKeys = [];
    psychoJS.experiment.addData('practice_decision.started', globalClock.getTime());
    practice_decisionMaxDuration = null
    // keep track of which components have finished
    practice_decisionComponents = [];
    practice_decisionComponents.push(practice_gabor);
    practice_decisionComponents.push(practice_wait_fix);
    practice_decisionComponents.push(practice_resp);
    
    for (const thisComponent of practice_decisionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_decisionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_decision' ---
    // get current time
    t = practice_decisionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_gabor* updates
    if (t >= 0 && practice_gabor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_gabor.tStart = t;  // (not accounting for frame time here)
      practice_gabor.frameNStart = frameN;  // exact frame index
      
      practice_gabor.setAutoDraw(true);
    }
    
    
    // if practice_gabor is active this frame...
    if (practice_gabor.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0 + 0.15 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (practice_gabor.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      practice_gabor.tStop = t;  // not accounting for scr refresh
      practice_gabor.frameNStop = frameN;  // exact frame index
      // update status
      practice_gabor.status = PsychoJS.Status.FINISHED;
      practice_gabor.setAutoDraw(false);
    }
    
    
    // *practice_wait_fix* updates
    if (((practice_gabor.status == FINISHED)) && practice_wait_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_wait_fix.tStart = t;  // (not accounting for frame time here)
      practice_wait_fix.frameNStart = frameN;  // exact frame index
      
      practice_wait_fix.setAutoDraw(true);
    }
    
    
    // if practice_wait_fix is active this frame...
    if (practice_wait_fix.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if ((practice_wait_fix.status === PsychoJS.Status.STARTED || practice_wait_fix.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      // keep track of stop time/frame for later
      practice_wait_fix.tStop = t;  // not accounting for scr refresh
      practice_wait_fix.frameNStop = frameN;  // exact frame index
      // update status
      practice_wait_fix.status = PsychoJS.Status.FINISHED;
      practice_wait_fix.setAutoDraw(false);
    }
    
    
    // *practice_resp* updates
    if (t >= 0 && practice_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_resp.tStart = t;  // (not accounting for frame time here)
      practice_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_resp.clearEvents(); });
    }
    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (practice_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      practice_resp.tStop = t;  // not accounting for scr refresh
      practice_resp.frameNStop = frameN;  // exact frame index
      // update status
      practice_resp.status = PsychoJS.Status.FINISHED;
      frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (practice_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        practice_resp.tStop = t;  // not accounting for scr refresh
        practice_resp.frameNStop = frameN;  // exact frame index
        // update status
        practice_resp.status = PsychoJS.Status.FINISHED;
        practice_resp.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if practice_resp is active this frame...
      if (practice_resp.status === PsychoJS.Status.STARTED) {
        let theseKeys = practice_resp.getKeys({
          keyList: typeof [['f','j']] === 'string' ? [[['f','j']]] : [['f','j']], 
          waitRelease: false
        });
        _practice_resp_allKeys = _practice_resp_allKeys.concat(theseKeys);
        if (_practice_resp_allKeys.length > 0) {
          practice_resp.keys = _practice_resp_allKeys[0].name;  // just the first key pressed
          practice_resp.rt = _practice_resp_allKeys[0].rt;
          practice_resp.duration = _practice_resp_allKeys[0].duration;
          // was this correct?
          if (practice_resp.keys == corrAns) {
              practice_resp.corr = 1;
          } else {
              practice_resp.corr = 0;
          }
        }
      }
      
      // Run 'Each Frame' code from practice_minexposure
      if (practice_resp.keys !== undefined && practice_resp.keys !== null && practice_resp.keys.length > 0 && t >= 0.15) {
          continueRoutine = false;
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of practice_decisionComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function practice_decisionRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'practice_decision' ---
      for (const thisComponent of practice_decisionComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('practice_decision.stopped', globalClock.getTime());
      // was no response the correct answer?!
      if (practice_resp.keys === undefined) {
        if (['None','none',undefined].includes(corrAns)) {
           practice_resp.corr = 1;  // correct non-response
        } else {
           practice_resp.corr = 0;  // failed to respond (incorrectly)
        }
      }
      // store data for current loop
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(practice_resp.corr, level);
      }
      psychoJS.experiment.addData('practice_resp.keys', practice_resp.keys);
      psychoJS.experiment.addData('practice_resp.corr', practice_resp.corr);
      if (typeof practice_resp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('practice_resp.rt', practice_resp.rt);
          psychoJS.experiment.addData('practice_resp.duration', practice_resp.duration);
          }
      
      practice_resp.stop();
      // Run 'End Routine' code from practice_end
      psychoJS.experiment.addData('phase', 'practice');
      
      if (routineForceEnded) {
          routineTimer.reset();} else if (practice_decisionMaxDurationReached) {
          practice_decisionClock.add(practice_decisionMaxDuration);
      } else {
          practice_decisionClock.add(1.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var practice_feedbackMaxDurationReached;
var feedbackText;
var feedbackColor;
var practice_feedbackMaxDuration;
var practice_feedbackComponents;
function practice_feedbackRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'practice_feedback' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      practice_feedbackClock.reset(routineTimer.getTime());
      routineTimer.add(0.600000);
      practice_feedbackMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from practice_feedback_code
      if (practice_resp.keys === undefined || practice_resp.keys === null || practice_resp.keys.length === 0) {
          feedbackText = 'Too slow';
          feedbackColor = '#ffdc00';
      } else if (practice_resp.corr === 1) {
          feedbackText = 'Correct';
          feedbackColor = '#2ecc40';
      } else {
          feedbackText = 'Incorrect';
          feedbackColor = '#ff4136';
      }
      
      practice_feedback_text.setColor(new util.Color(feedbackColor));
      practice_feedback_text.setText(feedbackText);
      psychoJS.experiment.addData('practice_feedback.started', globalClock.getTime());
      practice_feedbackMaxDuration = null
      // keep track of which components have finished
      practice_feedbackComponents = [];
      practice_feedbackComponents.push(practice_feedback_text);
      
      for (const thisComponent of practice_feedbackComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  
function practice_feedbackRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'practice_feedback' ---
      // get current time
      t = practice_feedbackClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *practice_feedback_text* updates
      if (t >= 0 && practice_feedback_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        practice_feedback_text.tStart = t;  // (not accounting for frame time here)
        practice_feedback_text.frameNStart = frameN;  // exact frame index
        
        practice_feedback_text.setAutoDraw(true);
      }
      
      
      // if practice_feedback_text is active this frame...
      if (practice_feedback_text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (practice_feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        practice_feedback_text.tStop = t;  // not accounting for scr refresh
        practice_feedback_text.frameNStop = frameN;  // exact frame index
        // update status
        practice_feedback_text.status = PsychoJS.Status.FINISHED;
        practice_feedback_text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of practice_feedbackComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function practice_feedbackRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'practice_feedback' ---
      for (const thisComponent of practice_feedbackComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('practice_feedback.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (practice_feedbackMaxDurationReached) {
          practice_feedbackClock.add(practice_feedbackMaxDuration);
      } else {
          practice_feedbackClock.add(0.600000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var practice_itiMaxDurationReached;
var practice_itiMaxDuration;
var practice_itiComponents;
function practice_itiRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'practice_iti' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      practice_itiClock.reset(routineTimer.getTime());
      routineTimer.add(0.500000);
      practice_itiMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('practice_iti.started', globalClock.getTime());
      practice_itiMaxDuration = null
      // keep track of which components have finished
      practice_itiComponents = [];
      practice_itiComponents.push(practice_iti_fix);
      
      for (const thisComponent of practice_itiComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  
function practice_itiRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'practice_iti' ---
      // get current time
      t = practice_itiClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *practice_iti_fix* updates
      if (t >= 0 && practice_iti_fix.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        practice_iti_fix.tStart = t;  // (not accounting for frame time here)
        practice_iti_fix.frameNStart = frameN;  // exact frame index
        
        practice_iti_fix.setAutoDraw(true);
      }
      
      
      // if practice_iti_fix is active this frame...
      if (practice_iti_fix.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (practice_iti_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        practice_iti_fix.tStop = t;  // not accounting for scr refresh
        practice_iti_fix.frameNStop = frameN;  // exact frame index
        // update status
        practice_iti_fix.status = PsychoJS.Status.FINISHED;
        practice_iti_fix.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of practice_itiComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function practice_itiRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'practice_iti' ---
      for (const thisComponent of practice_itiComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('practice_iti.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (practice_itiMaxDurationReached) {
          practice_itiClock.add(practice_itiMaxDuration);
      } else {
          practice_itiClock.add(0.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var calibration_introMaxDurationReached;
var _calibration_intro_key_allKeys;
var calibration_introMaxDuration;
var calibration_introComponents;
function calibration_introRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'calibration_intro' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      calibration_introClock.reset();
      routineTimer.reset();
      calibration_introMaxDurationReached = false;
      // update component parameters for each repeat
      calibration_intro_key.keys = undefined;
      calibration_intro_key.rt = undefined;
      _calibration_intro_key_allKeys = [];
      psychoJS.experiment.addData('calibration_intro.started', globalClock.getTime());
      calibration_introMaxDuration = null
      // keep track of which components have finished
      calibration_introComponents = [];
      calibration_introComponents.push(calibration_intro_text);
      calibration_introComponents.push(calibration_intro_key);
      
      for (const thisComponent of calibration_introComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  
function calibration_introRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'calibration_intro' ---
      // get current time
      t = calibration_introClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *calibration_intro_text* updates
      if (t >= 0 && calibration_intro_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        calibration_intro_text.tStart = t;  // (not accounting for frame time here)
        calibration_intro_text.frameNStart = frameN;  // exact frame index
        
        calibration_intro_text.setAutoDraw(true);
      }
      
      
      // if calibration_intro_text is active this frame...
      if (calibration_intro_text.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *calibration_intro_key* updates
      if (t >= 0 && calibration_intro_key.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        calibration_intro_key.tStart = t;  // (not accounting for frame time here)
        calibration_intro_key.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { calibration_intro_key.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { calibration_intro_key.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { calibration_intro_key.clearEvents(); });
      }
      
      // if calibration_intro_key is active this frame...
      if (calibration_intro_key.status === PsychoJS.Status.STARTED) {
        let theseKeys = calibration_intro_key.getKeys({
          keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
          waitRelease: false
        });
        _calibration_intro_key_allKeys = _calibration_intro_key_allKeys.concat(theseKeys);
        if (_calibration_intro_key_allKeys.length > 0) {
          calibration_intro_key.keys = _calibration_intro_key_allKeys[0].name;  // just the first key pressed
          calibration_intro_key.rt = _calibration_intro_key_allKeys[0].rt;
          calibration_intro_key.duration = _calibration_intro_key_allKeys[0].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of calibration_introComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function calibration_introRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'calibration_intro' ---
      for (const thisComponent of calibration_introComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('calibration_intro.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(calibration_intro_key.corr, level);
      }
      psychoJS.experiment.addData('calibration_intro_key.keys', calibration_intro_key.keys);
      if (typeof calibration_intro_key.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('calibration_intro_key.rt', calibration_intro_key.rt);
          psychoJS.experiment.addData('calibration_intro_key.duration', calibration_intro_key.duration);
          routineTimer.reset();
          }
      
      calibration_intro_key.stop();
      // the Routine "calibration_intro" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var calibration_fixationMaxDurationReached;
var calibration_fixationMaxDuration;
var calibration_fixationComponents;
function calibration_fixationRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'calibration_fixation' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      calibration_fixationClock.reset(routineTimer.getTime());
      routineTimer.add(0.500000);
      calibration_fixationMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('calibration_fixation.started', globalClock.getTime());
      calibration_fixationMaxDuration = null
      // keep track of which components have finished
      calibration_fixationComponents = [];
      calibration_fixationComponents.push(calibration_fixation_fix);
      
      for (const thisComponent of calibration_fixationComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  
function calibration_fixationRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'calibration_fixation' ---
      // get current time
      t = calibration_fixationClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *calibration_fixation_fix* updates
      if (t >= 0 && calibration_fixation_fix.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        calibration_fixation_fix.tStart = t;  // (not accounting for frame time here)
        calibration_fixation_fix.frameNStart = frameN;  // exact frame index
        
        calibration_fixation_fix.setAutoDraw(true);
      }
      
      
      // if calibration_fixation_fix is active this frame...
      if (calibration_fixation_fix.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (calibration_fixation_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        calibration_fixation_fix.tStop = t;  // not accounting for scr refresh
        calibration_fixation_fix.frameNStop = frameN;  // exact frame index
        // update status
        calibration_fixation_fix.status = PsychoJS.Status.FINISHED;
        calibration_fixation_fix.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of calibration_fixationComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function calibration_fixationRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'calibration_fixation' ---
      for (const thisComponent of calibration_fixationComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('calibration_fixation.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (calibration_fixationMaxDurationReached) {
          calibration_fixationClock.add(calibration_fixationMaxDuration);
      } else {
          calibration_fixationClock.add(0.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var calibration_decisionMaxDurationReached;
var calibTiltSign;
var calibCorrAns;
var _calibration_resp_allKeys;
var calibration_decisionMaxDuration;
var calibration_decisionComponents;
function calibration_decisionRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'calibration_decision' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      calibration_decisionClock.reset(routineTimer.getTime());
      routineTimer.add(1.500000);
      calibration_decisionMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from calibration_setup
      if (Math.random() < 0.5) {
          calibTiltSign = -1;
          calibCorrAns = 'f';
      } else {
          calibTiltSign = 1;
          calibCorrAns = 'j';
      }
      
      calibration_gabor.setOri(calibTiltSign * level);
      calibration_resp.keys = undefined;
      calibration_resp.rt = undefined;
      _calibration_resp_allKeys = [];
      psychoJS.experiment.addData('calibration_decision.started', globalClock.getTime());
      calibration_decisionMaxDuration = null
      // keep track of which components have finished
      calibration_decisionComponents = [];
      calibration_decisionComponents.push(calibration_gabor);
      calibration_decisionComponents.push(calibration_wait_fix);
      calibration_decisionComponents.push(calibration_resp);
      
      for (const thisComponent of calibration_decisionComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  
function calibration_decisionRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'calibration_decision' ---
      // get current time
      t = calibration_decisionClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *calibration_gabor* updates
      if (t >= 0 && calibration_gabor.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        calibration_gabor.tStart = t;  // (not accounting for frame time here)
        calibration_gabor.frameNStart = frameN;  // exact frame index
        
        calibration_gabor.setAutoDraw(true);
      }
      
      
      // if calibration_gabor is active this frame...
      if (calibration_gabor.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 0.15 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (calibration_gabor.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        calibration_gabor.tStop = t;  // not accounting for scr refresh
        calibration_gabor.frameNStop = frameN;  // exact frame index
        // update status
        calibration_gabor.status = PsychoJS.Status.FINISHED;
        calibration_gabor.setAutoDraw(false);
      }
      
      
      // *calibration_wait_fix* updates
      if (((calibration_gabor.status == FINISHED)) && calibration_wait_fix.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        calibration_wait_fix.tStart = t;  // (not accounting for frame time here)
        calibration_wait_fix.frameNStart = frameN;  // exact frame index
        
        calibration_wait_fix.setAutoDraw(true);
      }
      
      
      // if calibration_wait_fix is active this frame...
      if (calibration_wait_fix.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if ((calibration_wait_fix.status === PsychoJS.Status.STARTED || calibration_wait_fix.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
        // keep track of stop time/frame for later
        calibration_wait_fix.tStop = t;  // not accounting for scr refresh
        calibration_wait_fix.frameNStop = frameN;  // exact frame index
        // update status
        calibration_wait_fix.status = PsychoJS.Status.FINISHED;
        calibration_wait_fix.setAutoDraw(false);
      }
      
      
      // *calibration_resp* updates
      if (t >= 0 && calibration_resp.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        calibration_resp.tStart = t;  // (not accounting for frame time here)
        calibration_resp.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { calibration_resp.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { calibration_resp.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { calibration_resp.clearEvents(); });
      }
      frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (calibration_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        calibration_resp.tStop = t;  // not accounting for scr refresh
        calibration_resp.frameNStop = frameN;  // exact frame index
        // update status
        calibration_resp.status = PsychoJS.Status.FINISHED;
        frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (calibration_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          calibration_resp.tStop = t;  // not accounting for scr refresh
          calibration_resp.frameNStop = frameN;  // exact frame index
          // update status
          calibration_resp.status = PsychoJS.Status.FINISHED;
          calibration_resp.status = PsychoJS.Status.FINISHED;
            }
          
        }
        
        // if calibration_resp is active this frame...
        if (calibration_resp.status === PsychoJS.Status.STARTED) {
          let theseKeys = calibration_resp.getKeys({
            keyList: typeof [['f','j']] === 'string' ? [[['f','j']]] : [['f','j']], 
            waitRelease: false
          });
          _calibration_resp_allKeys = _calibration_resp_allKeys.concat(theseKeys);
          if (_calibration_resp_allKeys.length > 0) {
            calibration_resp.keys = _calibration_resp_allKeys[0].name;  // just the first key pressed
            calibration_resp.rt = _calibration_resp_allKeys[0].rt;
            calibration_resp.duration = _calibration_resp_allKeys[0].duration;
            // was this correct?
            if (calibration_resp.keys == calibCorrAns) {
                calibration_resp.corr = 1;
            } else {
                calibration_resp.corr = 0;
            }
          }
        }
        
        // Run 'Each Frame' code from calibration_minexposure
        if (calibration_resp.keys !== undefined && calibration_resp.keys !== null && calibration_resp.keys.length > 0 && t >= 0.15) {
            continueRoutine = false;
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        for (const thisComponent of calibration_decisionComponents)
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
            break;
          }
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function calibration_decisionRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'calibration_decision' ---
        for (const thisComponent of calibration_decisionComponents) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        }
        psychoJS.experiment.addData('calibration_decision.stopped', globalClock.getTime());
        // was no response the correct answer?!
        if (calibration_resp.keys === undefined) {
          if (['None','none',undefined].includes(calibCorrAns)) {
             calibration_resp.corr = 1;  // correct non-response
          } else {
             calibration_resp.corr = 0;  // failed to respond (incorrectly)
          }
        }
        // store data for current loop
        // update the trial handler
        if (currentLoop instanceof MultiStairHandler) {
          currentLoop.addResponse(calibration_resp.corr, level);
        }
        psychoJS.experiment.addData('calibration_resp.keys', calibration_resp.keys);
        psychoJS.experiment.addData('calibration_resp.corr', calibration_resp.corr);
        if (typeof calibration_resp.keys !== 'undefined') {  // we had a response
            psychoJS.experiment.addData('calibration_resp.rt', calibration_resp.rt);
            psychoJS.experiment.addData('calibration_resp.duration', calibration_resp.duration);
            }
        
        calibration_resp.stop();
        // Run 'End Routine' code from calibration_end
        questLevels.push(Number(level));
        psychoJS.experiment.addData('phase', 'calibration');
        psychoJS.experiment.addData('tiltSignUsed', calibTiltSign);
        psychoJS.experiment.addData('corrAns', calibCorrAns);
        
        if (routineForceEnded) {
            routineTimer.reset();} else if (calibration_decisionMaxDurationReached) {
            calibration_decisionClock.add(calibration_decisionMaxDuration);
        } else {
            calibration_decisionClock.add(1.500000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var calibration_itiMaxDurationReached;
var calibration_itiMaxDuration;
var calibration_itiComponents;
function calibration_itiRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'calibration_iti' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        calibration_itiClock.reset(routineTimer.getTime());
        routineTimer.add(0.500000);
        calibration_itiMaxDurationReached = false;
        // update component parameters for each repeat
        psychoJS.experiment.addData('calibration_iti.started', globalClock.getTime());
        calibration_itiMaxDuration = null
        // keep track of which components have finished
        calibration_itiComponents = [];
        calibration_itiComponents.push(calibration_iti_fix);
        
        for (const thisComponent of calibration_itiComponents)
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
        return Scheduler.Event.NEXT;
      }
    }
    
    
function calibration_itiRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'calibration_iti' ---
        // get current time
        t = calibration_itiClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *calibration_iti_fix* updates
        if (t >= 0 && calibration_iti_fix.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          calibration_iti_fix.tStart = t;  // (not accounting for frame time here)
          calibration_iti_fix.frameNStart = frameN;  // exact frame index
          
          calibration_iti_fix.setAutoDraw(true);
        }
        
        
        // if calibration_iti_fix is active this frame...
        if (calibration_iti_fix.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (calibration_iti_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          calibration_iti_fix.tStop = t;  // not accounting for scr refresh
          calibration_iti_fix.frameNStop = frameN;  // exact frame index
          // update status
          calibration_iti_fix.status = PsychoJS.Status.FINISHED;
          calibration_iti_fix.setAutoDraw(false);
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        for (const thisComponent of calibration_itiComponents)
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
            break;
          }
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function calibration_itiRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'calibration_iti' ---
        for (const thisComponent of calibration_itiComponents) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        }
        psychoJS.experiment.addData('calibration_iti.stopped', globalClock.getTime());
        if (routineForceEnded) {
            routineTimer.reset();} else if (calibration_itiMaxDurationReached) {
            calibration_itiClock.add(calibration_itiMaxDuration);
        } else {
            calibration_itiClock.add(0.500000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var calibration_summaryMaxDurationReached;
var tiltDeg;
var calibration_summaryMaxDuration;
var calibration_summaryComponents;
function calibration_summaryRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'calibration_summary' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        calibration_summaryClock.reset(routineTimer.getTime());
        routineTimer.add(0.500000);
        calibration_summaryMaxDurationReached = false;
        // update component parameters for each repeat
        // Run 'Begin Routine' code from calibration_summary_code
        let lastLevels = questLevels.slice(-10);
        tiltDeg = medianValue(lastLevels);
        tiltDeg = Math.min(Math.max(tiltDeg, 1.0), 15.0);
        psychoJS.experiment.addData('calibratedTiltDeg', tiltDeg);
        psychoJS.experiment.addData('calibrationAtBoundary', (tiltDeg <= 1.0 || tiltDeg >= 15.0) ? 1 : 0);
        
        psychoJS.experiment.addData('calibration_summary.started', globalClock.getTime());
        calibration_summaryMaxDuration = 0.5
        // keep track of which components have finished
        calibration_summaryComponents = [];
        calibration_summaryComponents.push(calibration_done_text);
        
        for (const thisComponent of calibration_summaryComponents)
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
        return Scheduler.Event.NEXT;
      }
    }
    
    
function calibration_summaryRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'calibration_summary' ---
        // get current time
        t = calibration_summaryClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        // is it time to end the Routine? (based on local clock)
        if (t > calibration_summaryMaxDuration) {
            calibration_summaryMaxDurationReached = true
            continueRoutine = false
        }
        
        // *calibration_done_text* updates
        if (t >= 0 && calibration_done_text.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          calibration_done_text.tStart = t;  // (not accounting for frame time here)
          calibration_done_text.frameNStart = frameN;  // exact frame index
          
          calibration_done_text.setAutoDraw(true);
        }
        
        
        // if calibration_done_text is active this frame...
        if (calibration_done_text.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (calibration_done_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          calibration_done_text.tStop = t;  // not accounting for scr refresh
          calibration_done_text.frameNStop = frameN;  // exact frame index
          // update status
          calibration_done_text.status = PsychoJS.Status.FINISHED;
          calibration_done_text.setAutoDraw(false);
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        for (const thisComponent of calibration_summaryComponents)
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
            break;
          }
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function calibration_summaryRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'calibration_summary' ---
        for (const thisComponent of calibration_summaryComponents) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        }
        psychoJS.experiment.addData('calibration_summary.stopped', globalClock.getTime());
        if (routineForceEnded) {
            routineTimer.reset();} else if (calibration_summaryMaxDurationReached) {
            calibration_summaryClock.add(calibration_summaryMaxDuration);
        } else {
            calibration_summaryClock.add(0.500000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var baseline_introMaxDurationReached;
var _baseline_intro_key_allKeys;
var baseline_introMaxDuration;
var baseline_introComponents;
function baseline_introRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'baseline_intro' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        baseline_introClock.reset();
        routineTimer.reset();
        baseline_introMaxDurationReached = false;
        // update component parameters for each repeat
        baseline_intro_key.keys = undefined;
        baseline_intro_key.rt = undefined;
        _baseline_intro_key_allKeys = [];
        psychoJS.experiment.addData('baseline_intro.started', globalClock.getTime());
        baseline_introMaxDuration = null
        // keep track of which components have finished
        baseline_introComponents = [];
        baseline_introComponents.push(baseline_intro_text);
        baseline_introComponents.push(baseline_intro_key);
        
        for (const thisComponent of baseline_introComponents)
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
        return Scheduler.Event.NEXT;
      }
    }
    
    
function baseline_introRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'baseline_intro' ---
        // get current time
        t = baseline_introClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *baseline_intro_text* updates
        if (t >= 0 && baseline_intro_text.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          baseline_intro_text.tStart = t;  // (not accounting for frame time here)
          baseline_intro_text.frameNStart = frameN;  // exact frame index
          
          baseline_intro_text.setAutoDraw(true);
        }
        
        
        // if baseline_intro_text is active this frame...
        if (baseline_intro_text.status === PsychoJS.Status.STARTED) {
        }
        
        
        // *baseline_intro_key* updates
        if (t >= 0 && baseline_intro_key.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          baseline_intro_key.tStart = t;  // (not accounting for frame time here)
          baseline_intro_key.frameNStart = frameN;  // exact frame index
          
          // keyboard checking is just starting
          psychoJS.window.callOnFlip(function() { baseline_intro_key.clock.reset(); });  // t=0 on next screen flip
          psychoJS.window.callOnFlip(function() { baseline_intro_key.start(); }); // start on screen flip
          psychoJS.window.callOnFlip(function() { baseline_intro_key.clearEvents(); });
        }
        
        // if baseline_intro_key is active this frame...
        if (baseline_intro_key.status === PsychoJS.Status.STARTED) {
          let theseKeys = baseline_intro_key.getKeys({
            keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
            waitRelease: false
          });
          _baseline_intro_key_allKeys = _baseline_intro_key_allKeys.concat(theseKeys);
          if (_baseline_intro_key_allKeys.length > 0) {
            baseline_intro_key.keys = _baseline_intro_key_allKeys[0].name;  // just the first key pressed
            baseline_intro_key.rt = _baseline_intro_key_allKeys[0].rt;
            baseline_intro_key.duration = _baseline_intro_key_allKeys[0].duration;
            // a response ends the routine
            continueRoutine = false;
          }
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        for (const thisComponent of baseline_introComponents)
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
            break;
          }
        
        // refresh the screen if continuing
        if (continueRoutine) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function baseline_introRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'baseline_intro' ---
        for (const thisComponent of baseline_introComponents) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        }
        psychoJS.experiment.addData('baseline_intro.stopped', globalClock.getTime());
        // update the trial handler
        if (currentLoop instanceof MultiStairHandler) {
          currentLoop.addResponse(baseline_intro_key.corr, level);
        }
        psychoJS.experiment.addData('baseline_intro_key.keys', baseline_intro_key.keys);
        if (typeof baseline_intro_key.keys !== 'undefined') {  // we had a response
            psychoJS.experiment.addData('baseline_intro_key.rt', baseline_intro_key.rt);
            psychoJS.experiment.addData('baseline_intro_key.duration', baseline_intro_key.duration);
            routineTimer.reset();
            }
        
        baseline_intro_key.stop();
        // the Routine "baseline_intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset();
        
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var baseline_fixationMaxDurationReached;
var baseline_fixationMaxDuration;
var baseline_fixationComponents;
function baseline_fixationRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'baseline_fixation' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        baseline_fixationClock.reset(routineTimer.getTime());
        routineTimer.add(0.500000);
        baseline_fixationMaxDurationReached = false;
        // update component parameters for each repeat
        psychoJS.experiment.addData('baseline_fixation.started', globalClock.getTime());
        baseline_fixationMaxDuration = null
        // keep track of which components have finished
        baseline_fixationComponents = [];
        baseline_fixationComponents.push(baseline_fixation_fix);
        
        for (const thisComponent of baseline_fixationComponents)
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
        return Scheduler.Event.NEXT;
      }
    }
    
    
function baseline_fixationRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'baseline_fixation' ---
        // get current time
        t = baseline_fixationClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *baseline_fixation_fix* updates
        if (t >= 0 && baseline_fixation_fix.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          baseline_fixation_fix.tStart = t;  // (not accounting for frame time here)
          baseline_fixation_fix.frameNStart = frameN;  // exact frame index
          
          baseline_fixation_fix.setAutoDraw(true);
        }
        
        
        // if baseline_fixation_fix is active this frame...
        if (baseline_fixation_fix.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (baseline_fixation_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          baseline_fixation_fix.tStop = t;  // not accounting for scr refresh
          baseline_fixation_fix.frameNStop = frameN;  // exact frame index
          // update status
          baseline_fixation_fix.status = PsychoJS.Status.FINISHED;
          baseline_fixation_fix.setAutoDraw(false);
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        for (const thisComponent of baseline_fixationComponents)
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
            break;
          }
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function baseline_fixationRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'baseline_fixation' ---
        for (const thisComponent of baseline_fixationComponents) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        }
        psychoJS.experiment.addData('baseline_fixation.stopped', globalClock.getTime());
        if (routineForceEnded) {
            routineTimer.reset();} else if (baseline_fixationMaxDurationReached) {
            baseline_fixationClock.add(baseline_fixationMaxDuration);
        } else {
            baseline_fixationClock.add(0.500000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var baseline_decisionMaxDurationReached;
var _baseline_resp_allKeys;
var baseline_decisionMaxDuration;
var baseline_decisionComponents;
function baseline_decisionRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'baseline_decision' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        baseline_decisionClock.reset(routineTimer.getTime());
        routineTimer.add(1.500000);
        baseline_decisionMaxDurationReached = false;
        // update component parameters for each repeat
        baseline_gabor.setOri(tiltSign * tiltDeg);
        baseline_resp.keys = undefined;
        baseline_resp.rt = undefined;
        _baseline_resp_allKeys = [];
        psychoJS.experiment.addData('baseline_decision.started', globalClock.getTime());
        baseline_decisionMaxDuration = null
        // keep track of which components have finished
        baseline_decisionComponents = [];
        baseline_decisionComponents.push(baseline_gabor);
        baseline_decisionComponents.push(baseline_wait_fix);
        baseline_decisionComponents.push(baseline_resp);
        
        for (const thisComponent of baseline_decisionComponents)
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
        return Scheduler.Event.NEXT;
      }
    }
    
    
function baseline_decisionRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'baseline_decision' ---
        // get current time
        t = baseline_decisionClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *baseline_gabor* updates
        if (t >= 0 && baseline_gabor.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          baseline_gabor.tStart = t;  // (not accounting for frame time here)
          baseline_gabor.frameNStart = frameN;  // exact frame index
          
          baseline_gabor.setAutoDraw(true);
        }
        
        
        // if baseline_gabor is active this frame...
        if (baseline_gabor.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0 + 0.15 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (baseline_gabor.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          baseline_gabor.tStop = t;  // not accounting for scr refresh
          baseline_gabor.frameNStop = frameN;  // exact frame index
          // update status
          baseline_gabor.status = PsychoJS.Status.FINISHED;
          baseline_gabor.setAutoDraw(false);
        }
        
        
        // *baseline_wait_fix* updates
        if (((baseline_gabor.status == FINISHED)) && baseline_wait_fix.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          baseline_wait_fix.tStart = t;  // (not accounting for frame time here)
          baseline_wait_fix.frameNStart = frameN;  // exact frame index
          
          baseline_wait_fix.setAutoDraw(true);
        }
        
        
        // if baseline_wait_fix is active this frame...
        if (baseline_wait_fix.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if ((baseline_wait_fix.status === PsychoJS.Status.STARTED || baseline_wait_fix.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
          // keep track of stop time/frame for later
          baseline_wait_fix.tStop = t;  // not accounting for scr refresh
          baseline_wait_fix.frameNStop = frameN;  // exact frame index
          // update status
          baseline_wait_fix.status = PsychoJS.Status.FINISHED;
          baseline_wait_fix.setAutoDraw(false);
        }
        
        
        // *baseline_resp* updates
        if (t >= 0 && baseline_resp.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          baseline_resp.tStart = t;  // (not accounting for frame time here)
          baseline_resp.frameNStart = frameN;  // exact frame index
          
          // keyboard checking is just starting
          psychoJS.window.callOnFlip(function() { baseline_resp.clock.reset(); });  // t=0 on next screen flip
          psychoJS.window.callOnFlip(function() { baseline_resp.start(); }); // start on screen flip
          psychoJS.window.callOnFlip(function() { baseline_resp.clearEvents(); });
        }
        frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (baseline_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          baseline_resp.tStop = t;  // not accounting for scr refresh
          baseline_resp.frameNStop = frameN;  // exact frame index
          // update status
          baseline_resp.status = PsychoJS.Status.FINISHED;
          frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (baseline_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            baseline_resp.tStop = t;  // not accounting for scr refresh
            baseline_resp.frameNStop = frameN;  // exact frame index
            // update status
            baseline_resp.status = PsychoJS.Status.FINISHED;
            baseline_resp.status = PsychoJS.Status.FINISHED;
              }
            
          }
          
          // if baseline_resp is active this frame...
          if (baseline_resp.status === PsychoJS.Status.STARTED) {
            let theseKeys = baseline_resp.getKeys({
              keyList: typeof [['f','j']] === 'string' ? [[['f','j']]] : [['f','j']], 
              waitRelease: false
            });
            _baseline_resp_allKeys = _baseline_resp_allKeys.concat(theseKeys);
            if (_baseline_resp_allKeys.length > 0) {
              baseline_resp.keys = _baseline_resp_allKeys[0].name;  // just the first key pressed
              baseline_resp.rt = _baseline_resp_allKeys[0].rt;
              baseline_resp.duration = _baseline_resp_allKeys[0].duration;
              // was this correct?
              if (baseline_resp.keys == corrAns) {
                  baseline_resp.corr = 1;
              } else {
                  baseline_resp.corr = 0;
              }
            }
          }
          
          // Run 'Each Frame' code from baseline_minexposure
          if (baseline_resp.keys !== undefined && baseline_resp.keys !== null && baseline_resp.keys.length > 0 && t >= 0.15) {
              continueRoutine = false;
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of baseline_decisionComponents)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine && routineTimer.getTime() > 0) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      
function baseline_decisionRoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'baseline_decision' ---
          for (const thisComponent of baseline_decisionComponents) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('baseline_decision.stopped', globalClock.getTime());
          // was no response the correct answer?!
          if (baseline_resp.keys === undefined) {
            if (['None','none',undefined].includes(corrAns)) {
               baseline_resp.corr = 1;  // correct non-response
            } else {
               baseline_resp.corr = 0;  // failed to respond (incorrectly)
            }
          }
          // store data for current loop
          // update the trial handler
          if (currentLoop instanceof MultiStairHandler) {
            currentLoop.addResponse(baseline_resp.corr, level);
          }
          psychoJS.experiment.addData('baseline_resp.keys', baseline_resp.keys);
          psychoJS.experiment.addData('baseline_resp.corr', baseline_resp.corr);
          if (typeof baseline_resp.keys !== 'undefined') {  // we had a response
              psychoJS.experiment.addData('baseline_resp.rt', baseline_resp.rt);
              psychoJS.experiment.addData('baseline_resp.duration', baseline_resp.duration);
              }
          
          baseline_resp.stop();
          // Run 'End Routine' code from baseline_end
          psychoJS.experiment.addData('phase', 'baseline');
          
          psychoJS.experiment.addData('tiltDegUsed', tiltDeg);
          psychoJS.experiment.addData('probeScheduled', 0);
          
          if (routineForceEnded) {
              routineTimer.reset();} else if (baseline_decisionMaxDurationReached) {
              baseline_decisionClock.add(baseline_decisionMaxDuration);
          } else {
              baseline_decisionClock.add(1.500000);
          }
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      
var baseline_postMaxDurationReached;
var baseline_postMaxDuration;
var baseline_postComponents;
function baseline_postRoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'baseline_post' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          baseline_postClock.reset(routineTimer.getTime());
          routineTimer.add(1.500000);
          baseline_postMaxDurationReached = false;
          // update component parameters for each repeat
          psychoJS.experiment.addData('baseline_post.started', globalClock.getTime());
          baseline_postMaxDuration = 1.5
          // keep track of which components have finished
          baseline_postComponents = [];
          baseline_postComponents.push(baseline_post_fix);
          
          for (const thisComponent of baseline_postComponents)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      
function baseline_postRoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'baseline_post' ---
          // get current time
          t = baseline_postClock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          // is it time to end the Routine? (based on local clock)
          if (t > baseline_postMaxDuration) {
              baseline_postMaxDurationReached = true
              continueRoutine = false
          }
          
          // *baseline_post_fix* updates
          if (t >= 0 && baseline_post_fix.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            baseline_post_fix.tStart = t;  // (not accounting for frame time here)
            baseline_post_fix.frameNStart = frameN;  // exact frame index
            
            baseline_post_fix.setAutoDraw(true);
          }
          
          
          // if baseline_post_fix is active this frame...
          if (baseline_post_fix.status === PsychoJS.Status.STARTED) {
          }
          
          frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (baseline_post_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            baseline_post_fix.tStop = t;  // not accounting for scr refresh
            baseline_post_fix.frameNStop = frameN;  // exact frame index
            // update status
            baseline_post_fix.status = PsychoJS.Status.FINISHED;
            baseline_post_fix.setAutoDraw(false);
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of baseline_postComponents)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine && routineTimer.getTime() > 0) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      
function baseline_postRoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'baseline_post' ---
          for (const thisComponent of baseline_postComponents) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('baseline_post.stopped', globalClock.getTime());
          if (routineForceEnded) {
              routineTimer.reset();} else if (baseline_postMaxDurationReached) {
              baseline_postClock.add(baseline_postMaxDuration);
          } else {
              baseline_postClock.add(1.500000);
          }
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      
var baseline_itiMaxDurationReached;
var baseline_itiMaxDuration;
var baseline_itiComponents;
function baseline_itiRoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'baseline_iti' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          baseline_itiClock.reset(routineTimer.getTime());
          routineTimer.add(0.500000);
          baseline_itiMaxDurationReached = false;
          // update component parameters for each repeat
          psychoJS.experiment.addData('baseline_iti.started', globalClock.getTime());
          baseline_itiMaxDuration = null
          // keep track of which components have finished
          baseline_itiComponents = [];
          baseline_itiComponents.push(baseline_iti_fix);
          
          for (const thisComponent of baseline_itiComponents)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      
function baseline_itiRoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'baseline_iti' ---
          // get current time
          t = baseline_itiClock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          
          // *baseline_iti_fix* updates
          if (t >= 0 && baseline_iti_fix.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            baseline_iti_fix.tStart = t;  // (not accounting for frame time here)
            baseline_iti_fix.frameNStart = frameN;  // exact frame index
            
            baseline_iti_fix.setAutoDraw(true);
          }
          
          
          // if baseline_iti_fix is active this frame...
          if (baseline_iti_fix.status === PsychoJS.Status.STARTED) {
          }
          
          frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (baseline_iti_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            baseline_iti_fix.tStop = t;  // not accounting for scr refresh
            baseline_iti_fix.frameNStop = frameN;  // exact frame index
            // update status
            baseline_iti_fix.status = PsychoJS.Status.FINISHED;
            baseline_iti_fix.setAutoDraw(false);
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of baseline_itiComponents)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine && routineTimer.getTime() > 0) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      
function baseline_itiRoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'baseline_iti' ---
          for (const thisComponent of baseline_itiComponents) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('baseline_iti.stopped', globalClock.getTime());
          if (routineForceEnded) {
              routineTimer.reset();} else if (baseline_itiMaxDurationReached) {
              baseline_itiClock.add(baseline_itiMaxDuration);
          } else {
              baseline_itiClock.add(0.500000);
          }
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      
var main_introMaxDurationReached;
var _main_intro_key_allKeys;
var main_introMaxDuration;
var main_introComponents;
function main_introRoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'main_intro' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          main_introClock.reset();
          routineTimer.reset();
          main_introMaxDurationReached = false;
          // update component parameters for each repeat
          main_intro_key.keys = undefined;
          main_intro_key.rt = undefined;
          _main_intro_key_allKeys = [];
          psychoJS.experiment.addData('main_intro.started', globalClock.getTime());
          main_introMaxDuration = null
          // keep track of which components have finished
          main_introComponents = [];
          main_introComponents.push(main_intro_text);
          main_introComponents.push(main_intro_key);
          
          for (const thisComponent of main_introComponents)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      
function main_introRoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'main_intro' ---
          // get current time
          t = main_introClock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          
          // *main_intro_text* updates
          if (t >= 0 && main_intro_text.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            main_intro_text.tStart = t;  // (not accounting for frame time here)
            main_intro_text.frameNStart = frameN;  // exact frame index
            
            main_intro_text.setAutoDraw(true);
          }
          
          
          // if main_intro_text is active this frame...
          if (main_intro_text.status === PsychoJS.Status.STARTED) {
          }
          
          
          // *main_intro_key* updates
          if (t >= 0 && main_intro_key.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            main_intro_key.tStart = t;  // (not accounting for frame time here)
            main_intro_key.frameNStart = frameN;  // exact frame index
            
            // keyboard checking is just starting
            psychoJS.window.callOnFlip(function() { main_intro_key.clock.reset(); });  // t=0 on next screen flip
            psychoJS.window.callOnFlip(function() { main_intro_key.start(); }); // start on screen flip
            psychoJS.window.callOnFlip(function() { main_intro_key.clearEvents(); });
          }
          
          // if main_intro_key is active this frame...
          if (main_intro_key.status === PsychoJS.Status.STARTED) {
            let theseKeys = main_intro_key.getKeys({
              keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
              waitRelease: false
            });
            _main_intro_key_allKeys = _main_intro_key_allKeys.concat(theseKeys);
            if (_main_intro_key_allKeys.length > 0) {
              main_intro_key.keys = _main_intro_key_allKeys[0].name;  // just the first key pressed
              main_intro_key.rt = _main_intro_key_allKeys[0].rt;
              main_intro_key.duration = _main_intro_key_allKeys[0].duration;
              // a response ends the routine
              continueRoutine = false;
            }
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of main_introComponents)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      
function main_introRoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'main_intro' ---
          for (const thisComponent of main_introComponents) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('main_intro.stopped', globalClock.getTime());
          // update the trial handler
          if (currentLoop instanceof MultiStairHandler) {
            currentLoop.addResponse(main_intro_key.corr, level);
          }
          psychoJS.experiment.addData('main_intro_key.keys', main_intro_key.keys);
          if (typeof main_intro_key.keys !== 'undefined') {  // we had a response
              psychoJS.experiment.addData('main_intro_key.rt', main_intro_key.rt);
              psychoJS.experiment.addData('main_intro_key.duration', main_intro_key.duration);
              routineTimer.reset();
              }
          
          main_intro_key.stop();
          // the Routine "main_intro" was not non-slip safe, so reset the non-slip timer
          routineTimer.reset();
          
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      
var block_introMaxDurationReached;
var blockText;
var _block_intro_key_allKeys;
var block_introMaxDuration;
var block_introComponents;
function block_introRoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'block_intro' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          block_introClock.reset();
          routineTimer.reset();
          block_introMaxDurationReached = false;
          // update component parameters for each repeat
          // Run 'Begin Routine' code from block_intro_code
          blockText = 'Block ' + String(mainBlocks.thisN + 1) + ' of 4\n\nPress SPACE when you are ready.';
          
          block_intro_text.setText(blockText);
          block_intro_key.keys = undefined;
          block_intro_key.rt = undefined;
          _block_intro_key_allKeys = [];
          psychoJS.experiment.addData('block_intro.started', globalClock.getTime());
          block_introMaxDuration = null
          // keep track of which components have finished
          block_introComponents = [];
          block_introComponents.push(block_intro_text);
          block_introComponents.push(block_intro_key);
          
          for (const thisComponent of block_introComponents)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      
function block_introRoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'block_intro' ---
          // get current time
          t = block_introClock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          
          // *block_intro_text* updates
          if (t >= 0 && block_intro_text.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            block_intro_text.tStart = t;  // (not accounting for frame time here)
            block_intro_text.frameNStart = frameN;  // exact frame index
            
            block_intro_text.setAutoDraw(true);
          }
          
          
          // if block_intro_text is active this frame...
          if (block_intro_text.status === PsychoJS.Status.STARTED) {
          }
          
          
          // *block_intro_key* updates
          if (t >= 0 && block_intro_key.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            block_intro_key.tStart = t;  // (not accounting for frame time here)
            block_intro_key.frameNStart = frameN;  // exact frame index
            
            // keyboard checking is just starting
            psychoJS.window.callOnFlip(function() { block_intro_key.clock.reset(); });  // t=0 on next screen flip
            psychoJS.window.callOnFlip(function() { block_intro_key.start(); }); // start on screen flip
            psychoJS.window.callOnFlip(function() { block_intro_key.clearEvents(); });
          }
          
          // if block_intro_key is active this frame...
          if (block_intro_key.status === PsychoJS.Status.STARTED) {
            let theseKeys = block_intro_key.getKeys({
              keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
              waitRelease: false
            });
            _block_intro_key_allKeys = _block_intro_key_allKeys.concat(theseKeys);
            if (_block_intro_key_allKeys.length > 0) {
              block_intro_key.keys = _block_intro_key_allKeys[0].name;  // just the first key pressed
              block_intro_key.rt = _block_intro_key_allKeys[0].rt;
              block_intro_key.duration = _block_intro_key_allKeys[0].duration;
              // a response ends the routine
              continueRoutine = false;
            }
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of block_introComponents)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      
function block_introRoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'block_intro' ---
          for (const thisComponent of block_introComponents) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('block_intro.stopped', globalClock.getTime());
          // update the trial handler
          if (currentLoop instanceof MultiStairHandler) {
            currentLoop.addResponse(block_intro_key.corr, level);
          }
          psychoJS.experiment.addData('block_intro_key.keys', block_intro_key.keys);
          if (typeof block_intro_key.keys !== 'undefined') {  // we had a response
              psychoJS.experiment.addData('block_intro_key.rt', block_intro_key.rt);
              psychoJS.experiment.addData('block_intro_key.duration', block_intro_key.duration);
              routineTimer.reset();
              }
          
          block_intro_key.stop();
          // the Routine "block_intro" was not non-slip safe, so reset the non-slip timer
          routineTimer.reset();
          
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      
var main_fixationMaxDurationReached;
var main_fixationMaxDuration;
var main_fixationComponents;
function main_fixationRoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'main_fixation' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          main_fixationClock.reset(routineTimer.getTime());
          routineTimer.add(0.500000);
          main_fixationMaxDurationReached = false;
          // update component parameters for each repeat
          psychoJS.experiment.addData('main_fixation.started', globalClock.getTime());
          main_fixationMaxDuration = null
          // keep track of which components have finished
          main_fixationComponents = [];
          main_fixationComponents.push(main_fixation_fix);
          
          for (const thisComponent of main_fixationComponents)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      
function main_fixationRoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'main_fixation' ---
          // get current time
          t = main_fixationClock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          
          // *main_fixation_fix* updates
          if (t >= 0 && main_fixation_fix.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            main_fixation_fix.tStart = t;  // (not accounting for frame time here)
            main_fixation_fix.frameNStart = frameN;  // exact frame index
            
            main_fixation_fix.setAutoDraw(true);
          }
          
          
          // if main_fixation_fix is active this frame...
          if (main_fixation_fix.status === PsychoJS.Status.STARTED) {
          }
          
          frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (main_fixation_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            main_fixation_fix.tStop = t;  // not accounting for scr refresh
            main_fixation_fix.frameNStop = frameN;  // exact frame index
            // update status
            main_fixation_fix.status = PsychoJS.Status.FINISHED;
            main_fixation_fix.setAutoDraw(false);
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of main_fixationComponents)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine && routineTimer.getTime() > 0) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      
function main_fixationRoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'main_fixation' ---
          for (const thisComponent of main_fixationComponents) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('main_fixation.stopped', globalClock.getTime());
          if (routineForceEnded) {
              routineTimer.reset();} else if (main_fixationMaxDurationReached) {
              main_fixationClock.add(main_fixationMaxDuration);
          } else {
              main_fixationClock.add(0.500000);
          }
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      
var main_decisionMaxDurationReached;
var trialIndex;
var probeThisTrial;
var _main_resp_allKeys;
var main_decisionMaxDuration;
var main_decisionComponents;
function main_decisionRoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'main_decision' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          main_decisionClock.reset(routineTimer.getTime());
          routineTimer.add(1.500000);
          main_decisionMaxDurationReached = false;
          // update component parameters for each repeat
          // Run 'Begin Routine' code from main_setup
          trialIndex = globalTrialN;
          
          if (probeCondition === 'full_probe') {
              probeThisTrial = 1;
          } else if (probeCondition === 'sparse_probe') {
              probeThisTrial = Number(probeSchedule[trialIndex]);
          } else {
              probeThisTrial = 0;
          }
          
          main_gabor.setOri(tiltSign * tiltDeg);
          main_resp.keys = undefined;
          main_resp.rt = undefined;
          _main_resp_allKeys = [];
          psychoJS.experiment.addData('main_decision.started', globalClock.getTime());
          main_decisionMaxDuration = null
          // keep track of which components have finished
          main_decisionComponents = [];
          main_decisionComponents.push(main_gabor);
          main_decisionComponents.push(main_wait_fix);
          main_decisionComponents.push(main_resp);
          
          for (const thisComponent of main_decisionComponents)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      
function main_decisionRoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'main_decision' ---
          // get current time
          t = main_decisionClock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          
          // *main_gabor* updates
          if (t >= 0 && main_gabor.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            main_gabor.tStart = t;  // (not accounting for frame time here)
            main_gabor.frameNStart = frameN;  // exact frame index
            
            main_gabor.setAutoDraw(true);
          }
          
          
          // if main_gabor is active this frame...
          if (main_gabor.status === PsychoJS.Status.STARTED) {
          }
          
          frameRemains = 0 + 0.15 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (main_gabor.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            main_gabor.tStop = t;  // not accounting for scr refresh
            main_gabor.frameNStop = frameN;  // exact frame index
            // update status
            main_gabor.status = PsychoJS.Status.FINISHED;
            main_gabor.setAutoDraw(false);
          }
          
          
          // *main_wait_fix* updates
          if (((main_gabor.status == FINISHED)) && main_wait_fix.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            main_wait_fix.tStart = t;  // (not accounting for frame time here)
            main_wait_fix.frameNStart = frameN;  // exact frame index
            
            main_wait_fix.setAutoDraw(true);
          }
          
          
          // if main_wait_fix is active this frame...
          if (main_wait_fix.status === PsychoJS.Status.STARTED) {
          }
          
          frameRemains = 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if ((main_wait_fix.status === PsychoJS.Status.STARTED || main_wait_fix.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
            // keep track of stop time/frame for later
            main_wait_fix.tStop = t;  // not accounting for scr refresh
            main_wait_fix.frameNStop = frameN;  // exact frame index
            // update status
            main_wait_fix.status = PsychoJS.Status.FINISHED;
            main_wait_fix.setAutoDraw(false);
          }
          
          
          // *main_resp* updates
          if (t >= 0 && main_resp.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            main_resp.tStart = t;  // (not accounting for frame time here)
            main_resp.frameNStart = frameN;  // exact frame index
            
            // keyboard checking is just starting
            psychoJS.window.callOnFlip(function() { main_resp.clock.reset(); });  // t=0 on next screen flip
            psychoJS.window.callOnFlip(function() { main_resp.start(); }); // start on screen flip
            psychoJS.window.callOnFlip(function() { main_resp.clearEvents(); });
          }
          frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (main_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            main_resp.tStop = t;  // not accounting for scr refresh
            main_resp.frameNStop = frameN;  // exact frame index
            // update status
            main_resp.status = PsychoJS.Status.FINISHED;
            frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
            if (main_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
              // keep track of stop time/frame for later
              main_resp.tStop = t;  // not accounting for scr refresh
              main_resp.frameNStop = frameN;  // exact frame index
              // update status
              main_resp.status = PsychoJS.Status.FINISHED;
              main_resp.status = PsychoJS.Status.FINISHED;
                }
              
            }
            
            // if main_resp is active this frame...
            if (main_resp.status === PsychoJS.Status.STARTED) {
              let theseKeys = main_resp.getKeys({
                keyList: typeof [['f','j']] === 'string' ? [[['f','j']]] : [['f','j']], 
                waitRelease: false
              });
              _main_resp_allKeys = _main_resp_allKeys.concat(theseKeys);
              if (_main_resp_allKeys.length > 0) {
                main_resp.keys = _main_resp_allKeys[0].name;  // just the first key pressed
                main_resp.rt = _main_resp_allKeys[0].rt;
                main_resp.duration = _main_resp_allKeys[0].duration;
                // was this correct?
                if (main_resp.keys == corrAns) {
                    main_resp.corr = 1;
                } else {
                    main_resp.corr = 0;
                }
              }
            }
            
            // Run 'Each Frame' code from main_minexposure
            if (main_resp.keys !== undefined && main_resp.keys !== null && main_resp.keys.length > 0 && t >= 0.15) {
                continueRoutine = false;
            }
            
            // check for quit (typically the Esc key)
            if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
              return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
            }
            
            // check if the Routine should terminate
            if (!continueRoutine) {  // a component has requested a forced-end of Routine
              routineForceEnded = true;
              return Scheduler.Event.NEXT;
            }
            
            continueRoutine = false;  // reverts to True if at least one component still running
            for (const thisComponent of main_decisionComponents)
              if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                continueRoutine = true;
                break;
              }
            
            // refresh the screen if continuing
            if (continueRoutine && routineTimer.getTime() > 0) {
              return Scheduler.Event.FLIP_REPEAT;
            } else {
              return Scheduler.Event.NEXT;
            }
          };
        }
        
        
var choiceMade;
function main_decisionRoutineEnd(snapshot) {
          return async function () {
            //--- Ending Routine 'main_decision' ---
            for (const thisComponent of main_decisionComponents) {
              if (typeof thisComponent.setAutoDraw === 'function') {
                thisComponent.setAutoDraw(false);
              }
            }
            psychoJS.experiment.addData('main_decision.stopped', globalClock.getTime());
            // was no response the correct answer?!
            if (main_resp.keys === undefined) {
              if (['None','none',undefined].includes(corrAns)) {
                 main_resp.corr = 1;  // correct non-response
              } else {
                 main_resp.corr = 0;  // failed to respond (incorrectly)
              }
            }
            // store data for current loop
            // update the trial handler
            if (currentLoop instanceof MultiStairHandler) {
              currentLoop.addResponse(main_resp.corr, level);
            }
            psychoJS.experiment.addData('main_resp.keys', main_resp.keys);
            psychoJS.experiment.addData('main_resp.corr', main_resp.corr);
            if (typeof main_resp.keys !== 'undefined') {  // we had a response
                psychoJS.experiment.addData('main_resp.rt', main_resp.rt);
                psychoJS.experiment.addData('main_resp.duration', main_resp.duration);
                }
            
            main_resp.stop();
            // Run 'End Routine' code from main_end
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
            
            globalTrialN += 1;
            
            if (routineForceEnded) {
                routineTimer.reset();} else if (main_decisionMaxDurationReached) {
                main_decisionClock.add(main_decisionMaxDuration);
            } else {
                main_decisionClock.add(1.500000);
            }
            // Routines running outside a loop should always advance the datafile row
            if (currentLoop === psychoJS.experiment) {
              psychoJS.experiment.nextEntry(snapshot);
            }
            return Scheduler.Event.NEXT;
          }
        }
        
        
var main_postMaxDurationReached;
var _confidence_resp_allKeys;
var main_postMaxDuration;
var main_postComponents;
function main_postRoutineBegin(snapshot) {
          return async function () {
            TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
            
            //--- Prepare to start Routine 'main_post' ---
            t = 0;
            frameN = -1;
            continueRoutine = true; // until we're told otherwise
            // keep track of whether this Routine was forcibly ended
            routineForceEnded = false;
            main_postClock.reset();
            routineTimer.reset();
            main_postMaxDurationReached = false;
            // update component parameters for each repeat
            confidence_resp.keys = undefined;
            confidence_resp.rt = undefined;
            _confidence_resp_allKeys = [];
            psychoJS.experiment.addData('main_post.started', globalClock.getTime());
            main_postMaxDuration = 1.5
            // keep track of which components have finished
            main_postComponents = [];
            main_postComponents.push(post_fix);
            main_postComponents.push(confidence_prompt);
            main_postComponents.push(confidence_resp);
            
            for (const thisComponent of main_postComponents)
              if ('status' in thisComponent)
                thisComponent.status = PsychoJS.Status.NOT_STARTED;
            return Scheduler.Event.NEXT;
          }
        }
        
        
function main_postRoutineEachFrame() {
          return async function () {
            //--- Loop for each frame of Routine 'main_post' ---
            // get current time
            t = main_postClock.getTime();
            frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
            // update/draw components on each frame
            // is it time to end the Routine? (based on local clock)
            if (t > main_postMaxDuration) {
                main_postMaxDurationReached = true
                continueRoutine = false
            }
            
            // *post_fix* updates
            if (((probeThisTrial == 0)) && post_fix.status === PsychoJS.Status.NOT_STARTED) {
              // keep track of start time/frame for later
              post_fix.tStart = t;  // (not accounting for frame time here)
              post_fix.frameNStart = frameN;  // exact frame index
              
              post_fix.setAutoDraw(true);
            }
            
            
            // if post_fix is active this frame...
            if (post_fix.status === PsychoJS.Status.STARTED) {
            }
            
            if (post_fix.status === PsychoJS.Status.STARTED && t >= (post_fix.tStart + 1.5)) {
              // keep track of stop time/frame for later
              post_fix.tStop = t;  // not accounting for scr refresh
              post_fix.frameNStop = frameN;  // exact frame index
              // update status
              post_fix.status = PsychoJS.Status.FINISHED;
              post_fix.setAutoDraw(false);
            }
            
            
            // *confidence_prompt* updates
            if (((probeThisTrial == 1)) && confidence_prompt.status === PsychoJS.Status.NOT_STARTED) {
              // keep track of start time/frame for later
              confidence_prompt.tStart = t;  // (not accounting for frame time here)
              confidence_prompt.frameNStart = frameN;  // exact frame index
              
              confidence_prompt.setAutoDraw(true);
            }
            
            
            // if confidence_prompt is active this frame...
            if (confidence_prompt.status === PsychoJS.Status.STARTED) {
            }
            
            if (confidence_prompt.status === PsychoJS.Status.STARTED && t >= (confidence_prompt.tStart + 1.5)) {
              // keep track of stop time/frame for later
              confidence_prompt.tStop = t;  // not accounting for scr refresh
              confidence_prompt.frameNStop = frameN;  // exact frame index
              // update status
              confidence_prompt.status = PsychoJS.Status.FINISHED;
              confidence_prompt.setAutoDraw(false);
            }
            
            
            // *confidence_resp* updates
            if (((probeThisTrial == 1)) && confidence_resp.status === PsychoJS.Status.NOT_STARTED) {
              // keep track of start time/frame for later
              confidence_resp.tStart = t;  // (not accounting for frame time here)
              confidence_resp.frameNStart = frameN;  // exact frame index
              
              // keyboard checking is just starting
              psychoJS.window.callOnFlip(function() { confidence_resp.clock.reset(); });  // t=0 on next screen flip
              psychoJS.window.callOnFlip(function() { confidence_resp.start(); }); // start on screen flip
              psychoJS.window.callOnFlip(function() { confidence_resp.clearEvents(); });
            }
            if (confidence_resp.status === PsychoJS.Status.STARTED && t >= (confidence_resp.tStart + 1.5)) {
              // keep track of stop time/frame for later
              confidence_resp.tStop = t;  // not accounting for scr refresh
              confidence_resp.frameNStop = frameN;  // exact frame index
              // update status
              confidence_resp.status = PsychoJS.Status.FINISHED;
              if (confidence_resp.status === PsychoJS.Status.STARTED && t >= (confidence_resp.tStart + 1.5)) {
                // keep track of stop time/frame for later
                confidence_resp.tStop = t;  // not accounting for scr refresh
                confidence_resp.frameNStop = frameN;  // exact frame index
                // update status
                confidence_resp.status = PsychoJS.Status.FINISHED;
                confidence_resp.status = PsychoJS.Status.FINISHED;
                  }
                
              }
              
              // if confidence_resp is active this frame...
              if (confidence_resp.status === PsychoJS.Status.STARTED) {
                let theseKeys = confidence_resp.getKeys({
                  keyList: typeof [['1','2','3','4','5','6']] === 'string' ? [[['1','2','3','4','5','6']]] : [['1','2','3','4','5','6']], 
                  waitRelease: false
                });
                _confidence_resp_allKeys = _confidence_resp_allKeys.concat(theseKeys);
                if (_confidence_resp_allKeys.length > 0) {
                  confidence_resp.keys = _confidence_resp_allKeys[0].name;  // just the first key pressed
                  confidence_resp.rt = _confidence_resp_allKeys[0].rt;
                  confidence_resp.duration = _confidence_resp_allKeys[0].duration;
                }
              }
              
              // check for quit (typically the Esc key)
              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
              }
              
              // check if the Routine should terminate
              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                routineForceEnded = true;
                return Scheduler.Event.NEXT;
              }
              
              continueRoutine = false;  // reverts to True if at least one component still running
              for (const thisComponent of main_postComponents)
                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                  continueRoutine = true;
                  break;
                }
              
              // refresh the screen if continuing
              if (continueRoutine) {
                return Scheduler.Event.FLIP_REPEAT;
              } else {
                return Scheduler.Event.NEXT;
              }
            };
          }
          
          
var confidenceMade;
function main_postRoutineEnd(snapshot) {
            return async function () {
              //--- Ending Routine 'main_post' ---
              for (const thisComponent of main_postComponents) {
                if (typeof thisComponent.setAutoDraw === 'function') {
                  thisComponent.setAutoDraw(false);
                }
              }
              psychoJS.experiment.addData('main_post.stopped', globalClock.getTime());
              // update the trial handler
              if (currentLoop instanceof MultiStairHandler) {
                currentLoop.addResponse(confidence_resp.corr, level);
              }
              psychoJS.experiment.addData('confidence_resp.keys', confidence_resp.keys);
              if (typeof confidence_resp.keys !== 'undefined') {  // we had a response
                  psychoJS.experiment.addData('confidence_resp.rt', confidence_resp.rt);
                  psychoJS.experiment.addData('confidence_resp.duration', confidence_resp.duration);
                  }
              
              confidence_resp.stop();
              // Run 'End Routine' code from post_end
              confidenceMade = (
                  probeThisTrial === 1 &&
                  confidence_resp.keys !== undefined &&
                  confidence_resp.keys !== null &&
                  confidence_resp.keys.length > 0
              ) ? 1 : 0;
              psychoJS.experiment.addData('confidenceRequested', probeThisTrial);
              psychoJS.experiment.addData('confidenceMade', confidenceMade);
              
              // the Routine "main_post" was not non-slip safe, so reset the non-slip timer
              routineTimer.reset();
              
              // Routines running outside a loop should always advance the datafile row
              if (currentLoop === psychoJS.experiment) {
                psychoJS.experiment.nextEntry(snapshot);
              }
              return Scheduler.Event.NEXT;
            }
          }
          
          
var main_itiMaxDurationReached;
var main_itiMaxDuration;
var main_itiComponents;
function main_itiRoutineBegin(snapshot) {
            return async function () {
              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
              
              //--- Prepare to start Routine 'main_iti' ---
              t = 0;
              frameN = -1;
              continueRoutine = true; // until we're told otherwise
              // keep track of whether this Routine was forcibly ended
              routineForceEnded = false;
              main_itiClock.reset(routineTimer.getTime());
              routineTimer.add(0.500000);
              main_itiMaxDurationReached = false;
              // update component parameters for each repeat
              psychoJS.experiment.addData('main_iti.started', globalClock.getTime());
              main_itiMaxDuration = null
              // keep track of which components have finished
              main_itiComponents = [];
              main_itiComponents.push(main_iti_fix);
              
              for (const thisComponent of main_itiComponents)
                if ('status' in thisComponent)
                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
              return Scheduler.Event.NEXT;
            }
          }
          
          
function main_itiRoutineEachFrame() {
            return async function () {
              //--- Loop for each frame of Routine 'main_iti' ---
              // get current time
              t = main_itiClock.getTime();
              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
              // update/draw components on each frame
              
              // *main_iti_fix* updates
              if (t >= 0 && main_iti_fix.status === PsychoJS.Status.NOT_STARTED) {
                // keep track of start time/frame for later
                main_iti_fix.tStart = t;  // (not accounting for frame time here)
                main_iti_fix.frameNStart = frameN;  // exact frame index
                
                main_iti_fix.setAutoDraw(true);
              }
              
              
              // if main_iti_fix is active this frame...
              if (main_iti_fix.status === PsychoJS.Status.STARTED) {
              }
              
              frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
              if (main_iti_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                // keep track of stop time/frame for later
                main_iti_fix.tStop = t;  // not accounting for scr refresh
                main_iti_fix.frameNStop = frameN;  // exact frame index
                // update status
                main_iti_fix.status = PsychoJS.Status.FINISHED;
                main_iti_fix.setAutoDraw(false);
              }
              
              // check for quit (typically the Esc key)
              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
              }
              
              // check if the Routine should terminate
              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                routineForceEnded = true;
                return Scheduler.Event.NEXT;
              }
              
              continueRoutine = false;  // reverts to True if at least one component still running
              for (const thisComponent of main_itiComponents)
                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                  continueRoutine = true;
                  break;
                }
              
              // refresh the screen if continuing
              if (continueRoutine && routineTimer.getTime() > 0) {
                return Scheduler.Event.FLIP_REPEAT;
              } else {
                return Scheduler.Event.NEXT;
              }
            };
          }
          
          
function main_itiRoutineEnd(snapshot) {
            return async function () {
              //--- Ending Routine 'main_iti' ---
              for (const thisComponent of main_itiComponents) {
                if (typeof thisComponent.setAutoDraw === 'function') {
                  thisComponent.setAutoDraw(false);
                }
              }
              psychoJS.experiment.addData('main_iti.stopped', globalClock.getTime());
              if (routineForceEnded) {
                  routineTimer.reset();} else if (main_itiMaxDurationReached) {
                  main_itiClock.add(main_itiMaxDuration);
              } else {
                  main_itiClock.add(0.500000);
              }
              // Routines running outside a loop should always advance the datafile row
              if (currentLoop === psychoJS.experiment) {
                psychoJS.experiment.nextEntry(snapshot);
              }
              return Scheduler.Event.NEXT;
            }
          }
          
          
var block_breakMaxDurationReached;
var breakText;
var _block_break_key_allKeys;
var block_breakMaxDuration;
var block_breakComponents;
function block_breakRoutineBegin(snapshot) {
            return async function () {
              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
              
              //--- Prepare to start Routine 'block_break' ---
              t = 0;
              frameN = -1;
              continueRoutine = true; // until we're told otherwise
              // keep track of whether this Routine was forcibly ended
              routineForceEnded = false;
              block_breakClock.reset();
              routineTimer.reset();
              block_breakMaxDurationReached = false;
              // update component parameters for each repeat
              // Run 'Begin Routine' code from block_break_code
              let blockNumber = mainBlocks.thisN + 1;
              if (blockNumber < 4) {
                  breakText = 'End of block ' + String(blockNumber) +
                      ' of 4.\n\nTake a short break. Press SPACE to continue.';
              } else {
                  breakText = 'The main task is complete. Press SPACE to continue.';
              }
              
              block_break_text.setText(breakText);
              block_break_key.keys = undefined;
              block_break_key.rt = undefined;
              _block_break_key_allKeys = [];
              psychoJS.experiment.addData('block_break.started', globalClock.getTime());
              block_breakMaxDuration = null
              // keep track of which components have finished
              block_breakComponents = [];
              block_breakComponents.push(block_break_text);
              block_breakComponents.push(block_break_key);
              
              for (const thisComponent of block_breakComponents)
                if ('status' in thisComponent)
                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
              return Scheduler.Event.NEXT;
            }
          }
          
          
function block_breakRoutineEachFrame() {
            return async function () {
              //--- Loop for each frame of Routine 'block_break' ---
              // get current time
              t = block_breakClock.getTime();
              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
              // update/draw components on each frame
              
              // *block_break_text* updates
              if (t >= 0 && block_break_text.status === PsychoJS.Status.NOT_STARTED) {
                // keep track of start time/frame for later
                block_break_text.tStart = t;  // (not accounting for frame time here)
                block_break_text.frameNStart = frameN;  // exact frame index
                
                block_break_text.setAutoDraw(true);
              }
              
              
              // if block_break_text is active this frame...
              if (block_break_text.status === PsychoJS.Status.STARTED) {
              }
              
              
              // *block_break_key* updates
              if (t >= 0 && block_break_key.status === PsychoJS.Status.NOT_STARTED) {
                // keep track of start time/frame for later
                block_break_key.tStart = t;  // (not accounting for frame time here)
                block_break_key.frameNStart = frameN;  // exact frame index
                
                // keyboard checking is just starting
                psychoJS.window.callOnFlip(function() { block_break_key.clock.reset(); });  // t=0 on next screen flip
                psychoJS.window.callOnFlip(function() { block_break_key.start(); }); // start on screen flip
                psychoJS.window.callOnFlip(function() { block_break_key.clearEvents(); });
              }
              
              // if block_break_key is active this frame...
              if (block_break_key.status === PsychoJS.Status.STARTED) {
                let theseKeys = block_break_key.getKeys({
                  keyList: typeof ['space'] === 'string' ? [['space']] : ['space'], 
                  waitRelease: false
                });
                _block_break_key_allKeys = _block_break_key_allKeys.concat(theseKeys);
                if (_block_break_key_allKeys.length > 0) {
                  block_break_key.keys = _block_break_key_allKeys[0].name;  // just the first key pressed
                  block_break_key.rt = _block_break_key_allKeys[0].rt;
                  block_break_key.duration = _block_break_key_allKeys[0].duration;
                  // a response ends the routine
                  continueRoutine = false;
                }
              }
              
              // check for quit (typically the Esc key)
              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
              }
              
              // check if the Routine should terminate
              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                routineForceEnded = true;
                return Scheduler.Event.NEXT;
              }
              
              continueRoutine = false;  // reverts to True if at least one component still running
              for (const thisComponent of block_breakComponents)
                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                  continueRoutine = true;
                  break;
                }
              
              // refresh the screen if continuing
              if (continueRoutine) {
                return Scheduler.Event.FLIP_REPEAT;
              } else {
                return Scheduler.Event.NEXT;
              }
            };
          }
          
          
function block_breakRoutineEnd(snapshot) {
            return async function () {
              //--- Ending Routine 'block_break' ---
              for (const thisComponent of block_breakComponents) {
                if (typeof thisComponent.setAutoDraw === 'function') {
                  thisComponent.setAutoDraw(false);
                }
              }
              psychoJS.experiment.addData('block_break.stopped', globalClock.getTime());
              // update the trial handler
              if (currentLoop instanceof MultiStairHandler) {
                currentLoop.addResponse(block_break_key.corr, level);
              }
              psychoJS.experiment.addData('block_break_key.keys', block_break_key.keys);
              if (typeof block_break_key.keys !== 'undefined') {  // we had a response
                  psychoJS.experiment.addData('block_break_key.rt', block_break_key.rt);
                  psychoJS.experiment.addData('block_break_key.duration', block_break_key.duration);
                  routineTimer.reset();
                  }
              
              block_break_key.stop();
              // the Routine "block_break" was not non-slip safe, so reset the non-slip timer
              routineTimer.reset();
              
              // Routines running outside a loop should always advance the datafile row
              if (currentLoop === psychoJS.experiment) {
                psychoJS.experiment.nextEntry(snapshot);
              }
              return Scheduler.Event.NEXT;
            }
          }
          
          
var thanksMaxDurationReached;
var thanksMaxDuration;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
            return async function () {
              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
              
              //--- Prepare to start Routine 'thanks' ---
              t = 0;
              frameN = -1;
              continueRoutine = true; // until we're told otherwise
              // keep track of whether this Routine was forcibly ended
              routineForceEnded = false;
              thanksClock.reset(routineTimer.getTime());
              routineTimer.add(3.000000);
              thanksMaxDurationReached = false;
              // update component parameters for each repeat
              psychoJS.experiment.addData('thanks.started', globalClock.getTime());
              thanksMaxDuration = 3
              // keep track of which components have finished
              thanksComponents = [];
              thanksComponents.push(thanks_text);
              
              for (const thisComponent of thanksComponents)
                if ('status' in thisComponent)
                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
              return Scheduler.Event.NEXT;
            }
          }
          
          
function thanksRoutineEachFrame() {
            return async function () {
              //--- Loop for each frame of Routine 'thanks' ---
              // get current time
              t = thanksClock.getTime();
              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
              // update/draw components on each frame
              // is it time to end the Routine? (based on local clock)
              if (t > thanksMaxDuration) {
                  thanksMaxDurationReached = true
                  continueRoutine = false
              }
              
              // *thanks_text* updates
              if (t >= 0 && thanks_text.status === PsychoJS.Status.NOT_STARTED) {
                // keep track of start time/frame for later
                thanks_text.tStart = t;  // (not accounting for frame time here)
                thanks_text.frameNStart = frameN;  // exact frame index
                
                thanks_text.setAutoDraw(true);
              }
              
              
              // if thanks_text is active this frame...
              if (thanks_text.status === PsychoJS.Status.STARTED) {
              }
              
              frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
              if (thanks_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                // keep track of stop time/frame for later
                thanks_text.tStop = t;  // not accounting for scr refresh
                thanks_text.frameNStop = frameN;  // exact frame index
                // update status
                thanks_text.status = PsychoJS.Status.FINISHED;
                thanks_text.setAutoDraw(false);
              }
              
              // check for quit (typically the Esc key)
              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
              }
              
              // check if the Routine should terminate
              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                routineForceEnded = true;
                return Scheduler.Event.NEXT;
              }
              
              continueRoutine = false;  // reverts to True if at least one component still running
              for (const thisComponent of thanksComponents)
                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                  continueRoutine = true;
                  break;
                }
              
              // refresh the screen if continuing
              if (continueRoutine && routineTimer.getTime() > 0) {
                return Scheduler.Event.FLIP_REPEAT;
              } else {
                return Scheduler.Event.NEXT;
              }
            };
          }
          
          
function thanksRoutineEnd(snapshot) {
            return async function () {
              //--- Ending Routine 'thanks' ---
              for (const thisComponent of thanksComponents) {
                if (typeof thisComponent.setAutoDraw === 'function') {
                  thisComponent.setAutoDraw(false);
                }
              }
              psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
              if (routineForceEnded) {
                  routineTimer.reset();} else if (thanksMaxDurationReached) {
                  thanksClock.add(thanksMaxDuration);
              } else {
                  thanksClock.add(3.000000);
              }
              // Routines running outside a loop should always advance the datafile row
              if (currentLoop === psychoJS.experiment) {
                psychoJS.experiment.nextEntry(snapshot);
              }
              return Scheduler.Event.NEXT;
            }
          }
          
          
function importConditions(currentLoop) {
            return async function () {
              psychoJS.importAttributes(currentLoop.getCurrentTrial());
              return Scheduler.Event.NEXT;
              };
          }
          
          
async function quitPsychoJS(message, isCompleted) {
            // Check for and save orphaned data
            if (psychoJS.experiment.isEntryEmpty()) {
              psychoJS.experiment.nextEntry();
            }
            psychoJS.window.close();
            psychoJS.quit({message: message, isCompleted: isCompleted});
            
            return Scheduler.Event.QUIT;
          }
