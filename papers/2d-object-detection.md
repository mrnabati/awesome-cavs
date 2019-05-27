# Awesome Connected and Automated Vehicles

## 2D Object Detection

### 2019

- **RRPN: Radar Region Proposal Network for Object Detection in Autonomous Vehicles** [ICIP 2019] [[Paper](https://arxiv.org/abs/1905.00526), [Code](https://github.com/mrnabati/RRPN)]
    > **Authors:** Ramin Nabati, Hairong Qi <br>
    > **Abstract:**   Region proposal algorithms play an important role in most state-of-the-art two-stage object detection networks by hypothesizing object locations in the image. Nonetheless, region proposal algorithms are known to be the bottleneck in most two-stage object detection networks, increasing the processing time for each image and resulting in slow networks not suitable for real-time applications such as autonomous driving vehicles. In this paper we introduce RRPN, a Radar-based real-time region proposal algorit...


- **Bottom-up Object Detection by Grouping Extreme and Center Points** [Arxiv] [[Paper](https://arxiv.org/abs/1901.08043v2), [Code](https://github.com/xingyizhou/ExtremeNet)]
    > **Authors:** Xingyi Zhou, Jiacheng Zhuo, Philipp Krähenbühl <br>
    > **Abstract:**   With the advent of deep learning, object detection drifted from a bottom-up to a top-down recognition problem. State of the art algorithms enumerate a near-exhaustive list of object locations and classify each into: object or not. In this paper, we show that bottom-up approaches still perform competitively. We detect four extreme points (top-most, left-most, bottom-most, right-most) and one center point of objects using a standard keypoint estimation network. We group the five keypoints into a bounding box if they are geometrically a...

- **RetinaMask: Learning to predict masks improves state-of-the-art single-shot detection for free** [Arxiv] [[Paper](https://arxiv.org/abs/1901.03353v1), [Code](https://github.com/chengyangfu/retinamask)]
    > **Authors:** Cheng-Yang Fu, Mykhailo Shvets, Alexander C. Berg <br>
    > **Abstract:**   Recently two-stage detectors have surged ahead of single-shot detectors in the accuracy-vs-speed trade-off. Nevertheless single-shot detectors are immensely popular in embedded vision applications. This paper brings single-shot detectors up to the same level as current two-stage techniques. We do this by improving training for the state-of-the-art single-shot detector, RetinaNet, in three ways: integrating instance mask prediction for the first time, making the loss function adaptive and more stable, and including additional hard exa...

### 2018

- **SNIPER: Efficient Multi-Scale Training** [NIPS 2018] [[Paper](https://arxiv.org/abs/1805.09300), [Code](https://github.com/mahyarnajibi/SNIPER)]
    > **Authors:** Bharat Singh, Mahyar Najibi, Larry S. Davis <br>
    > **Abstract:**   We present SNIPER, an algorithm for performing efficient multi-scale training in instance level visual recognition tasks. Instead of processing every pixel in an image pyramid, SNIPER processes context regions around ground-truth instances (referred to as chips) at the appropriate scale. For background sampling, these context-regions are generated using proposals extracted from a region proposal network trained with a short learning schedule. Hence, the number of chips generated per image during training adaptively changes based on t...
