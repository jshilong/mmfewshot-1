<div align="center">

  <img src="resources/mmfewshot-logo.png" width="500px"/>

</div>

## Introduction

English | [简体中文](README_zh-CN.md)

[![Documentation](https://readthedocs.org/projects/mmfewshot/badge/?version=latest)](https://mmfewshot.readthedocs.io/en/latest/?badge=latest)

[![actions](https://github.com/open-mmlab/mmfewshot/workflows/build/badge.svg)](https://github.com/open-mmlab/mmfewshot/actions)

[![codecov](https://codecov.io/gh/open-mmlab/mmfewshot/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmfewshot)

[![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/)

[![LICENSE](https://img.shields.io/github/license/open-mmlab/mmfewshot.svg)](https://github.com/open-mmlab/mmfewshot/blob/master/LICENSE)

[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/open-mmlab/mmfewshot.svg)](https://github.com/open-mmlab/mmfewshot/issues)

[![Percentage of issues still open](https://isitmaintained.com/badge/open/open-mmlab/mmfewshot.svg)](https://github.com/open-mmlab/mmfewshot/issues)


mmfewshot is an open source few shot learning toolbox based on PyTorch. It is a part of the [OpenMMLab](https://open-mmlab.github.io/) project.

The master branch works with **PyTorch 1.5+**.
The compatibility to earlier versions of PyTorch is not fully tested.

Documentation: https://mmfewshot.readthedocs.io/en/latest/.

<div align="left">
  <img src="resources/demo.png"/>
</div>

### Major features
- **Support multiple tasks in Few Shot Learning**

  MMFewShot provides unified implementation and evaluation of few shot classification and detection.

- **Modular Design**

  We decompose the few shot learning framework into different components,
  which makes it much easy and flexible to build a new model by combining different modules.

- **Strong baseline and State of the art**

  The toolbox provides strong baselines and state-of-the-art methods in few shot classification and detection.


## License

This project is released under the [Apache 2.0 license](LICENSE).


## Model Zoo

Supported algorithms:

<details open>
<summary>classification</summary>

- [x] [Baseline](configs/classification/baseline/README.md) (ICLR'2019)
- [x] [Baseline++](configs/classification/baseline_plus/README.md) (ICLR'2019)
- [x] [NegMargin](configs/classification/neg_margin/README.md) (ECCV'2020)
- [x] [MatchingNet](configs/classification/matching_net/README.md) (NeurIPS'2016)
- [x] [ProtoNet](configs/classification/proto_net/README.md) (NeurIPS'2017)
- [x] [RelationNet](configs/classification/relation_net/README.md) (CVPR'2018)
- [x] [MetaBaseline](configs/classification/meta_baseline/README.md) (ICCV'2021)
- [x] [MAML](configs/classification/maml/README.md) (ICML'2017)

</details>

<details open>
<summary>Detection</summary>

- [x] [TFA](configs/detection/tfa/README.md) (ICML'2020)
- [x] [FSCE](configs/detection/fsce/README.md) (CVPR'2021)
- [x] [AttentionRPN](configs/detection/attention_rpn/README.md) (CVPR'2020)
- [x] [MetaRCNN](configs/detection/meta_rcnn/README.md) (ICCV'2019)
- [x] [FSDetView](configs/detection/fsdetview/README.md) (ECCV'2020)
- [x] [MPSR](configs/detection/mpsr/README.md) (ECCV'2020)

</details>


## Changelog


## Installation

Please refer to [install.md](docs/install.md) for installation of mmfewshot.

## Getting Started

Please see [getting_started.md](docs/get_started.md) for the basic usage of mmfewshot.


## Citation

If you find this project useful in your research, please consider cite:

```bibtex
@misc{mmfewshot2021,
    title={OpenMMLab Few Shot Learning Toolbox and Benchmark},
    author={mmfewshot Contributors},
    howpublished = {\url{https://github.com/open-mmlab/mmfewshot}},
    year={2021}
}
```


## Contributing

We appreciate all contributions to improve mmfewshot. Please refer to [CONTRIBUTING.md in MMFewShot](https://github.com/open-mmlab/mmcv/blob/master/.github/CONTRIBUTING.md) for the contributing guideline.

## Acknowledgement

mmfewshot is an open source project that is contributed by researchers and engineers from various colleges and companies. We appreciate all the contributors who implement their methods or add new features, as well as users who give valuable feedbacks. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new methods.

## Projects in OpenMMLab

- [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
- [MIM](https://github.com/open-mmlab/mim): MIM Installs OpenMMLab Packages.
- [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
- [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
- [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
- [MMEditing](https://github.com/open-mmlab/mmfewshot): OpenMMLab image and video editing toolbox.
- [MMOCR](https://github.com/open-mmlab/mmocr): A Comprehensive Toolbox for Text Detection, Recognition and Understanding.
- [MMGeneration](https://github.com/open-mmlab/mmgeneration): A powerful toolkit for generative models.
