# Awesome Connected and Automated Vehicles

## Arxiv Link Parser

This is a simple Pyhton script I use to get papers' information from their Arxiv
page and format it nicely in Markdown.

### Usage

This script only needs the URL to the paper's Arxive abstract page to generate
and display the formatted Markdown code. The output is also copied to clipboard
so you can easily paste it into a Markdown script, but this may only work on a 
Mac computer. 

Here is an example:

```bash
python arxiveLinkParser.py https://arxiv.org/abs/1809.02165
```

For the above example, the output is:

```markdown
- **Deep Learning for Generic Object Detection: A Survey** [Arxiv] [[Paper](https://arxiv.org/abs/1809.02165)]
    > **Authors:** Li Liu, Wanli Ouyang, Xiaogang Wang, Paul Fieguth, Jie Chen, Xinwang Liu, Matti Pietikäinen <br>
    > **Abstract:**   Generic object detection, aiming at locating object instances from a large number of predefined categories in natural images, is one of the most fundamental and challenging problems in computer vision. Deep learning techniques have emerged in recent years as powerful methods for learning feature representations directly from data, and have led to remarkable breakthroughs in the field of generic object detection. Given this time of rapid evolution, the goal of this paper is to provide a comprehensive survey of the recent achievements ...
```

Which will look like this in Markdown:

- **Deep Learning for Generic Object Detection: A Survey** [Arxiv] [[Paper](https://arxiv.org/abs/1809.02165)]
    > **Authors:** Li Liu, Wanli Ouyang, Xiaogang Wang, Paul Fieguth, Jie Chen, Xinwang Liu, Matti Pietikäinen <br>
    > **Abstract:**   Generic object detection, aiming at locating object instances from a large number of predefined categories in natural images, is one of the most fundamental and challenging problems in computer vision. Deep learning techniques have emerged in recent years as powerful methods for learning feature representations directly from data, and have led to remarkable breakthroughs in the field of generic object detection. Given this time of rapid evolution, the goal of this paper is to provide a comprehensive survey of the recent achievements ...

----
There are also a few flags you can use to include more information about the paper:

- -p : Paper's publication (default: Arxiv)
- -c : Link to paper's code
- -m : Maximum abstract preview length in characters (defaults: 550)

For example:

```bash
python arxiveLinkParser.py https://arxiv.org/abs/1611.07759 -c https://github.com/bostondiditeam/MV3D -p "CVPR 2017"
```

will output:

```markdown
- **Multi-View 3D Object Detection Network for Autonomous Driving** [CVPR 2017] [[Paper](https://arxiv.org/abs/1611.07759), [Code](https://github.com/bostondiditeam/MV3D)]
    > **Authors:** Xiaozhi Chen, Huimin Ma, Ji Wan, Bo Li, Tian Xia <br>
    > **Abstract:**   This paper aims at high-accuracy 3D object detection in autonomous driving scenario. We propose Multi-View 3D networks (MV3D), a sensory-fusion framework that takes both LIDAR point cloud and RGB images as input and predicts oriented 3D bounding boxes. We encode the sparse 3D point cloud with a compact multi-view representation. The network is composed of two subnetworks: one for 3D object proposal generation and another for multi-view feature fusion. The proposal network generates 3D candidate boxes efficiently from the bird's eye v...
```

Which looks like this in Markdown:

- **Multi-View 3D Object Detection Network for Autonomous Driving** [CVPR 2017] [[Paper](https://arxiv.org/abs/1611.07759), [Code](https://github.com/bostondiditeam/MV3D)]
    > **Authors:** Xiaozhi Chen, Huimin Ma, Ji Wan, Bo Li, Tian Xia <br>
    > **Abstract:**   This paper aims at high-accuracy 3D object detection in autonomous driving scenario. We propose Multi-View 3D networks (MV3D), a sensory-fusion framework that takes both LIDAR point cloud and RGB images as input and predicts oriented 3D bounding boxes. We encode the sparse 3D point cloud with a compact multi-view representation. The network is composed of two subnetworks: one for 3D object proposal generation and another for multi-view feature fusion. The proposal network generates 3D candidate boxes efficiently from the bird's eye v...
