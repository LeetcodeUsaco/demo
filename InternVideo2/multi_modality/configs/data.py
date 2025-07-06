import os as __os  # add "__" if not want to be exported
from copy import deepcopy as __deepcopy

root_path = "/home/zli"

# ============== pretraining datasets=================
available_corpus = dict(
    # pretraining image datasets
    cc3m=dict(
        anno_path="your_path",
        data_root="",
        media_type="image"
    ),
    webvid_10m=dict(
        anno_path="your_path",
        data_root="",
        media_type="video",
    ),
    smol_test=dict(
        anno_path="/root/IV2/InternVideo2/multi_modality/data_test/smol_test.json",
        data_root="/root/IV2/InternVideo2/multi_modality/data_test/",
        media_type="video"
    ),
    slim_kinetics=dict(
        anno_path=f"{root_path}/test/kinetics-test.json",
        data_root=f"{root_path}/test",
        media_type="video",
        min_caption_length=1
    )
)

# ============== for validation =================

available_corpus["slim_kinetics_act_val"] = dict(
    anno_path=f"{root_path}/test/kinetics-test.json",
    data_root=f"{root_path}/test",
    media_type="video",
    is_act_rec=True,
)
