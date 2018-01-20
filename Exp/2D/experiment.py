from psychopy import visual #import some libraries from PsychoPy
import numpy as np

class Experiment(object):

    def __init__(self, win=None, trials_no=None, blocks_no=None, mode='motion-color'):

        # Welcoming/intro
        self.welcome_msg = visual.TextStim(win=win,
                                           text='Welcome to the experiment\nPlease press ENTER to proceed',
                                           pos=[0, 0], alignHoriz='center',
                                           color=(0, 0, 0))
        # Instructions
        if mode == 'motion-shape':
            self.instruct1_msg = visual.TextStim(win=win,
                                                 text='Attend to Shape',
                                                 pos=[0, 0], alignHoriz='center',
                                                 color=(0, 0, 0))
        elif mode == 'motion-color':
            self.instruct1_msg = visual.TextStim(win=win,
                                                 text='Attend to Color',
                                                 pos=[0, 0], alignHoriz='center',
                                                 color=(0, 0, 0))

        self.attended_feature = visual.TextStim(win=win,
                                                text='',
                                                pos=[0, 0], alignHoriz='center',
                                                color=(0, 0, 0))

        # Closing remark
        self.closing_msg = visual.TextStim(win=win,
                                           text='This is the end of experiment!',
                                           pos=[0, 0], alignHoriz='center',
                                           color=(0,0,0))

        # Task stimuli
        self.stim1 = visual.GratingStim(win=win, mask='gauss',
                                        size=3, pos=[-4, 0], sf=0)

        self.fixat = visual.TextStim(win=win,
                                     text='+',
                                     pos=[0, 0], alignHoriz='center',
                                     color=(0, 0, 0))

        self.imag_rec = visual.ShapeStim(win=win,
                                         vertices=((-5, 2), (-5, 5), (5, 5), (5, 2)),
                                         lineWidth=.5, pos=(0, 0),
                                         lineColor='black')

        self.triangle = visual.Polygon(win=win,
                                       radius=1.5, pos=(0, 3.5),
                                       fillColor='red', lineColor=None)

        self.square = visual.Rect(win=win,
                                  width=3, height=3, pos=(0, 3.5),
                                  fillColor='red', lineColor=None)

        self.circle = visual.Circle(win=win,
                                    radius=1.5, pos=(0, 3.5),
                                    fillColor='red', lineColor=None)

        self.trials_no = trials_no
        self.blocks_no = blocks_no
        self.total_no = trials_no * blocks_no
        self.mode = mode

        # markers
        if mode == 'motion-color':
            self.block_start = 1
            self.flash1_start_Notarget = 2
            self.flash1_start_standard = 3
            self.flash1_start_target = 4
            self.flash2_start = 5

        if mode == 'motion-shape':
            self.block_start = 6
            self.flash1_start_Notarget = 7
            self.flash1_start_standard = 8
            self.flash1_start_target = 9
            self.flash2_start = 10

        self.response_marker = 11

    def isTarget(self, feature1, feature2, color, shape, direction, stim_type):

        # print(feature1, feature2, color, shape, direction, stim_type)
        if self.mode == 'motion-color':
            if feature1 == color and feature2 == direction and stim_type == 9:
                return True

            else:
                return False

        if self.mode == 'motion-shape':
            if feature1 == shape and feature2 == direction and stim_type == 9:
                return True

            else:
                return False

    def isStandard(self, feature1, feature2, color, shape, direction, stim_type):

        # print(feature1, feature2, color, shape, direction, stim_type)
        if self.mode == 'motion-color':
            if feature1 == color and feature2 == direction and stim_type == 3:
                return True

            else:
                return False

        if self.mode == 'motion-shape':
            if feature1 == shape and feature2 == direction and stim_type == 3:
                return True

            else:
                return False

    def getRandAttendedFeature(self, color, shape, direction):
        selected_shape = np.random.choice(np.array(shape))
        selected_color = np.random.choice(np.array(color))
        selected_direction = np.random.choice(np.array(direction))

        if self.mode == 'motion-color':
            return selected_color, selected_direction

        if self.mode == 'motion-shape':
            return selected_shape, selected_direction


    def randomize2val(self, val1, val2):
        rnd = np.concatenate((np.ones(self.total_no//2)*val1, np.ones(self.total_no//2)*val2), axis=0)
        np.random.shuffle(rnd)
        np.random.shuffle(rnd)
        return rnd

    def randomize2str(self, str1, str2):
        rnd = np.concatenate((np.array([str1]).repeat(self.total_no//2), np.array([str2]).repeat(self.total_no//2)),
                             axis=0)
        np.random.shuffle(rnd)
        np.random.shuffle(rnd)
        return rnd

    def randomize2type(self, std_delay, std_prob, target_delay, target_prob):
        rnd = np.concatenate((np.ones(int(self.total_no * std_prob + .5)) * std_delay,
                              np.ones(int(self.total_no * target_prob + .5)) * target_delay),
                             axis=0)
        np.random.shuffle(rnd)
        np.random.shuffle(rnd)
        return rnd.astype(int)


    def getrand_obj(self, val):
        if val:
            return self.circle
        else:
            return self.square

    def getrand_pos(self):
        return np.random.rand()*8-4, 3.5  # this depends on the boundaries (x-axis) of the imaginary rectangle