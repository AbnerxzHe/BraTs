import pdb
import argparse

from data import *
from unet import *

def train(args):

    # Data Load
    trainset = trainGenerator(args)

    # Model Load
    model = unet(args)
    model_checkpoint = ModelCheckpoint(args.ckpt_path,
                                       monitor='loss',verbose=2,
                                       save_best_only=True)
    model.fit_generator(trainset, steps_per_epoch=200, shuffle=True,
                        epochs=args.epoch,callbacks=[model_checkpoint],
                        workers=16, use_multiprocessing=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--resume', type=bool, default=False,
                        help='Resume model checkpoint')
    parser.add_argument('--batch_size', type=int, default=20,
                        help='batch size.')
    parser.add_argument('--lr', type=float, default=0.0001,
                        help='starting learning_rate')
    parser.add_argument('--epoch', type=int, default=10,
                        help='number of epochs.')
    parser.add_argument('--data', type=str, default='complete',
                        help='MRI Label data to train')
    parser.add_argument('--train_root', type=str,
                        default='../data/train/keras',
                        help='the directory containing the train dataset.')
    parser.add_argument('--image_folder', type=str,
                        default='flair2',
                        help='the directory containing the trian image dataset.')
    parser.add_argument('--label_folder', type=str,
                        default='label2',
                        help='the directory containing the train label dataset.')
    parser.add_argument('--ckpt_path', type=str, default='./checkpoint/unet.hdf5',
                        help='The directory containing the generative image.')
    args = parser.parse_args()

    train(args)
