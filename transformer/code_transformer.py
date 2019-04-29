from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.data_generators import translate
from tensor2tensor.data_generators import wiki_lm
from tensor2tensor.utils import registry

_CODE_TRAIN_DATASETS = [
    [
        "https://github.com/jverbraeken/Deep-Learning/blob/master/transformer_data/train.tgz?raw=true",
        ("train/train.cd",
        "train/train.en")
    ],
]
_CODE_EVAL_DATASETS = [
    [
        "https://github.com/jverbraeken/Deep-Learning/blob/master/transformer_data/valid.tgz?raw=true",
        ("valid/valid.cd",
        "valid/valid.en")
    ],
]

@registry.register_problem
class CodeTransformer(translate.TranslateProblem):
    """Translate from Java code to English"""

    # We should check if this value holds for our problem!
    @property
    def approx_vocab_size(self):
        return 2**13

    @property
    def additional_training_datasets(self):
        """Allow subclasses to add training datasets."""
        return []
    
    def source_data_files(self, dataset_split):
        train = dataset_split == problem.DatasetSplit == problem.DatasetSplit.TRAIN
        train_datasets = _CODE_TRAIN_DATASETS + self.additional_training_datasets
        return train_datasets if train else _CODE_EVAL_DATASETS
    