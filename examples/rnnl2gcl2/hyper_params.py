################################################################################
# parameters defined by the user

# INPUT PATH
num_balls     = 1
project_path  = '/deep/u/kuanfang/optical-flow-pred/'
data_path     = project_path + 'data/bouncing_balls/'+ str(num_balls) + 'balls/' 
gc_path       = project_path + 'data/grammar_cells/' + str(num_balls) + 'balls/'

## DATA
image_suffix    = '.jpeg'   # suffix to load/store images
image_shape     = (16, 16)  # size of single channel images
numframes_train = 50000     # number of frames to train in each epoch
numframes_test  = 10000     # number of frames to validate in each epoch
seq_len         = 5         # number of frames in a sequence

## MODEL PARAMETERS 
hidden1_size = 100          # size of the hidden1 layer
hidden2_size = 50           # size of the hidden2 layer

# GRAMMAR CELL
numfac    = 80      # dimension of the feature factors
numvel    = 40      # dimension of the velocity units 
numvelfac = 40      # dimension of the velocity factors
numacc    = 20      # dimension of the acceleration units
numaccfac = 10      # dimension of the acceleration factors
numjerk   = 10      # dimension of the jerk units

## OPTIMIZATION PARAMETERS
lr = 1.e1             # learning rate
batch_size    = 1     # batch size in batched traning (useless for other cases)
save_epoch    = 100   # epoch number to save (written over) model and prediction
backup_epoch  = 1000  # epoch number to backup model and prediction

en_shuffle  = True    # enable shuffling of the training data

en_decay    = True    # enable learning rate decay
max_decay   = 20      # after contiunous max_decay viloations, the lr will decay
epsl_decay  = 1e-4    # threashold of decaying the learning rate

en_validate   = True  # enable validation phase
epsl_validate = 0.    # threshold of reloading the model

## OUTPUT PATH
models_path = 'models/'         # path to store the models
pred_path   = 'prediction/'     # path to store the predictions
vis_path    = 'visualization/'  # path to store the visualied results

## VISUALIZATION
max_plot  = 1000                # maximum number of time step to plot
th_of     = 0.1                 # threashold to draw optical flows


################################################################################
# parameters depend on above settings

## DATA
frame_dim = image_shape[0] * image_shape[1]   # data dimension of each frame
seq_dim = frame_dim * seq_len                 # data dimension of each sequence
numseqs_train = numframes_train / seq_len     # number of sequence to train
numseqs_test = numframes_test / seq_len       # number of sequence to validate
