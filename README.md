# Semantic SLAM

![license](https://img.shields.io/bower/l/bootstrap.svg?color=blue) <a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>

This on-going project is Semantic SLAM using ROS, ORB SLAM and PSPNet101. Will be used in Robotics for semantic understanding and navigation.

Now we can get visualized semantic map.

![semantic SLAM](https://github.com/1989Ryan/Semantic_SLAM/blob/master/semantic_map.png?raw=true)

## Acknowledgement 

The state-of-the-art methodologies are achieved by team of [Raul Mur-Artal](https://github.com/raulmur) for [ORB_SLAM](https://github.com/raulmur/ORB_SLAM2) and team of [Hengshuang Zhao](https://github.com/hszhao) for [PSPNet](https://github.com/hszhao/PSPNet). Thanks for their great works.

The implementation of [PSPNet by keras](https://github.com/Vladkryvoruchko/PSPNet-Keras-tensorflow) is presented by [VladKry](https://github.com/Vladkryvoruchko). Thanks for their team's work.

## Project Structure

```
map_engine/
    map_engine.py
Third_Part/
    ORB_SLAM/
    PSPNet_Keras_tensorflow/
test/
.gitignore
README.md
```

## TODO

* ~~Publish the cloud point infomation~~
* ~~Encode the cloud point and visual descriptor with semantic information~~
* Clustering the cloud points into a single location point
* Visualize the result
* Run in the KITTI dataset
* Run in XJTU campus
* Connect all the elements into a single project
* Inference accelerate
