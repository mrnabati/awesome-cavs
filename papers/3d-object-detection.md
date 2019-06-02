# Awesome Connected and Automated Vehicles

## 3D Object Detection

### 2019
- **PointPillars: Fast Encoders for Object Detection from Point Clouds** [CVPR 2019] [[Paper](https://arxiv.org/pdf/1812.05784), [Code](https://github.com/nutonomy/second.pytorch)]
    > **Authors:** Alex H. Lang, Sourabh Vora, Holger Caesar, Lubing Zhou, Jiong Yang, Oscar Beijbom <br>
    > **Abstract:** Object detection in point clouds is an important aspect of many robotics applications such as autonomous driving. In this paper we consider the problem of encoding a point cloud into a format appropriate for a downstream detection pipeline. Recent literature suggests two types of encoders; fixed encoders tend to be fast but sacrifice accuracy, while encoders that are learned from data are more accurate, but slower. In this work we propose PointPillars, a novel encoder which utilizes PointNets to learn a representation of point clouds...

- **3D Backbone Network for 3D Object Detection** [Arxiv][[Paper](https://arxiv.org/pdf/1901.08373.pdf), [Code](https://github.com/Benzlxs/tDBN)]
    > **Authors:** Xuesong Li, Jose E Guivant, Ngaiming Kwok, Yongzhi Xu <br>
    > **Abstract:** The task of detecting 3D objects in point cloud has a pivotal role in many real-world applications. However,3D object detection performance is behind that of 2D object detection due to the lack of powerful 3D feature extraction methods. In order to address this issue, we propose to build a 3D backbone network to learn rich 3D feature maps by using sparse 3D CNN operations for 3D object detection in point cloud. The 3D backbone network can inherently learn 3D features from almost raw data without compressing point cloud...

- **Focal Loss in 3D Object Detection** [IEEE Robotics and Automation Letters 2019] [[Paper](https://arxiv.org/abs/1809.06065), [Code](https://sites.google.com/view/fl3d)]
    > **Authors:** Peng Yun, Lei Tai, Yuan Wang, Chengju Liu, Ming Liu <br>
    > **Abstract:**   3D object detection is still an open problem in autonomous driving scenes. When recognizing and localizing key objects from sparse 3D inputs, autonomous vehicles suffer from a larger continuous searching space and higher fore-background imbalance compared to image-based object detection. In this paper, we aim to solve this fore-background imbalance in 3D object detection. Inspired by the recent use of focal loss in image-based object detection, we extend this hard-mining improvement of binary cross entro...

- **Monocular 3D Object Detection with Pseudo-LiDAR Point Cloud** [Arxiv] [[Paper](https://arxiv.org/abs/1903.09847)]
    > **Authors:** Xinshuo Weng, Kris Kitani <br>
    > **Abstract:**   Monocular 3D scene understanding tasks, such as object size estimation, heading angle estimation and 3D localization, is challenging. Successful modern day methods for 3D scene understanding require the use of a 3D sensor such as a depth camera, a stereo camera or LiDAR. On the other hand, single image based methods have significantly worse performance, but rightly so, as there is little explicit depth information in a 2D image. In this work, we aim at bridging the performance gap between 3D sensing and ...

- **Stereo R-CNN based 3D Object Detection for Autonomous Driving** [CVPR 2019] [[Paper](https://arxiv.org/abs/1902.09738)]
    > **Authors:** Peiliang Li, Xiaozhi Chen, Shaojie Shen <br>
    > **Abstract:**   We propose a 3D object detection method for autonomous driving by fully exploiting the sparse and dense, semantic and geometry information in stereo imagery. Our method, called Stereo R-CNN, extends Faster R-CNN for stereo inputs to simultaneously detect and associate object in left and right images. We add extra branches after stereo Region Proposal Network (RPN) to predict sparse keypoints, viewpoints, and object dimensions, which are combined with 2D left-right boxes to calculate a coarse 3D object bo...

- **PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud** [CVPR 2019] [[Paper](https://arxiv.org/abs/1812.04244), [Code](https://github.com/sshaoshuai/PointRCNN)]
    > **Authors:** Shaoshuai Shi, Xiaogang Wang, Hongsheng Li <br>
    > **Abstract:**   In this paper, we propose PointRCNN for 3D object detection from raw point cloud. The whole framework is composed of two stages: stage-1 for the bottom-up 3D proposal generation and stage-2 for refining proposals in the canonical coordinates to obtain the final detection results. Instead of generating proposals from RGB image or projecting point cloud to bird's view or voxels as previous methods do, our stage-1 sub-network directly generates a small number of high-quality 3D proposals from point cloud in...


### 2018

- **LMNet: Real-time Multiclass Object Detection on CPU using 3D LiDAR** [ACIRS 2018] [[Paper](https://arxiv.org/pdf/1805.04902.pdf), [Code](https://github.com/CPFL/Autoware/tree/feature/cnn_lidar_detection)]
    > **Authors:** Kazuki Minemura, Hengfui Liau, Abraham Monrroy, Shinpei Kato <br>
    > **Abstract:** This paper describes an optimized single-stage deep convolutional neural network to detect objects in urban environments, using nothing more than point cloud data. This feature enables our method to work regardless the time of the day and the lighting conditions. The proposed network structure employs dilated convolutions to gradually increase the perceptive field as depth increases, this helps to reduce the computation time by about 30%. The network input consists of five perspective representations of the unorganized...

- **SBNet: Sparse Blocks Network for Fast Inference** [Arxiv] [[Paper](https://arxiv.org/pdf/1801.02108.pdf), [Code](https://github.com/uber/sbnet)]
    > **Authors:** Mengye Ren, Andrei Pokrovsky, Bin Yang, Raquel Urtasun <br>
    > **Abstract:** Conventional deep convolutional neural networks (CNNs) apply convolution operators uniformly in space across all feature maps for hundreds of layers - this incurs a high computational cost for real-time applications. For many problems such as object detection and semantic segmentation, we are able to obtain a low-cost computation mask, either from a priori problem knowledge, or from a low-resolution segmentation network. We show that such computation masks can be used to reduce computation in the high-resolution...

- **Joint 3D Proposal Generation and Object Detection from View Aggregation** [IROS 2018] [[Paper](https://arxiv.org/pdf/1712.02294), [Code](https://github.com/kujason/avod)]
    > **Authors:** Jason Ku, Melissa Mozifian, Jungwook Lee, Ali Harakeh, Steven Waslander <br>
    > **Abstract:** We present AVOD, an Aggregate View Object Detection network for autonomous driving scenarios. The proposed neural network architecture uses LIDAR point clouds and RGB images to generate features that are shared by two subnetworks: a region proposal network (RPN) and a second stage detector network. The proposed RPN uses a novel architecture capable of performing multimodal feature fusion on high resolution feature maps to generate reliable 3D object proposals for multiple object classes in road scenes. ...

- **RoarNet: A Robust 3D Object Detection based on RegiOn Approximation Refinement** [Arxiv] [[Paper](https://arxiv.org/pdf/1811.03818v1.pdf), [Code](https://github.com/Kiwoo/RoarNet)]
    > **Authors:** Kiwoo Shin, Youngwook Paul Kwon, Masayoshi Tomizuka <br>
    > **Abstract:** We present RoarNet, a new approach for 3D object detection from a 2D image and 3D Lidar point clouds. Based on two-stage object detection framework with PointNet as our backbone network, we suggest several novel ideas to improve 3D object detection performance. The first part of our method, RoarNet_2D, estimates the 3D poses of objects from a monocular image, which approximates where to examine further, and derives multiple candidates that are geometrically feasible. ...

- **Eliminating the Blind Spot: Adapting 3D Object Detection and Monocular Depth Estimation to 360◦ Panoramic Imagery** [ECCV 2018][[Paper](https://arxiv.org/pdf/1808.06253v1.pdf), [Code](https://github.com/gdlg/panoramic-depth-estimation)]
    > **Authors:** Grégoire Payen de La Garanderie, Amir Atapour Abarghouei, Toby P. Breckon <br>
    > **Abstract:** Recent automotive vision work has focused almost exclusively on processing forward-facing cameras. However, future autonomous vehicles will not be viable without a more comprehensive surround sensing, akin to a human driver, as can be provided by 360° panoramic cameras. We present an approach to adapt contemporary deep network architectures developed on conventional rectilinear imagery to work on equirectangular 360° panoramic imagery. To address the lack of annotated panoramic automotive datasets availability, ...

- **PointFusion: Deep Sensor Fusion for 3D Bounding Box Estimation** [CVPR 2018] [[Paper](https://arxiv.org/abs/1711.10871)]
    > **Authors:** Danfei Xu, Dragomir Anguelov, Ashesh Jain <br>
    > **Abstract:**   We present PointFusion, a generic 3D object detection method that leverages both image and 3D point cloud information. Unlike existing methods that either use multi-stage pipelines or hold sensor and dataset-specific assumptions, PointFusion is conceptually simple and application-agnostic. The image data and the raw point cloud data are independently processed by a CNN and a PointNet architecture, respectively. The resulting outputs are then combined by a novel fusion network, which predicts multiple 3D box hypotheses and their confi...

- **Frustum PointNets for 3D Object Detection from RGB-D Data** [CVPR 2018] [[Paper](https://arxiv.org/abs/1711.08488), [Code](https://github.com/charlesq34/frustum-pointnets)]
    > **Authors:** Charles R. Qi, Wei Liu, Chenxia Wu, Hao Su, Leonidas J. Guibas <br>
    > **Abstract:**   In this work, we study 3D object detection from RGB-D data in both indoor and outdoor scenes. While previous methods focus on images or 3D voxels, often obscuring natural 3D patterns and invariances of 3D data, we directly operate on raw point clouds by popping up RGB-D scans. However, a key challenge of this approach is how to efficiently localize objects in point clouds of large-scale scenes (region proposal). Instead of solely relying on 3D proposals, our method leverages both mature 2D object detectors and advanced 3D deep learni...

- **Fast and Furious: Real Time End-to-End 3D Detection, Tracking and Motion Forecasting with a Single Convolutional Net** [publication][[Paper](http://openaccess.thecvf.com/content_cvpr_2018/papers/Luo_Fast_and_Furious_CVPR_2018_paper.pdf)]
    > **Authors:** Wenjie Luo, Bin Yang, Raquel Urtasun
    > **Abstract:** In this paper we propose a novel deep neural network that is able to jointly reason about 3D detection, tracking and motion forecasting given data captured by a 3D sensor. By jointly reasoning about these tasks, our holistic approach is more robust to occlusion as well as sparse data at range. Our approach performs 3D convolutions across space and time over a bird’s eye view representation of the 3D world, which is very efficient in terms of both memory...

- **PIXOR: Real-time 3D Object Detection from Point Clouds** [CVPR 2018] [[Paper](https://arxiv.org/abs/1902.06326)]
    > **Authors:** Bin Yang, Wenjie Luo, Raquel Urtasun <br>
    > **Abstract:**   We address the problem of real-time 3D object detection from point clouds in the context of autonomous driving. Computation speed is critical as detection is a necessary component for safety. Existing approaches are, however, expensive in computation due to high dimensionality of point clouds. We utilize the 3D data more efficiently by representing the scene from the Bird's Eye View (BEV), and propose PIXOR, a proposal-free, single-stage detector that outputs oriented 3D object estimates decoded from pixel-wise...

- **Multi-Level Fusion based 3D Object Detection from Monocular Images** [CVPR 2018][[Paper](http://openaccess.thecvf.com/content_cvpr_2018/papers/Xu_Multi-Level_Fusion_Based_CVPR_2018_paper.pdf)]
    > **Authors:** Bin Xu, Zhenzhong Chen
    > **Abstract:** In this paper, we present an end-to-end multi-level fusion based framework for 3D object detection from a single monocular image. The whole network is composed of two parts: one for 2D region proposal generation and another for simultaneously predictions of objects’ 2D locations, orientations, dimensions, and 3D locations. With the help of a stand-alone module to estimate the disparity and compute the 3D point cloud, we introduce the multi-level fusion scheme. ...

- **SECOND: Sparsely Embedded Convolutional Detection** [Sensors 2018] [[Paper](https://pdfs.semanticscholar.org/5125/a16039cabc6320c908a4764f32596e018ad3.pdf), [Code](https://github.com/traveller59/second.pytorch)]
    > **Authors:** Yan Yan, Yuxing Mao, Bo Li <br>
    > **Abstract:** LiDAR-based or RGB-D-based object detection is used in numerous applications, ranging from autonomous driving to robot vision. Voxel-based 3D convolutional networks have been used for some time to enhance the retention of information when processing point cloud LiDAR data. However, problems remain, including a slow inference speed and low orientation estimation performance. We therefore investigate an improved sparse convolution method for such networks, which significantly increases the speed of both training and inference. We also introduce a new...

### 2017

- **Multi-View 3D Object Detection Network for Autonomous Driving** [CVPR 2017] [[Paper](https://arxiv.org/pdf/1611.07759), [Code](https://github.com/bostondiditeam/MV3D)]
    > **Authors:** Xiaozhi Chen, Huimin Ma, Ji Wan, Bo Li, Tian Xia <br>
    > **Abstract:** This paper aims at high-accuracy 3D object detection in autonomous driving scenario. We propose Multi-View 3D networks (MV3D), a sensory-fusion framework that takes both LIDAR point cloud and RGB images as input and predicts oriented 3D bounding boxes. We encode the sparse 3D point cloud with a compact multi-view representation. The network is composed of two subnetworks: one for 3D object proposal generation and another for multi-view feature fusion. ...
