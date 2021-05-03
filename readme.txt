No additional packages are necessary for inference using the predict function in main.py
We trained & tested our pipeline on kaggle & google colab, where the inference works out of the box.

We have added some of the test images in sample_images folder
*Note: All the characters present in sample_images were not included in final submission model.

Somethings to take note of:
  - Image segmentation works when there is a line joining all the characters.
    Or if all characters with their own individual overhead lines are on same side.
    ie they are not placed in zig zag. We assumed it since the input will be a hindi word.
    It works without it too, but in some cases it may not.
    
    ex: type0.jpeg


  - segmentation process can handle input images with noisy lines (both horizontal & vertical)
    for example find pass-type1-[01].jpeg

    Although very thick noise lines do not always work well.

  - Handles slanting words, or arching words.
    ex: ravan.jpeg
  - Words where character is separate from overhead line
    ex: ravan.jpeg




